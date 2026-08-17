import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.

        ThemeFactory factory;
        Scanner scanner = new Scanner(System.in);
        String theme = scanner.nextLine();

        if(theme.equals("light")){
            factory = new LightTheme();
        }
        else factory = new DarkTheme();

        Application app = new Application(factory);
        app.render();
    }
}