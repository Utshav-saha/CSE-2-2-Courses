import java.util.ArrayList;
import java.util.List;

public class Building implements SmartComponent{

    private String name;
    private List<Room> rooms;

    public Building(String name){
        this.name = name;
        rooms = new ArrayList<Room>();
    }

    public void addRoom(Room room){
        rooms.add(room);
    }

    public void removeRoom(Room room){
        rooms.remove(room);
    }

    @Override
    public void monitor() {
        for(Room r : rooms){
            r.monitor();
        }
    }
}
