
abstract class State {
    protected Order order;
    State(Order order){
        this.order = order;
    }
    public abstract void next();
    public void cancel() {
        order.setState(new Cancelled(order));
    }
    public abstract void display();
}

class Placed extends State {
    Placed(Order order){
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Confirmed(order));
    }

    @Override
    public void display() {
        System.out.println("Current status: Placed");
    }
}

class Confirmed extends State {
    Confirmed(Order order){
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Shipped(order));
    }

    @Override
    public void display() {
        System.out.println("Current status: Confirmed");
    }
}

class Shipped extends State {
    Shipped(Order order){
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Delivered(order));
    }

    @Override
    public void display() {
        System.out.println("Current status: Shipped");
    }

    @Override
    public void cancel(){
        System.out.println("Can't cancel shipped order");
    }
}

class Delivered extends State {
    Delivered(Order order){
        super(order);
    }

    @Override
    public void next() {
        System.out.println("Order delivered, can't continue");
    }

    @Override
    public void display() {
        System.out.println("Current status: Delivered");
    }

    @Override
    public void cancel(){
        System.out.println("Can't cancel delivered order");
    }
}

class Cancelled extends State {
    Cancelled(Order order){
        super(order);
    }

    @Override
    public void next() {
        System.out.println("Order cancelled, can't continue");
    }

    @Override
    public void cancel(){
        System.out.println("Order already cancelled");
    }

    @Override
    public void display() {
        System.out.println("Current status: Cancelled");
    }
}

class Order{
    private State state;
    Order(){
        this.state = new Placed(this);
    }

    public void setState(State state){
        this.state = state;
    }
    public void next(){
        state.next();
    }
    public void cancel(){
        state.cancel();
    }
    public void display(){
        state.display();
    }
}
public class Main {
    public static void main(String[] args) {

        // -------- Normal order --------
        System.out.println("=== ORDER 1 ===");

        Order order1 = new Order();

        order1.display();    // Placed

        order1.next();
        order1.display();    // Confirmed

        order1.next();
        order1.display();    // Shipped

        // invalid cancellation
        order1.cancel();     // Cannot cancel after shipment

        order1.next();
        order1.display();    // Delivered

        order1.next();       // Cannot continue


        // -------- Cancelled order --------
        System.out.println("\n=== ORDER 2 ===");

        Order order2 = new Order();

        order2.display();    // Placed

        order2.next();
        order2.display();    // Confirmed

        order2.cancel();
        order2.display();    // Cancelled

        order2.next();       // Cannot continue
        order2.cancel();     // Already cancelled
    }
}