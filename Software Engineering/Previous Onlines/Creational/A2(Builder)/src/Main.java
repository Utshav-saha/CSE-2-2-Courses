//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Director d = new Director();
        PackageBuilder b1 = new PackageBuilder();
        PackageBuilder b2 = new PackageBuilder();

        d.RelaxationPackage(b1);
        Package p1 = b1.getPackage();

        d.AdventurePackage(b2);
        Package p2 = b2.getPackage();

        System.out.println(p1);
        System.out.println(p2);
    }
}