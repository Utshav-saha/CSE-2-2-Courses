abstract class State {
    protected Order order;

    State(Order order) {
        this.order = order;
    }

    public abstract void next();

    public void cancel() {
        order.setState(new Cancelled(order));
    }

    public abstract void display();
}

class Received extends State {

    Received(Order order) {
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Preparing(order));
    }

    @Override
    public void display() {
        System.out.println("State: Received");
    }
}

class Preparing extends State {

    Preparing(Order order) {
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Ready(order));
    }

    @Override
    public void display() {
        System.out.println("State: Preparing");
    }
}

class Ready extends State {

    Ready(Order order) {
        super(order);
    }

    @Override
    public void next() {
        order.setState(new Completed(order));
    }

    @Override
    public void cancel() {
        System.out.println("Cannot cancel after order becomes Ready");
    }

    @Override
    public void display() {
        System.out.println("State: Ready");
    }
}

class Completed extends State {

    Completed(Order order) {
        super(order);
    }

    @Override
    public void next() {
        System.out.println("Order already completed");
    }

    @Override
    public void cancel() {
        System.out.println("Completed order cannot be cancelled");
    }

    @Override
    public void display() {
        System.out.println("State: Completed");
    }
}

class Cancelled extends State {

    Cancelled(Order order) {
        super(order);
    }

    @Override
    public void next() {
        System.out.println("Cancelled order cannot continue");
    }

    @Override
    public void cancel() {
        System.out.println("Order already cancelled");
    }

    @Override
    public void display() {
        System.out.println("State: Cancelled");
    }
}

abstract class Order {

    private State state;

    Order() {
        state = new Received(this);
    }

    public void setState(State state) {
        this.state = state;
    }

    public void next() {
        state.next();
    }

    public void cancel() {
        state.cancel();
    }

    public void display() {
        state.display();
    }

    // Template Method
    public final void processOrder() {

        validateOrder();
        calculatePrice();

        next();             // Received -> Preparing

        prepareFood();      // customized by subclass

        next();             // Preparing -> Ready

        packageOrder();

        next();             // Ready -> Completed

        completeOrder();
    }

    public void validateOrder() {
        System.out.println("Order validated");
    }

    public void calculatePrice() {
        System.out.println("Price calculated");
    }

    protected abstract void prepareFood();

    public void packageOrder() {
        System.out.println("Order packaged");
    }

    public void completeOrder() {
        System.out.println("Order completed");
    }
}

class RegularOrder extends Order {

    @Override
    protected void prepareFood() {
        System.out.println("Food prepared normally");
    }
}

class ExpressOrder extends Order {

    @Override
    protected void prepareFood() {
        System.out.println("Food prepared with priority");
    }
}

public class Main {
    public static void main(String[] args) {

        System.out.println("=== NORMAL ORDER ===");

        Order order1 = new RegularOrder();

        order1.display();          // Received
        order1.processOrder();
        order1.display();          // Completed

        order1.cancel();           // invalid


        System.out.println("\n=== CANCELLED EXPRESS ORDER ===");

        Order order2 = new ExpressOrder();

        order2.display();          // Received

        order2.next();             // Preparing
        order2.display();

        order2.cancel();           // allowed
        order2.display();          // Cancelled

        order2.next();             // cannot continue
    }
}