public class Order {
//    private String shipping;
    private Shipping shipping;
    private double total;
    private double totalWeight;

    public Order(double total, double totalWeight) {
        this.total = total;
        this.totalWeight = totalWeight;
    }

    public double getTotal() { return total; }
    public double getTotalWeight() { return totalWeight; }

//    // VIOLATION OF OCP: Hardcoded logic inside the class
//    // Now if I want to add a new shipping method i have to edit this class again
//    public double getShippingCost() {
//        if (shipping.equals("ground")) {
//            if (getTotal() > 100) {
//                return 0;
//            }
//            return Math.max(10, getTotalWeight() * 1.5);
//        }
//
//        if (shipping.equals("air")) {
//            return Math.max(20, getTotalWeight() * 3);
//        }
//
//        return 0;
//    }

    // We can change the shipping method at runtime
    public void setShippingType(Shipping shipping) {
        this.shipping = shipping;
    }

    // The Order class no longer cares HOW the cost is calculated.
    // It just asks the Shipping object to do it.
    public double getShippingCost() {
        return shipping.getCost(this);
    }
}