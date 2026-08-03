import java.util.ArrayList;
import java.util.List;

public class Room implements SmartComponent{
    private String name;
    private List<SmartDevice> devices;

    public Room(String name){
        this.name = name;
        devices = new ArrayList<SmartDevice>();
    }

    public void addDevice(SmartDevice device){
        devices.add(device);
    }

    public void removeDevice(SmartDevice device){
        devices.remove(device);
    }

    @Override
    public void monitor() {
        for(SmartDevice d : devices){
            d.monitor();
        }
    }
}
