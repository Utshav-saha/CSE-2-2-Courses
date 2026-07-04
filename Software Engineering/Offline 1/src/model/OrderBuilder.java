package model;

import java.time.LocalDateTime;
import java.util.List;

public interface OrderBuilder {

    public void setDeliveryType(DeliveryType deliveryType);
    public void setDeliveryAddress(String deliveryAddress);
    public void setPaymentMethod(PaymentMethod paymentMethod);
    public void setScheduledTime(LocalDateTime scheduledTime);
    public void setCouponCode(String couponCode);
    public void setGiftWrap(boolean giftWrap);
    public void setCutlery(boolean cutlery);
    public void setLoyaltyPoints(int loyaltyPoints);
    public void setSpecialInstructions(String specialInstructions);
    public void setRushOrder(boolean rushOrder);

}
