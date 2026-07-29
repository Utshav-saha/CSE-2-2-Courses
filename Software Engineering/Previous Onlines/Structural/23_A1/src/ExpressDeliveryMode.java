public class ExpressDeliveryMode implements DeliveryMode {

    @Override
    public double getAdditionalCharge() {
        return 10;
    }

    @Override
    public String getEstimatedTime(
            RegionCategory category,
            String standardDeliveryTime) {

        if (category == RegionCategory.INTERNATIONAL) {
            return "1 week";
        }

        return "2 days";
    }

    @Override
    public String getModeName() {
        return "Express Delivery";
    }
}