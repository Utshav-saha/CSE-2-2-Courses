import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Factory factory;
        Scanner scanner = new Scanner(System.in);
        String type = scanner.nextLine();

        switch (type) {
            case "truck":
                factory = new TruckFactory();
                break;
            case "ship":
                factory = new ShipFactory();
                break;
                default:
                    System.out.println("Invalid type");
                    return;
        }

        factory.render();
    }
}