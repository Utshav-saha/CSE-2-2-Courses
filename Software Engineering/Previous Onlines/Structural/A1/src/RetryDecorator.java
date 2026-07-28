public class RetryDecorator extends BaseDecorator{

    RetryDecorator(Notification notification) {
        super(notification);
    }

    @Override
    public void send(String message) {
        System.out.println("Retrying notification if necessary");
        super.send(message);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Retry";
    }

}
