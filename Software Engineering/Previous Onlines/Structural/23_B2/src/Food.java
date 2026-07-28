public class Food implements OrderItem{

    private String name;
    private int price;

    public Food(String name, int price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public void print() {
        System.out.println("Food: " + name + "(" + price + ")");
    }

    @Override
    public double getPrice() {
        return price;
    }
}
