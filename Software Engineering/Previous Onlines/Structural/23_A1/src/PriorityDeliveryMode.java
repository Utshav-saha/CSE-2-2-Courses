public class PriorityDeliveryMode implements DeliveryMode {

    @Override
    public double getAdditionalCharge() {
        return 25;
    }

    @Override
    public String getEstimatedTime(
            RegionCategory category,
            String standardDeliveryTime) {

        if (category == RegionCategory.INTERNATIONAL) {
            return "5 days";
        }

        return "1 day";
    }

    @Override
    public String getModeName() {
        return "Priority Delivery";
    }
}

