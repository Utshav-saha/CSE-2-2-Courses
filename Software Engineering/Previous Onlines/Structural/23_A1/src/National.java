public class National implements DeliveryRegion{
    @Override
    public double getRegionCost(int miles) {
        return miles + 20;
    }

    @Override
    public boolean isInternational() {
        return false;
    }

    @Override
    public String getTime() {
        return "1-2 weeks";
    }
}
