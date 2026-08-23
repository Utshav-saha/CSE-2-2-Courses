import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Authority {

    Map<Categories, List<Observer>> citizens = new HashMap<>();


    public Authority() {
        for (Categories operation : Categories.values()) {
            this.citizens.put(operation, new ArrayList<>());
        }
    }

    public void subscribe(Categories eventType, Observer citizen) {

        List<Observer> users = citizens.get(eventType);
        if (!users.contains(citizen)) {
            users.add(citizen);
        }
    }

    public void unsubscribe(Categories eventType, Observer citizen) {

        List<Observer> users = citizens.get(eventType);
        users.remove(citizen);
    }

    public void notify(Alert alert) {

        Categories eventType = alert.getCategory();

        List<Observer> users = citizens.get(eventType);
        for (Observer listener : users) {
            listener.update(alert);
        }
    }

}
