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



