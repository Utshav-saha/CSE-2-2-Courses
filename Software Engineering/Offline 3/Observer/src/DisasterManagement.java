import java.util.ArrayList;

public class DisasterManagement {
    public Authority authority;
    private Alert alert;
    private ArrayList<Citizen> citizens = new ArrayList<>();

    public DisasterManagement(){
        this.authority = new Authority();
    }

    public void register(Citizen citizen) {
        citizens.add(citizen);
    }

    public void subscribe(Categories category,Citizen citizen) {
        if(!citizens.contains(citizen)) {
            System.out.println("Citizen not in database");
            return;
        }
        authority.subscribe(category, citizen);
    }

    public void unsubscribe(Categories category,Citizen citizen) {
        if(!citizens.contains(citizen)) {
            System.out.println("Citizen not in database");
            return;
        }
        authority.unsubscribe(category, citizen);
    }


    public void createAlert(Alert alert){
        this.alert = alert;
        authority.notify(alert);
    }
}
