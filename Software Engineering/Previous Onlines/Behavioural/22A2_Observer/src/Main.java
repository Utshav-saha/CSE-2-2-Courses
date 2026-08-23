import java.util.ArrayList;

interface Observer {
    void update(String message);
}
class Scouts implements Observer {
    @Override
    public void update(String message) {
        System.out.println("Scouts received " + message);
        System.out.println("Dispatch Riders ! ");
    }
}

class Commander implements Observer {
    @Override
    public void update(String message) {
        System.out.println("Commander received " + message);
        System.out.println("Get ready Soldiers !");
    }
}

class SupplyTeam implements Observer {
    @Override
    public void update(String message) {
        System.out.println("Suuply Team received " + message);
        System.out.println("Update inventory !");
    }
}

class RavenBoard{

    ArrayList<Observer> observers = new ArrayList<>();

    void subscribe(Observer observer) {
        observers.add(observer);
    }

    void unsubscribe(Observer observer) {
        observers.remove(observer);
    }

    void update(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }

}
public class Main {
    public static void main(String[] args) {

        Observer observer1 = new Commander();
        Observer observer2 = new SupplyTeam();
        Observer observer3 = new Scouts();

        RavenBoard ravenBoard = new RavenBoard();
        ravenBoard.subscribe(observer1);
        ravenBoard.subscribe(observer2);

        ravenBoard.update("Enemy spotted near the river");

        ravenBoard.unsubscribe(observer2);
        ravenBoard.subscribe(observer3);
        ravenBoard.update("Winter supplies running low");
    }
}