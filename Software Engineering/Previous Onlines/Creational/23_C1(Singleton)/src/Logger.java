public class Logger {

    private static Logger instance;
    private int value;

    private Logger(int value) {
        this.value = value;
    }

    public static Logger getInstance(int value) {
        if(instance == null){
            instance = new Logger(value);
        }
        return instance;
    }
    public int getValue() {
        return value;
    }
}
