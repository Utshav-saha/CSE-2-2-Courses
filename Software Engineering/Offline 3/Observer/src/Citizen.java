import java.util.ArrayList;
import java.util.List;

public class Citizen implements Observer{

    private String name;
    private List<Alert> notifications;

    public Citizen(String name){
        this.name = name;
        notifications = new ArrayList<>();
    }

    @Override
    public void update(Alert alert) {
        System.out.println("Citizen " + name + " has been updated" );
        System.out.println(alert);
        System.out.println("\n");
        notifications.add(alert);
    }

    public void clearNotifications(){
        notifications.clear();
    }



    public void showNotifications(){
        System.out.println("Citizen " + name + " has notifications:\n");
        for(Alert alert : notifications){
            System.out.println(alert);
        }
    }
}
