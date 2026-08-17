public final class Logger {

    private static Logger instance;
    public String value;

    private Logger(String v) {
        value = v;
    }

    public static Logger getInstance(String v) {
        if (instance == null) {
            instance = new Logger(v);
        }
        return instance;
    }
}
