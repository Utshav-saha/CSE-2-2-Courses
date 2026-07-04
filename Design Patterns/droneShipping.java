public class droneShipping implements Shipping{
    @Override
    public double getCost(Order order) {
        return 50.0;
    }
}
