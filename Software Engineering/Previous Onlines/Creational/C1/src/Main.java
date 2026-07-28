//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Director d = new Director();
        CycleBuilder b1 = new CycleBuilder();
        CycleBuilder b2 = new CycleBuilder();

        d.constructCommuter(b1);
        d.constructMountain(b2);

        Bicycle cycle1 = b1.getCycle();
        Bicycle cycle2 = b2.getCycle();

        System.out.println(cycle1);
        System.out.println(cycle2);
    }
}