public class Express extends DeliveryMode{

    Express(DeliveryRegion region, Item item , int miles) {
        super(region, item, miles);
    }

    @Override
    public double getTotalCost() {
        return super.getTotalCost() + 10;
    }

    @Override
    public String getTime() {
        return super.region.isInternational() ? "1 week" : "2 days";
    }
}
