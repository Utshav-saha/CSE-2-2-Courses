// Interface expected by the client
interface Target {
    void request();
}


// Existing incompatible class
class Adaptee {

    public void specificRequest() {
        System.out.println(
                "Adaptee's original operation"
        );
    }
}


// Adapter
class Adapter implements Target {

    private final Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void request() {
        adaptee.specificRequest();
    }
}


// Client
public class adapter_template {
    public static void main(String[] args) {

        Adaptee oldObject =
                new Adaptee();

        Target target =
                new Adapter(oldObject);

        target.request();
    }
}