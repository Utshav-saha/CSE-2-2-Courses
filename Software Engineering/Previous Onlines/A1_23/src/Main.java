import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true){

            Theme theme;
            ThemeFactory factory = new LightFactory();
            String input = scanner.nextLine();
            if(input.equals("q")){
                break;
            }

            else if(input.equals("light")){
                factory = new LightFactory();
            }
            else if(input.equals("dark")){
                factory = new DarkFactory();
            }

            else{
                System.out.println("Invalid input");
                continue;
            }

            theme = new Theme(factory);
            theme.print();

        }
    }
}