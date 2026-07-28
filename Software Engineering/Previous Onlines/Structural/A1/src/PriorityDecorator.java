public class PriorityDecorator extends BaseDecorator{

    PriorityDecorator(Notification notification) {
        super(notification);
    }

    @Override
    public void send(String message) {
        System.out.println("Adding HIGH PRIORITY level");
        super.send(message);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Priority";
    }
}
