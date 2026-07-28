public class Grocery extends GroceryItem{

    private String name;
    private int price;

    public Grocery(String name, int price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public void print() {
        System.out.println("Grocery: " + name + "(" + price + ")");
    }

    @Override
    public double getPrice() {
        return price;
    }
}
