public class International implements DeliveryRegion{
    @Override
    public double getRegionCost(int miles) {
        return 500;
    }

    @Override
    public boolean isInternational() {
        return true;
    }

    @Override
    public String getTime() {
        return "2-3 weeks";
    }
}
