public class Local implements DeliveryRegion{
    @Override
    public double getRegionCost(int miles) {
        return miles;
    }

    @Override
    public boolean isInternational() {
        return false;
    }

    @Override
    public String getTime() {
        return "1 week";
    }
}
