public class Setup {
    private String name;
    private String Monitor;
    private String Keyboard;
    private String Mouse;

    @Override
    public String toString() {
        return "Setup{" +
                "name='" + name + '\'' +
                ", Monitor='" + Monitor + '\'' +
                ", Keyboard='" + Keyboard + '\'' +
                ", Mouse='" + Mouse + '\'' +
                '}';
    }

    public Setup(String name, String monitor, String keyboard, String mouse) {
        this.name = name;
        Monitor = monitor;
        Keyboard = keyboard;
        Mouse = mouse;
    }
}
