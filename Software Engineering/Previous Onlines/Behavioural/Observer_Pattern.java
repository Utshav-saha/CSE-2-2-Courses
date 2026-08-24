import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update(String data);
}

class ConcreteObserverA implements Observer {

    @Override
    public void update(String data) {
        System.out.println("Observer A received: " + data);
    }
}

class ConcreteObserverB implements Observer {

    @Override
    public void update(String data) {
        System.out.println("Observer B received: " + data);
    }
}

class Subject {

    private List<Observer> observers = new ArrayList<>();

    public void subscribe(Observer observer) {
        observers.add(observer);
    }

    public void unsubscribe(Observer observer) {
        observers.remove(observer);
    }

    public void notifyObservers(String data) {
        for (Observer observer : observers) {
            observer.update(data);
        }
    }

    public void doSomething(String data) {

        // subject changes something

        notifyObservers(data);
    }
}

public class Observer_Pattern {
    public static void main(String[] args) {

        Subject subject = new Subject();

        Observer o1 = new ConcreteObserverA();
        Observer o2 = new ConcreteObserverB();

        subject.subscribe(o1);
        subject.subscribe(o2);

        subject.doSomething("New Data");

        subject.unsubscribe(o1);

        subject.doSomething("Another Data");
    }
}