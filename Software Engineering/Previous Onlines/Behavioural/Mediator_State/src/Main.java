import java.util.ArrayList;

interface Mediator{
    void notify(component plane, String message);
}

class ControlTower implements Mediator{

    private ArrayList<component> planes = new ArrayList<>();
    private boolean runwayFree = true;

    public void register(component plane){
        planes.add(plane);
    }
    @Override
    public void notify(component plane, String message) {
        if(message.equals("requestLanding")){
            requestLanding(plane);
        }
        else if(message.equals("requestTakeoff")){
            requestTakeoff(plane);
        }
        else if(message.equals("releaseRunway")){
            releaseRunway(plane);
        }
    }

    public void requestLanding(component plane) {
        if(runwayFree){
            runwayFree = false;
            System.out.println(plane.getName() + " is cleared for landing");
            plane.setState(new Landing(plane));
        }
        else{
            System.out.println(plane.getName() + " must wait");
        }
    }

    public void releaseRunway(component plane) {
        runwayFree = true;
        System.out.println(plane.getName() + " cleared the runway");
    }

    public void requestTakeoff(component plane) {
        if(runwayFree){
            runwayFree = false;
            System.out.println(plane.getName() + " is cleared for Takeoff");
            plane.setState(new TakingOff(plane));
        }
        else{
            System.out.println(plane.getName() + " must wait");
        }
    }
}



abstract class state{
    protected component plane;
    state(component plane){
        this.plane = plane;
    }
    public void requestLanding() {
        System.out.println("Landing request invalid in current state");
    }

    public void finishLanding() {
        System.out.println("Cannot finish landing in current state");
    }

    public void requestTakeoff() {
        System.out.println("Takeoff request invalid in current state");
    }

    public void finishTakeoff() {
        System.out.println("Cannot finish takeoff in current state");
    }

    public abstract void display();
}

class Waiting extends state{
    public Waiting(component plane){
        super(plane);
    }

    @Override
    public void requestLanding() {
        plane.getMediator().notify(plane,"requestLanding");
    }

    public void display() {
        System.out.println(plane.getName() + " is waiting");
    }
}

class Landing extends state{
    public Landing(component plane){
        super(plane);
    }

    @Override
    public void finishLanding() {
        plane.getMediator().notify(plane,"releaseRunway");
        plane.setState(new Grounded(plane));
    }
    public void display() {
        System.out.println(plane.getName() + " is Landed");
    }
}

class Grounded extends state{
    public Grounded(component plane){
        super(plane);
    }

    @Override
    public void requestTakeoff() {
        plane.getMediator().notify(plane,"requestTakeoff");
    }
    public void display() {
        System.out.println(plane.getName() + " is Grounded");
    }
}

class TakingOff extends state{
    public TakingOff(component plane){
        super(plane);
    }

    @Override
    public void finishTakeoff() {
        plane.getMediator().notify(plane,"releaseRunway");
        plane.setState(new Waiting(plane));
    }
    public void display() {
        System.out.println(plane.getName() + " is Taking Off");
    }
}

abstract class component{
    protected Mediator mediator;
    protected state state;
    String name;

    component(Mediator mediator, String name){
        this.mediator = mediator;
        this.name = name;
        state = new Waiting(this);
    }

    public String getName() {
        return name;
    }

    public void setState(state state) {
        this.state = state;
    }

    public Mediator getMediator() {
        return mediator;
    }

    public void requestLanding() {
        state.requestLanding();
    }

    public void finishLanding() {
        state.finishLanding();
    }

    public void requestTakeoff() {
        state.requestTakeoff();
    }
    public void finishTakeoff() {
        state.finishTakeoff();
    }
    public void display() {
        state.display();
    }

}

class PassengerPlane extends component{
    public PassengerPlane(Mediator mediator, String name){
        super(mediator, name);
    }
}

class CargoPlane extends component{
    public CargoPlane(Mediator mediator, String name){
        super(mediator, name);
    }
}

class EmergencyPlane extends component{
    public EmergencyPlane(Mediator mediator, String name){
        super(mediator, name);
    }
}

public class Main {
    public static void main(String[] args) {

        ControlTower tower = new ControlTower();

        component p1 =
                new PassengerPlane(tower,"Passenger-101");

        component p2 =
                new CargoPlane(tower,"Cargo-202");

        tower.register(p1);
        tower.register(p2);


        // Both planes initially waiting
        p1.display();
        p2.display();


        System.out.println("\n--- Landing Requests ---");

        // p1 gets runway
        p1.requestLanding();

        // runway currently occupied by p1
        p2.requestLanding();


        // p1 finishes landing
        p1.finishLanding();
        p1.display();                  // Grounded


        // runway is now free
        p2.requestLanding();
        p2.finishLanding();
        p2.display();                  // Grounded


        System.out.println("\n--- Invalid Operation ---");

        // grounded plane cannot request landing
        p1.requestLanding();


        System.out.println("\n--- Takeoff ---");

        p1.requestTakeoff();
        p1.display();                  // TakingOff

        p1.finishTakeoff();
        p1.display();                  // Waiting
    }
}