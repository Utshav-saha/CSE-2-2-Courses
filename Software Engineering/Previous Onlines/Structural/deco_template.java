// Common component
interface Component {
    void operation();
}


// Concrete component
class ConcreteComponent implements Component {

    @Override
    public void operation() {
        System.out.println("Basic operation");
    }
}


// Base decorator
abstract class BaseDecorator implements Component {

    protected final Component wrapped;

    public BaseDecorator(Component wrapped) {
        this.wrapped = wrapped;
    }

    @Override
    public void operation() {
        wrapped.operation();
    }
}


// Concrete decorator 1
class FeatureA extends BaseDecorator {

    public FeatureA(Component wrapped) {
        super(wrapped);
    }

    @Override
    public void operation() {
        System.out.println("Feature A before");
        super.operation();
        System.out.println("Feature A after");
    }
}


// Concrete decorator 2
class FeatureB extends BaseDecorator {

    public FeatureB(Component wrapped) {
        super(wrapped);
    }

    @Override
    public void operation() {
        System.out.println("Feature B");
        super.operation();
    }
}


// Client
public class deco_template{
    public static void main(String[] args) {

        Component object = new ConcreteComponent();

        object = new FeatureA(object);
        object = new FeatureB(object);

        object.operation();
    }
}