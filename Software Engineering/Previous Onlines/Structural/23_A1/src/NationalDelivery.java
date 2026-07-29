public class NationalDelivery extends Delivery {

    private final int miles;

    public NationalDelivery(
            Item item,
            int miles,
            DeliveryMode deliveryMode) {

        super(item, deliveryMode);
        this.miles = miles;
    }

    @Override
    protected double getRegionCharge() {
        return miles + 20;
    }

    @Override
    protected String getRegionName() {
        return "National Delivery";
    }

    @Override
    protected String getStandardDeliveryTime() {
        return "1-2 weeks";
    }

    @Override
    protected RegionCategory getRegionCategory() {
        return RegionCategory.DOMESTIC;
    }
}
