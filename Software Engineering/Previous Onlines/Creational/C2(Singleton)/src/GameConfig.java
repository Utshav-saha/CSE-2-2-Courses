public class GameConfig {

    private String gameName;
    private static GameConfig instance;

    private GameConfig(String gameName) {
        this.gameName = gameName;
    }

    public static GameConfig getInstance(String g) {

        if (instance == null) {
            instance = new GameConfig(g);
        }
        return instance;
    }

    public String getGameName() {
        return gameName;
    }
}
