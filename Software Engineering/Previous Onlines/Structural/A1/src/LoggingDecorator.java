public class LoggingDecorator extends BaseDecorator{

    LoggingDecorator(Notification notification) {
        super(notification);
    }

    @Override
    public void send(String message) {
        System.out.println("Logging Notification Attempt");
        super.send(message);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Logging";
    }
}
