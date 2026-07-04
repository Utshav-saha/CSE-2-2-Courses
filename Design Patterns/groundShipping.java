public class groundShipping implements Shipping{

    @Override
    public double getCost(Order order) {
        if (order.getTotal() > 100) {
            return 0;
        }
        return Math.max(10, order.getTotalWeight() * 1.5);
    }
}
