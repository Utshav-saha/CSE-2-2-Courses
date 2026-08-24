interface pricing{
    int calculate(int distance);
}

class regular implements pricing{
    @Override
    public int calculate(int distance) {
        return distance * 20;
    }
}

class Peak implements pricing{
    @Override
    public int calculate(int distance) {
        return distance * 30;
    }
}
class Discount implements pricing{
    @Override
    public int calculate(int distance) {
        return distance * 15;
    }
}

abstract class state{
    protected Application app;
    public state(Application app){
        this.app = app;
    }

    public abstract void next();
    public void cancel(){
        app.setState(new Cancelled(app));
    }
    public abstract void display();
    public void changePricing(pricing pricing){
        app.setPricing(pricing);
    }
}

class Requested extends state{
    public Requested(Application app){
        super(app);
    }

    @Override
    public void next() {
        app.setState(new Accepted(app));
    }

    @Override
    public void display() {
        System.out.println("Current state: Requested");
    }
}

class Accepted extends state{
    public Accepted(Application app){
        super(app);
    }

    @Override
    public void next() {
        app.setState(new Ongoing(app));
    }

    @Override
    public void display() {
        System.out.println("Current state: Accepted");
    }
}

class Ongoing extends state{
    public Ongoing(Application app){
        super(app);
    }

    @Override
    public void next() {
        app.setState(new Completed(app));
    }

    @Override
    public void display() {
        System.out.println("Current state: Ongoing");
    }

    @Override
    public void cancel() {
        System.out.println("Ride ongoing , can't cancel");
    }
}

class Completed extends state{
    public Completed(Application app){
        super(app);
    }

    @Override
    public void next() {
        System.out.println("Ride Completed");
    }

    @Override
    public void display() {
        System.out.println("Current state: Completed");
    }

    @Override
    public void cancel() {
        System.out.println("Ride Completed , can't cancel");
    }

    @Override
    public void changePricing(pricing pricing) {
        System.out.println("Can't change pricing now");
    }
}

class Cancelled extends state{
    public Cancelled(Application app){
        super(app);
    }

    @Override
    public void next() {
        System.out.println("Ride cancelled");
    }

    @Override
    public void display() {
        System.out.println("Current state: Cancelled");
    }

    @Override
    public void cancel() {
        System.out.println("Ride already cancelled");
    }

    @Override
    public void changePricing(pricing pricing) {
        System.out.println("Can't change pricing now");
    }
}
class Application{
    private state state;
    private pricing method;

    public Application(){
        this.state = new Requested(this);
        this.method = new regular();
    }

    public void setState(state state){
        this.state = state;
    }

    public void setPricing(pricing method){
        this.method = method;
    }

    public void display(){
        state.display();
    }

    public void changePricing(pricing pricing){
        state.changePricing(pricing);
    }

    public void cancel(){
        state.cancel();
    }

    public void next(){
        state.next();
    }

    public int getPrice(int distance){
        return method.calculate(distance);
    }

}
public class Main {
    public static void main(String[] args) {

        System.out.println("=== RIDE 1 ===");

        Application ride1 = new Application();

        // Requested + Regular pricing
        ride1.display();
        System.out.println("Price: " + ride1.getPrice(10));
        // 10 * 20 = 200

        // Change to peak pricing
        ride1.changePricing(new Peak());
        System.out.println("Peak Price: " + ride1.getPrice(10));
        // 10 * 30 = 300

        // Requested -> Accepted
        ride1.next();
        ride1.display();

        // Change to discount pricing
        ride1.changePricing(new Discount());
        System.out.println("Discount Price: " + ride1.getPrice(10));
        // 10 * 15 = 150

        // Accepted -> Ongoing
        ride1.next();
        ride1.display();

        // Cannot cancel ongoing ride
        ride1.cancel();

        // Ongoing -> Completed
        ride1.next();
        ride1.display();

        // Cannot change pricing after completion
        ride1.changePricing(new Peak());

        // Cannot cancel completed ride
        ride1.cancel();


        System.out.println("\n=== RIDE 2 ===");

        Application ride2 = new Application();

        ride2.display();          // Requested

        ride2.next();             // Accepted
        ride2.display();

        ride2.cancel();           // Accepted -> Cancelled
        ride2.display();

        ride2.next();             // Cannot continue
        ride2.cancel();           // Already cancelled

        ride2.changePricing(new Peak()); // Cannot change pricing
    }
}