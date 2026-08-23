abstract class State{
    protected App app;
    protected int lowerDist=0;
    protected int upperDist=0;

    State(App app){
        this.app = app;
    }

    public void setLowerDist(int lowerDist){
        this.lowerDist = lowerDist;
    }
    public void setUpperDist(int upperDist){
        this.upperDist = upperDist;
    }

    public void travelCheck(int km) {

        if(lowerDist<= km && km <= upperDist){
            System.out.println("STABLE");
        }
        else{
            System.out.println("UNSTABLE");
            System.out.println("ALERT: Bring patient back into coverage.");

        }

    }

    public void setMood(String mood) {
        System.out.println("Mood Control Unavailable");
    }

    public abstract void promote();
    public abstract void demote();

}

class Common extends State{

    Common(App app){
        super(app);
        super.setLowerDist(0);
        super.setUpperDist(10);
    }

    @Override
    public void promote() {
        super.app.setState(new Plus(app));
    }

    @Override
    public void demote() {
        super.app.setState(new Common(app));
    }
}

class Plus extends State{

    Plus(App app){
        super(app);
        super.setLowerDist(0);
        super.setUpperDist(50);
    }

    @Override
    public void promote() {
        super.app.setState(new Lux(app));
    }

    @Override
    public void demote() {
        super.app.setState(new Common(app));
    }
}

class Lux extends State{

    Lux(App app){
        super(app);
        super.setLowerDist(0);
        super.setUpperDist(50);
    }

    @Override
    public void promote() {
        super.app.setState(new Lux(app));
    }

    @Override
    public void demote() {
        super.app.setState(new Plus(app));
    }

    @Override
    public void setMood(String mood) {
        System.out.println("Mood set to " + mood);
    }
}

class App{

    State state;
    App(){
        state = new Common(this);
    }


    public void setState(State state){
        this.state = state;
    }

    public void setMood(String mood){
       state.setMood(mood);
    }

    public void activateLux(int hours){
        State prev = state;
        state = new Lux(this);
        System.out.println("Lux activated for " + hours + " hours");

        try{
            Thread.sleep(2000);
            this.setState(prev);
            System.out.println("State changed to " + prev.getClass().getSimpleName());

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            System.out.println("The thread was interrupted!");
        }

    }

    public void travelCheck(int km){
        state.travelCheck(km);
    }

    public void promote(){
        state.promote();
    }

    public void demote(){
        state.demote();
    }

}
public class Main {
    public static void main(String[] args) throws InterruptedException {

        App app = new App();

        // Common: range 0-10
        System.out.println("--- Common ---");
        app.travelCheck(5);      // STABLE
        app.travelCheck(20);     // UNSTABLE
        app.travelCheck(0);      // back in coverage

        // Mood not available in Common
        app.setMood("happy");

        // Common -> Plus
        System.out.println("\n--- Promote to Plus ---");
        app.promote();

        app.travelCheck(40);     // STABLE in Plus
        app.travelCheck(60);     // UNSTABLE
        app.travelCheck(0);      // recovery

        // Plus -> Common
        System.out.println("\n--- Demote to Common ---");
        app.demote();
        app.travelCheck(20);     // UNSTABLE again

        // Common -> Plus again
        app.promote();

        // Temporary Lux
        System.out.println("\n--- Temporary Lux ---");

        Thread luxThread = new Thread(() -> app.activateLux(2));
        luxThread.start();

        // Give activateLux enough time to enter Lux
        Thread.sleep(100);

        app.setMood("calm");
        app.setMood("happy");

        app.travelCheck(40);     // STABLE under Lux

        // Wait until temporary Lux ends
        luxThread.join();

        // Should now be Plus again
        System.out.println("\n--- After Lux expires ---");
        app.travelCheck(40);     // STABLE because returned to Plus

        // Mood should no longer work
        app.setMood("exhausted");

        // Plus -> Lux permanently through promote()
        System.out.println("\n--- Promote Plus to Lux ---");
        app.promote();

        app.setMood("exhausted");

        // Lux -> Plus
        System.out.println("\n--- Demote Lux to Plus ---");
        app.demote();

        app.setMood("calm");     // unavailable
    }
}