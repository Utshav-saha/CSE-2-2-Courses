import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Factory factory;
        Scanner scanner = new Scanner(System.in);
        String command = scanner.nextLine();
        switch (command) {
            case "pdf":
                factory = new pdfFactory();
                break;

            case "word":
                factory = new wordFactory();
                break;

            case "html":
                factory = new htmlFactory();
                break;

            default:
                System.out.println("Invalid command");
                return;
        }

        factory.render();

    }
}