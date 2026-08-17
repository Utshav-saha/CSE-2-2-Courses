//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Director d = new Director();
        CommuterBuilder b1 = new CommuterBuilder();
        MountainBuilder b2 = new MountainBuilder();

        d.construct(b1);
        d.construct(b2);

        Bicycle cycle1 = b1.getCycle();
        Bicycle cycle2 = b2.getCycle();

        System.out.println(cycle1);
        System.out.println(cycle2);
    }
}