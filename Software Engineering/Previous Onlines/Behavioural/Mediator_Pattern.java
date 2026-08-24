interface Mediator {

    void notify(Component sender, String event);
}

abstract class Component {

    protected Mediator mediator;

    Component(Mediator mediator) {
        this.mediator = mediator;
    }

    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }
}

class ComponentA extends Component {

    ComponentA(Mediator mediator) {
        super(mediator);
    }

    public void actionA() {

        System.out.println("Component A performs action");

        mediator.notify(this, "A");
    }

    public void reactA() {
        System.out.println("Component A reacts");
    }
}

class ComponentB extends Component {

    ComponentB(Mediator mediator) {
        super(mediator);
    }

    public void actionB() {

        System.out.println("Component B performs action");

        mediator.notify(this, "B");
    }

    public void reactB() {
        System.out.println("Component B reacts");
    }
}

class ConcreteMediator implements Mediator {

    private ComponentA componentA;
    private ComponentB componentB;

    public ConcreteMediator(
            ComponentA componentA,
            ComponentB componentB) {

        this.componentA = componentA;
        this.componentB = componentB;
    }

    @Override
    public void notify(Component sender, String event) {

        if (event.equals("A")) {

            componentB.reactB();

        } else if (event.equals("B")) {

            componentA.reactA();
        }
    }
}

public class Mediator_Pattern {
    public static void main(String[] args) {

        ComponentA a = new ComponentA(null);
        ComponentB b = new ComponentB(null);

        Mediator mediator =
                new ConcreteMediator(a, b);

        a.setMediator(mediator);
        b.setMediator(mediator);

        a.actionA();

        b.actionB();
    }
}