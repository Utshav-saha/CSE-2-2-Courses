import java.util.ArrayList;
import java.util.List;

interface SmartDevice {

     void activate();
     void deactivate();
     double getPowerUsage();
     String getStatus();
}

class SmartLight implements SmartDevice{

        boolean on = false;

        public void activate() {

            this.on = true;

        }

        public void deactivate() {

            on = false;

        }

        public double getPowerUsage() {
            double p = on ? 10.0 : 0.0;

            return p;
        }

        public String getStatus() {
            String s = "Light: " + (on ? "ON" : "OFF");

            return s;
        }
    }

class SmartThermostat implements SmartDevice{

    boolean on = false;

    public void activate() {

        on = true;

    }

    public void deactivate() {

        on = false;

    }

    public double getPowerUsage() {
        double p = on ? 150.0 : 0.0;
        return p;

    }

    public String getStatus() {
        String s = "Thermostat: " + (on ? "ON" : "OFF");

        return s;
    }
}


class SmartSpeaker implements SmartDevice{

    boolean on = false;
    // Same flags AGAIN — copy-pasted a third time

    public void activate() {

        on = true;

    }

    public void deactivate() {

        on = false;

    }

    public double getPowerUsage() {
        double p = on ? 5.0 : 0.0;

        return p;
    }

    public String getStatus() {
        String s = "Speaker: " + (on ? "Playing" : "Idle");

        return s;
    }
}


class Room implements SmartDevice{
    String name;
    List<SmartDevice> devices = new ArrayList<>();

    Room(String name) { this.name = name; }
    public void addDevice(SmartDevice d) { devices.add(d); }

    public void activate() {
        for (SmartDevice d : devices) d.activate();
    }

    public void deactivate() {
        for (SmartDevice d : devices) d.deactivate();
    }

    @Override
    public double getPowerUsage() {
        double total = 0;
        for (SmartDevice d : devices) total += d.getPowerUsage();
        return total;
    }

    public String getStatus() {

        String s = name;
        s+= "\n";
        for (SmartDevice d : devices){
            s += d.getStatus();
            s+= "\n";
        }
        return s;
    }
}


class Home implements SmartDevice{

    String name;
    List<SmartDevice> rooms = new ArrayList<>();

    Home(String name) {
        this.name = name;
    }

    @Override
    public void activate() {
        for (SmartDevice room : rooms) {
            room.activate();
        }
    }

    @Override
    public void deactivate() {
        for (SmartDevice room : rooms) {
            room.deactivate();
        }
    }

    @Override
    public double getPowerUsage() {
        double total = 0;
        for (SmartDevice room : rooms) {
            total += room.getPowerUsage();
        }
        return total;
    }

    @Override
    public String getStatus() {
        String s = name;
        s+= "\n";
        for (SmartDevice room : rooms) {
            s += room.getStatus();
            s+= "\n";
        }
        return s;
    }

    public void addRoom(Room room) {
        rooms.add(room);
    }
}

abstract class deviceDecorator implements SmartDevice{
    private SmartDevice wrappee;

    public deviceDecorator(SmartDevice wrappee) {
        this.wrappee = wrappee;
    }

    @Override
    public void activate() {
        wrappee.activate();
    }

    @Override
    public void deactivate() {
        wrappee.deactivate();
    }

    @Override
    public double getPowerUsage() {
        return wrappee.getPowerUsage();
    }

    @Override
    public String getStatus() {
       return wrappee.getStatus();
    }
}

class AccessRestricted extends deviceDecorator{

    private int pin;
    boolean locked = true;
    public AccessRestricted(SmartDevice wrappee, int pin) {
        super(wrappee);
        this.pin = pin;
    }

    @Override
    public void activate() {
        if(locked) return;
        else super.activate();
    }

    @Override
    public void deactivate() {
        if(locked) return;
        else super.deactivate();
    }

    @Override
    public String getStatus() {
        String s = super.getStatus();
        if(locked) s += " [LOCKED]";

        return s;
    }

    public void unlock(int key){
        if(!locked) return;
        else if(key == pin){
            locked = false;
            System.out.println("    >> Unlock SUCCESS");
        }

        else{
            System.out.println("    >> Unlock FAILED");
        }
    }
}

class TimerControlled extends deviceDecorator{

    private boolean timerRunning = false;
    private int timerSeconds = 0;
    public TimerControlled(SmartDevice wrappee, int timerSeconds) {
        super(wrappee);
        this.timerSeconds = timerSeconds;
    }


    @Override
    public void activate() {
        timerRunning = true;
        super.activate();
    }

    @Override
    public void deactivate() {
        super.deactivate();
        timerRunning = false;
    }

    @Override
    public String getStatus() {
        String s = super.getStatus();
        if (timerRunning) s += " (auto-off in " + timerSeconds + "s)";

        return s;
    }

    public void simulateTimerExpiry(){
        if(timerRunning){
            System.out.println("    >> Timer expired — auto-deactivating.");
            this.deactivate();
        }
    }
}

class PowerThrottled extends deviceDecorator{
    private boolean powerThrottled = false;
    private double powerCap = 0;

    public PowerThrottled(SmartDevice wrappee, int powerCap) {
        super(wrappee);
        this.powerCap = powerCap;
        powerThrottled = true;
    }

    @Override
    public double getPowerUsage() {
        double p = super.getPowerUsage();
        if (powerThrottled && p > powerCap) p = powerCap;
        return p;
    }

    @Override
    public String getStatus() {
        String s = super.getStatus();
        if (powerThrottled && super.getPowerUsage()> powerCap) s += " [throttled to " + powerCap + "W]";
        return s;
    }
}

abstract class modeDecorator extends Room{
    private Room wrappee;

    public modeDecorator(Room wrappee) {
        super(wrappee.name);
        this.wrappee = wrappee;
    }
    @Override
    public void activate() {
        wrappee.activate();
    }

    @Override
    public void deactivate() {
        wrappee.deactivate();
    }

    @Override
    public double getPowerUsage() {
        return wrappee.getPowerUsage();
    }

    @Override
    public String getStatus() {
        return wrappee.getStatus();
    }
}



