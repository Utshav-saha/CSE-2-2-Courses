// Mediator
interface SmartHomeHub {
    void notify(SmartDevice sender, String event);
}

// Component Base
abstract class SmartDevice {
    protected SmartHomeHub mediator;

    public SmartDevice(SmartHomeHub mediator) {
        this.mediator = mediator;
    }
}

// Concrete Components
class LightSensor extends SmartDevice {
    public LightSensor(SmartHomeHub mediator) {
        super(mediator);
    }

    public void detectBrightness() {
        System.out.println("Light Sensor: 'High Brightness' detected.");
        mediator.notify(this, "HIGH_BRIGHTNESS");
    }
}

class AutomaticBlinds extends SmartDevice {
    public AutomaticBlinds(SmartHomeHub mediator) {
        super(mediator);
    }

    public void close() {
        System.out.println("Automatic Blinds: Closing...");
        mediator.notify(this, "BLINDS_CLOSED");
    }
}

class AirConditioner extends SmartDevice {
    public AirConditioner(SmartHomeHub mediator) {
        super(mediator);
    }

    public void turnOn() {
        System.out.println("Air Conditioner: Turning ON to prevent stuffiness.");
    }
}

// Concrete Mediator
class CentralHub implements SmartHomeHub {
    private AutomaticBlinds blinds;
    private AirConditioner ac;

    public void setBlinds(AutomaticBlinds blinds) {
        this.blinds = blinds;
    }

    public void setAc(AirConditioner ac) {
        this.ac = ac;
    }

    @Override
    public void notify(SmartDevice sender, String event) {
        if (event.equals("HIGH_BRIGHTNESS")) {
            System.out.println("Central Hub: Instructing Blinds to close.");
            if (blinds != null) {
                blinds.close();
            }
        } else if (event.equals("BLINDS_CLOSED")) {
            System.out.println("Central Hub: Instructing AC to turn on.");
            if (ac != null) {
                ac.turnOn();
            }
        }
    }
}

// 5. Demonstration
public class Main {
    public static void main(String[] args) {
        CentralHub hub = new CentralHub();

        LightSensor sensor = new LightSensor(hub);
        AutomaticBlinds blinds = new AutomaticBlinds(hub);
        AirConditioner ac = new AirConditioner(hub);

        hub.setBlinds(blinds);
        hub.setAc(ac);

        sensor.detectBrightness();
    }
}