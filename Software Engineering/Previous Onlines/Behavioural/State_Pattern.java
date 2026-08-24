abstract class State {

    protected Context context;

    State(Context context) {
        this.context = context;
    }

    public abstract void action();
    public abstract void next();
}

class StateA extends State {

    StateA(Context context) {
        super(context);
    }

    @Override
    public void action() {
        System.out.println("Behavior in State A");
    }

    @Override
    public void next() {
        context.setState(new StateB(context));
    }
}

class StateB extends State {

    StateB(Context context) {
        super(context);
    }

    @Override
    public void action() {
        System.out.println("Behavior in State B");
    }

    @Override
    public void next() {
        context.setState(new StateC(context));
    }
}

class StateC extends State {

    StateC(Context context) {
        super(context);
    }

    @Override
    public void action() {
        System.out.println("Behavior in State C");
    }

    @Override
    public void next() {
        System.out.println("No next state");
    }
}

class Context {

    private State state;

    Context() {
        state = new StateA(this);
    }

    public void setState(State state) {
        this.state = state;
    }

    public void action() {
        state.action();
    }

    public void next() {
        state.next();
    }
}

public class State_Pattern {
    public static void main(String[] args) {

        Context context = new Context();

        context.action();

        context.next();
        context.action();

        context.next();
        context.action();
    }
}