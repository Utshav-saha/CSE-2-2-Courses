public interface DeliveryRegion {
    double getRegionCost(int miles);
    boolean isInternational();
    String getTime();
}
