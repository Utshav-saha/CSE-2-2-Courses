public class Gift implements Item {
    private final String description;
    private final double price;

    public Gift(String description, double price) {
        this.description = description;
        this.price = price;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public String getDescription() {
        return description;
    }
}
