abstract class AbstractProcess {

    // TEMPLATE METHOD
    public final void run() {

        step1();
        step2();
        customStep();
        step4();
    }

    public void step1() {
        System.out.println("Common step 1");
    }

    public void step2() {
        System.out.println("Common step 2");
    }

    protected abstract void customStep();

    public void step4() {
        System.out.println("Common step 4");
    }
}

class ConcreteProcessA extends AbstractProcess {

    @Override
    protected void customStep() {
        System.out.println("Process A custom step");
    }
}

class ConcreteProcessB extends AbstractProcess {

    @Override
    protected void customStep() {
        System.out.println("Process B custom step");
    }
}

public class Template_Pattern {
    public static void main(String[] args) {

        AbstractProcess p1 =
                new ConcreteProcessA();

        AbstractProcess p2 =
                new ConcreteProcessB();

        p1.run();

        System.out.println();

        p2.run();
    }
}