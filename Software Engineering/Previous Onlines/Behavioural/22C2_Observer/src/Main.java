import java.util.ArrayList;

interface Observer {
    void update(String stock, double price);
}

class TickerTape implements Observer {
    @Override
    public void update(String stock, double price) {
        System.out.println("Ticker: " + stock + " = " + price);
    }
}

class Graph implements Observer {
    @Override
    public void update(String stock, double price) {
        System.out.println("Graph plots: " + stock + " = " + price);
    }
}

class BuySellBot implements Observer {
    @Override
    public void update(String stock, double price) {
        System.out.println("Bot evaluates: " + stock + " at " + price);
    }
}

class StockData {

    private ArrayList<Observer> observers = new ArrayList<>();

    public void subscribe(Observer observer) {
        observers.add(observer);
    }

    public void unsubscribe(Observer observer) {
        observers.remove(observer);
    }

    public void updatePrice(String stock, double price) {

        System.out.println("\nPrice changed: " + stock + " = " + price);

        for (Observer observer : observers) {
            observer.update(stock, price);
        }
    }
}

public class Main {
    public static void main(String[] args) {

        StockData stockData = new StockData();

        Observer ticker = new TickerTape();
        Observer graph = new Graph();
        Observer bot = new BuySellBot();

        stockData.subscribe(ticker);
        stockData.subscribe(graph);
        stockData.subscribe(bot);

        stockData.updatePrice("AAPL", 210.5);

        // remove Graph at runtime
        stockData.unsubscribe(graph);

        stockData.updatePrice("AAPL", 215.0);

        // add Graph again
        stockData.subscribe(graph);

        stockData.updatePrice("TSLA", 330.0);
    }
}