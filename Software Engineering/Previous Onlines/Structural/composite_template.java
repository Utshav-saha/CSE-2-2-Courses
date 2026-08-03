import java.util.ArrayList;
import java.util.List;


// Common component
interface Component {
    void operation();
    double getValue();
    void display(String indent);
}


// Leaf
class Leaf implements Component {

    private final String name;
    private final double value;

    public Leaf(String name, double value) {
        this.name = name;
        this.value = value;
    }

    @Override
    public void operation() {
        System.out.println("Operating leaf: " + name);
    }

    @Override
    public double getValue() {
        return value;
    }

    @Override
    public void display(String indent) {
        System.out.println(
                indent + "Leaf: " + name
                        + ", value: " + value
        );
    }
}


// Composite
class Composite implements Component {

    private final String name;
    private final List<Component> children =
            new ArrayList<>();

    public Composite(String name) {
        this.name = name;
    }

    public void add(Component component) {
        children.add(component);
    }

    public void remove(Component component) {
        children.remove(component);
    }

    @Override
    public void operation() {
        System.out.println("Operating group: " + name);

        for (Component child : children) {
            child.operation();
        }
    }

    @Override
    public double getValue() {
        double total = 0;

        for (Component child : children) {
            total += child.getValue();
        }

        return total;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "Group: " + name);

        for (Component child : children) {
            child.display(indent + "  ");
        }
    }
}


// Client
public class composite_template {
    public static void main(String[] args) {

        Component leaf1 =
                new Leaf("Leaf 1", 10);

        Component leaf2 =
                new Leaf("Leaf 2", 20);

        Composite group =
                new Composite("Group A");

        group.add(leaf1);
        group.add(leaf2);

        Composite root =
                new Composite("Root");

        root.add(group);
        root.add(new Leaf("Leaf 3", 30));

        root.display("");

        System.out.println(
                "Total: " + root.getValue()
        );

        root.operation();
    }
}