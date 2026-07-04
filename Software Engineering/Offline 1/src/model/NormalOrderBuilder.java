package model;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

import static util.TextUtils.requireNonBlank;


public class NormalOrderBuilder implements OrderBuilder{
    private  String orderId;
    private  String customerName;
    private  String phone;
    private  DeliveryType deliveryType = DeliveryType.PICKUP;
    private  String deliveryAddress = "";
    private  PaymentMethod paymentMethod = PaymentMethod.CASH;
    private  LocalDateTime scheduledTime = null;
    private  String couponCode = "";
    private  boolean giftWrap = false;
    private  boolean cutleryRequired = true;
    private  int loyaltyPointsToRedeem = 0;
    private  boolean rushOrder = false;
    private  List<OrderItem> items;
    private  String specialInstructions = "";

    public NormalOrderBuilder(String orderId, String customerName, String phone , List<OrderItem> items) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.phone = phone;
        this.items = items;
    }

    @Override
    public void setDeliveryType(DeliveryType deliveryType){
        this.deliveryType = deliveryType;
    };

    @Override
    public void setDeliveryAddress(String deliveryAddress){
        this.deliveryAddress = deliveryAddress;
    };

    @Override
    public void setPaymentMethod(PaymentMethod paymentMethod){
        this.paymentMethod = paymentMethod;
    };

    @Override
    public void setScheduledTime(LocalDateTime scheduledTime){
        this.scheduledTime = scheduledTime;
    };

    @Override
    public void setCouponCode(String couponCode){
        this.couponCode = couponCode;
    };

    @Override
    public void setGiftWrap(boolean giftWrap){
        this.giftWrap = giftWrap;
    };

    @Override
    public void setCutlery(boolean cutlery){
        this.cutleryRequired = cutlery;
    };

    @Override
    public void setLoyaltyPoints(int loyaltyPoints){
        this.loyaltyPointsToRedeem = loyaltyPoints;
    };

    @Override
    public void setSpecialInstructions(String specialInstructions){
        this.specialInstructions = specialInstructions;
    };

    @Override
    public void setRushOrder(boolean rushOrder){
        this.rushOrder = rushOrder;
    };



    public Order getResult(){

        if (this.deliveryType == DeliveryType.DELIVERY) {
            this.deliveryAddress = requireNonBlank(deliveryAddress, "Delivery address");
        } else {
            this.deliveryAddress = deliveryAddress != null ? deliveryAddress.trim() : "";
        }

        this.orderId = requireNonBlank(orderId, "Order id");
        this.customerName = requireNonBlank(customerName, "Customer name");
        this.phone = requireNonBlank(phone, "Phone");

        this.couponCode = couponCode != null ? couponCode.trim().toUpperCase() : "";
        this.specialInstructions = specialInstructions != null ? specialInstructions.trim() : "";

        this.loyaltyPointsToRedeem = Math.max(0, loyaltyPointsToRedeem);

        Objects.requireNonNull(items, "Items cannot be null");
        if (items.isEmpty()) {
            throw new IllegalArgumentException("Order must contain at least one item");
        }


        return new Order(orderId,
                customerName,
                phone,
                deliveryType,
                deliveryAddress,
                paymentMethod,
                scheduledTime,
                couponCode,
                giftWrap,
                cutleryRequired,
                loyaltyPointsToRedeem,
                rushOrder,
                items,
                specialInstructions);
    };

}
