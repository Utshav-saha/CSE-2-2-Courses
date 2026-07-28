import java.util.ArrayList;
import java.util.List;

public class SetMenu implements OrderItem{

    private String name;
    private double total = 0;
    private List<Food> items = new ArrayList<>();

    public SetMenu(String name) {
        this.name = name;
    }

    @Override
    public void print() {
        System.out.println("SetMenu: " + name);
        for (Food f : items){
            f.print();
        }


    }

    @Override
    public double getPrice() {
        for (Food f : items){
            total += f.getPrice();
        }
        total = (total*0.9);
        return total;
    }

    public void addFood(Food food) {
        items.add(food);
    }
}
