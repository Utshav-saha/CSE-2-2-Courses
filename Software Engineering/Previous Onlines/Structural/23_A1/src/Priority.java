public class Priority extends DeliveryMode{

    Priority(DeliveryRegion region, Item item , int miles) {
        super(region, item, miles);
    }

    @Override
    public double getTotalCost() {
        return super.getTotalCost() + 25;
    }

    @Override
    public String getTime() {
        return super.region.isInternational() ? "5 days" : "1 day";
    }
}
