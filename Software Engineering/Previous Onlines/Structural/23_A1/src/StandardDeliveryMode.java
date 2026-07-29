public class StandardDeliveryMode implements DeliveryMode {

    @Override
    public double getAdditionalCharge() {
        return 0;
    }

    @Override
    public String getEstimatedTime(
            RegionCategory category,
            String standardDeliveryTime) {

        return standardDeliveryTime;
    }

    @Override
    public String getModeName() {
        return "Standard Delivery";
    }
}