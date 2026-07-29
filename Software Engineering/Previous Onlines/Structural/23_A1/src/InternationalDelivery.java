public class InternationalDelivery extends Delivery {

    public InternationalDelivery(
            Item item,
            DeliveryMode deliveryMode) {

        super(item, deliveryMode);
    }

    @Override
    protected double getRegionCharge() {
        return 500;
    }

    @Override
    protected String getRegionName() {
        return "International Delivery";
    }

    @Override
    protected String getStandardDeliveryTime() {
        return "2-3 weeks";
    }

    @Override
    protected RegionCategory getRegionCategory() {
        return RegionCategory.INTERNATIONAL;
    }
}
