//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        GameConfig g1 = GameConfig.getInstance("Game1");
        GameConfig g2 = GameConfig.getInstance("Game2");

        System.out.println(g1.getGameName());
        System.out.println(g2.getGameName());
    }
}