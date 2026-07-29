abstract class Delivery {

    protected final Item item;
    protected final DeliveryMode deliveryMode;

    public Delivery(Item item, DeliveryMode deliveryMode) {
        this.item = item;
        this.deliveryMode = deliveryMode;
    }

    protected abstract double getRegionCharge();

    protected abstract String getRegionName();

    protected abstract String getStandardDeliveryTime();

    protected abstract RegionCategory getRegionCategory();

    public double getTotalCost() {
        return item.getPrice()
                + getRegionCharge()
                + deliveryMode.getAdditionalCharge();
    }

    public String getEstimatedTime() {
        return deliveryMode.getEstimatedTime(
                getRegionCategory(),
                getStandardDeliveryTime()
        );
    }

    public String getDescription() {
        return item.getDescription()
                + " + "
                + getRegionName()
                + " + "
                + deliveryMode.getModeName();
    }

    public void displayDetails() {
        System.out.println("Order: " + getDescription());
        System.out.printf("Total Cost: $%.2f%n", getTotalCost());
        System.out.println(
                "Estimated Delivery Time: " + getEstimatedTime()
        );
    }
}
