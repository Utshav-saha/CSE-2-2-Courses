//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        SmartDevice sensor =  new MotionSensor( new Zigbee());
        SmartDevice sensor2 =  new Camera( new Wifi());
        SmartDevice sensor3 =  new MotionSensor( new Bluetooth());

        Room room = new Room("Room 101");
        room.addDevice(sensor);
        room.addDevice(sensor2);

        Room room2 = new Room("Room 102");
        room2.addDevice(sensor3);
        room2.addDevice(sensor);

        Building b1 = new Building("B1");
        b1.addRoom(room);
        b1.addRoom(room2);

        b1.monitor();


    }
}