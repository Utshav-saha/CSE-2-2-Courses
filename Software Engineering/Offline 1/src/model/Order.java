package model;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Represents a placed food order.
 *
 * Design note for the assignment:
 * This class works, but its construction API is intentionally awkward.
 * The long constructor mixes required fields, optional fields, defaults,
 * validation, and pricing flags. Students should refactor this design without
 * changing the observable behavior of the program.
 */
public class Order {
    public static final double DELIVERY_FEE = 80.0;
    public static final double RUSH_FEE = 120.0;
    public static final double GIFT_WRAP_FEE = 50.0;

    private final String orderId;
    private final String customerName;
    private final String phone;
    private final DeliveryType deliveryType;
    private final String deliveryAddress;
    private final PaymentMethod paymentMethod;
    private final LocalDateTime scheduledTime;
    private final String couponCode;
    private final boolean giftWrap;
    private final boolean cutleryRequired;
    private final int loyaltyPointsToRedeem;
    private final boolean rushOrder;
    private final List<OrderItem> items;
    private final String specialInstructions;

    Order(String orderId,
          String customerName,
          String phone,
          DeliveryType deliveryType,
          String deliveryAddress,
          PaymentMethod paymentMethod,
          LocalDateTime scheduledTime,
          String couponCode,
          boolean giftWrap,
          boolean cutleryRequired,
          int loyaltyPointsToRedeem,
          boolean rushOrder,
          List<OrderItem> items,
          String specialInstructions) {

        this.orderId = orderId;
        this.customerName = customerName;
        this.phone = phone;

        this.deliveryType = deliveryType ;
        this.paymentMethod = paymentMethod;
        this.scheduledTime = scheduledTime;
        this.couponCode = couponCode;
        this.giftWrap = giftWrap;
        this.cutleryRequired = cutleryRequired;
        this.loyaltyPointsToRedeem =loyaltyPointsToRedeem;
        this.rushOrder = rushOrder;
        this.specialInstructions = specialInstructions ;

        this.deliveryAddress = deliveryAddress;

        this.items = Collections.unmodifiableList(new ArrayList<>(items));
    }

//    public Order(String orderId, String customerName, String phone, List<OrderItem> items) {
//        this(orderId, customerName, phone, DeliveryType.PICKUP, "", PaymentMethod.CASH,
//                null, "", false, true, 0, false, items, "");
//    }

    public String getOrderId() {
        return orderId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public String getPhone() {
        return phone;
    }

    public DeliveryType getDeliveryType() {
        return deliveryType;
    }

    public String getDeliveryAddress() {
        return deliveryAddress;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }

    public LocalDateTime getScheduledTime() {
        return scheduledTime;
    }

    public String getCouponCode() {
        return couponCode;
    }

    public boolean isGiftWrap() {
        return giftWrap;
    }

    public boolean isCutleryRequired() {
        return cutleryRequired;
    }

    public int getLoyaltyPointsToRedeem() {
        return loyaltyPointsToRedeem;
    }

    public boolean isRushOrder() {
        return rushOrder;
    }

    public List<OrderItem> getItems() {
        return items;
    }

    public String getSpecialInstructions() {
        return specialInstructions;
    }

    public double getSubtotal() {
        return items.stream().mapToDouble(OrderItem::getSubtotal).sum();
    }

    public double getDiscount() {
        double couponDiscount = 0.0;
        if ("WELCOME10".equals(couponCode)) {
            couponDiscount = getSubtotal() * 0.10;
        } else if ("FAMILY15".equals(couponCode) && getSubtotal() >= 1000.0) {
            couponDiscount = getSubtotal() * 0.15;
        }

        double loyaltyDiscount = Math.min(loyaltyPointsToRedeem, 100);
        return couponDiscount + loyaltyDiscount;
    }

    public double getServiceCharges() {
        double charges = 0.0;
        if (deliveryType == DeliveryType.DELIVERY) {
            charges += DELIVERY_FEE;
        }
        if (rushOrder) {
            charges += RUSH_FEE;
        }
        if (giftWrap) {
            charges += GIFT_WRAP_FEE;
        }
        return charges;
    }

    public double getTotal() {
        return Math.max(0.0, getSubtotal() + getServiceCharges() - getDiscount());
    }

}
