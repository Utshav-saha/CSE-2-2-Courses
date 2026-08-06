//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        DisasterManagement system = new DisasterManagement();

        Citizen c1 = new Citizen("Utshav");
        Citizen c2 = new Citizen("Swayam");
        Citizen c3 = new Citizen("smaf");

        system.authority.subscribe(Categories.Earthquake, c1);
        system.authority.subscribe(Categories.Flood, c1);
        system.authority.subscribe(Categories.Fire, c1);

        system.authority.subscribe(Categories.Flood, c2);
        system.authority.subscribe(Categories.Earthquake, c2);

        system.authority.subscribe(Categories.Earthquake, c3);
        system.authority.subscribe(Categories.Flood, c3);
        system.authority.subscribe(Categories.Fire, c3);


        Alert a1 = new Alert(
                "Strong Earthquake",Categories.Earthquake, "Dhaka",
                8, "Move to an open area"
        );

        Alert a2 = new Alert("Building Fire",Categories.Fire, "Thakurgaon", 7,
                "Evacuate the building asap"
        );

        Alert a3 = new Alert("Flood",Categories.Flood, "Ctg", 6,
                "Get to higher ground"
        );

        Alert a4 = new Alert("New Fire",Categories.Fire, "Dhaka", 7,
                "Evacuate the building fast"
        );

        system.createAlert(a1);
        system.createAlert(a2);
        system.createAlert(a3);

        c1.showNotifications();
        c2.showNotifications();
        c3.showNotifications();

        system.authority.subscribe(Categories.Fire, c2);
        system.authority.unsubscribe(Categories.Fire, c3);

        system.createAlert(a4);

        c1.showNotifications();
        c2.showNotifications();
        c3.showNotifications();

    }
}