interface Strategy {

    void execute(String data);
}

class ConcreteStrategyA implements Strategy {

    @Override
    public void execute(String data) {
        System.out.println("Strategy A: " + data);
    }
}

class ConcreteStrategyB implements Strategy {

    @Override
    public void execute(String data) {
        System.out.println("Strategy B: " + data);
    }
}

class Context {

    private Strategy strategy;

    Context(Strategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public void performTask(String data) {

        // other common work

        strategy.execute(data);
    }
}

public class Strategy_Pattern {
    public static void main(String[] args) {

        Context context =
                new Context(new ConcreteStrategyA());

        context.performTask("Hello");

        // dynamically switch algorithm
        context.setStrategy(new ConcreteStrategyB());

        context.performTask("Hello");
    }
}