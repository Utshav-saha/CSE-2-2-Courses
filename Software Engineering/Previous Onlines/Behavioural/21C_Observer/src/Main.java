import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

interface Observer{
    void update(String stock , double price);
}

class user implements Observer{

    private String name;
    user(String name){
        this.name = name;
    }
    @Override
    public void update(String stock, double price) {
        System.out.println(name + " is notified about " + stock + " with price " + price);
    }
}

class Stock{
    Map<String, List<Observer>> observers = new HashMap<>();

    Stock(){
        for(int i=1; i<=10; i++){
            observers.put("Stock " + i, new ArrayList<Observer>());
        }
    }

    public void addObserver(String stock, Observer observer){
        List<Observer> users = observers.get(stock);
        if(!users.contains(observer)){
            users.add(observer);
        }
    }

    public void removeObserver(String stock, Observer observer){
        List<Observer> users = observers.get(stock);
        users.remove(observer);
    }

    public void notifyObservers(String stock, double price){
        List<Observer> users = observers.get(stock);
        for(Observer o : users){
            o.update(stock, price);
        }
    }
}


public class Main {
    public static void main(String[] args) {
        Stock stock = new Stock();
        user user1 = new user("User1");
        user user2 = new user("User2");
        user user3 = new user("User3");
        user user4 = new user("User4");

        stock.addObserver("Stock 1", user1);
        stock.addObserver("Stock 1", user2);
        stock.addObserver("Stock 1", user3);
        stock.addObserver("Stock 1", user4);

        stock.addObserver("Stock 2", user2);
        stock.addObserver("Stock 3", user3);
        stock.addObserver("Stock 4", user4);

        stock.notifyObservers("Stock 1", 120.75);
        stock.removeObserver("Stock 2", user2);
        stock.notifyObservers("Stock 2", 110.75);
        stock.notifyObservers("Stock 4", 1500.75);
    }
}