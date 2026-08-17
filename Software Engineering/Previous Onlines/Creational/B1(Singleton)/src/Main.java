//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Logger l1 = Logger.getInstance("Logger 1");
        Logger l2 = Logger.getInstance("Logger 2");

        System.out.println(l1.value);
        System.out.println(l2.value);
    }
}