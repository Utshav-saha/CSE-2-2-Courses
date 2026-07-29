public interface DeliveryMode {

    double getAdditionalCharge();

    String getEstimatedTime(
            RegionCategory category,
            String standardDeliveryTime
    );

    String getModeName();
}
