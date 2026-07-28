import java.util.ArrayList;
import java.util.List;

public class GroceryPackage extends GroceryItem{

    private String name;
    private double total = 0;
    private List<GroceryItem> items = new ArrayList<>();

    public GroceryPackage(String name) {
        this.name = name;
    }

    @Override
    public void print() {
        System.out.println("Package: " + name);
        for (OrderItem f : items){
            f.print();
        }

    }

    @Override
    public double getPrice() {
        for (OrderItem f : items){
            total += f.getPrice();
        }

        return total;
    }

    public void add(GroceryItem grocery) {
        items.add(grocery);
    }
}
