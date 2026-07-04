package model;

import java.time.LocalDateTime;

public class OrderDirector {

    public void DeliveryOrderBuild(OrderBuilder builder, String address, String coupon, boolean rushOrder, String specialInstructions) {

        builder.setDeliveryType(DeliveryType.DELIVERY);
        builder.setDeliveryAddress(address);
        builder.setPaymentMethod(PaymentMethod.CASH);
        builder.setCouponCode(coupon);
        builder.setRushOrder(rushOrder);
        builder.setSpecialInstructions(specialInstructions);

    }

    public void PickupOrderBuild(OrderBuilder builder) {
        builder.setDeliveryType(DeliveryType.PICKUP);
        builder.setPaymentMethod(PaymentMethod.CASH);

    }

    public void ScheduledGiftOrderBuild(OrderBuilder builder, String address, LocalDateTime scheduledTime) {
        builder.setDeliveryType(DeliveryType.DELIVERY);
        builder.setDeliveryAddress(address);
        builder.setPaymentMethod(PaymentMethod.CARD);
        builder.setScheduledTime(scheduledTime);
        builder.setCouponCode("WELCOME10");
        builder.setGiftWrap(true);
        builder.setCutlery(false);
        builder.setLoyaltyPoints(25);
        builder.setSpecialInstructions("Please call before delivery");
    }

    public void FamilyOrderBuild(OrderBuilder builder, String address, String coupon, int loyaltyPoints, String specialInstructions) {

        builder.setDeliveryType(DeliveryType.DELIVERY);
        builder.setDeliveryAddress(address);
        builder.setPaymentMethod(PaymentMethod.MOBILE_BANKING);
        builder.setCouponCode(coupon);
        builder.setLoyaltyPoints(loyaltyPoints);
        builder.setRushOrder(true);
        builder.setSpecialInstructions(specialInstructions);

    }
}
