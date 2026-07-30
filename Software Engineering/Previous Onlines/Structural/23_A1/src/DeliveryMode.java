abstract class DeliveryMode implements Mode{

    protected DeliveryRegion region;
    protected Item item;
    protected int miles;

    DeliveryMode(DeliveryRegion region, Item item, int miles) {
        this.region = region;
        this.item = item;
        this.miles = miles;
    }

    @Override
    public double getTotalCost() {
        return region.getRegionCost(miles) + item.getPrice();
    }

    @Override
    public String getTime() {
        return region.getTime();
    }
}
