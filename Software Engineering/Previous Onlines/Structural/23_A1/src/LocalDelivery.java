public class LocalDelivery extends Delivery {

    private final int miles;

    public LocalDelivery(
            Item item,
            int miles,
            DeliveryMode deliveryMode) {

        super(item, deliveryMode);
        this.miles = miles;
    }

    @Override
    protected double getRegionCharge() {
        return miles;
    }

    @Override
    protected String getRegionName() {
        return "Local Delivery";
    }

    @Override
    protected String getStandardDeliveryTime() {
        return "1 week";
    }

    @Override
    protected RegionCategory getRegionCategory() {
        return RegionCategory.DOMESTIC;
    }
}
