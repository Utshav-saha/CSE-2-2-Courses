interface Airplane {
    void requestTakeOff();
    void requestLanding();
    void notify(String message);

}

interface AirTrafficControlTower {
    void requestTakeoff(Airplane airplane);
    void requestLanding(Airplane airplane);
}

class controlTower implements AirTrafficControlTower {
    @Override
    public void requestTakeoff(Airplane airplane) {
        System.out.println("Control Tower: You can takeoff now");
    }

    @Override
    public void requestLanding(Airplane airplane) {
        System.out.println("Control Tower: You can land now");
    }
}


class Boeing implements Airplane {

    private AirTrafficControlTower mediator;
    Boeing(AirTrafficControlTower mediator) {
        this.mediator = mediator;
    }
    @Override
    public void requestTakeOff() {
        mediator.requestTakeoff(this);
    }

    @Override
    public void requestLanding() {
        mediator.requestLanding(this);
    }

    @Override
    public void notify(String message) {
        System.out.println("This is Boeing: " + message);
    }
}
public class Main {
    public static void main(String[] args) {

        AirTrafficControlTower controlTower = new controlTower();

        Airplane airplane1 = new Boeing(controlTower);
        Airplane airplane2 = new Boeing(controlTower);

        airplane1.requestTakeOff();
        airplane2.requestLanding();
    }
}