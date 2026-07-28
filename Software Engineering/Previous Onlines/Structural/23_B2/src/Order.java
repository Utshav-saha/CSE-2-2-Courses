import java.util.ArrayList;
import java.util.List;
public class Order {
    private List<OrderItem> items = new ArrayList<>();
    public void add(OrderItem item) {
        items.add(item);
    }
    public double getTotalPrice() {
        double total = 0;
        for (OrderItem item : items) {
            total += item.getPrice();
        }
        return total;
    }
    public void printReceipt() {
        System.out.println("========== RECEIPT ==========");
        for (OrderItem item : items) {
            item.print();
        }
        System.out.println("-----------------------------");
        System.out.printf("Total Bill: £%.2f%n", getTotalPrice());
    }
}
