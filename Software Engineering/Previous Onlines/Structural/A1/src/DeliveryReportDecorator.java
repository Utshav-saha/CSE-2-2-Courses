public class DeliveryReportDecorator extends BaseDecorator{

    DeliveryReportDecorator(Notification notification) {
        super(notification);
    }

    @Override
    public void send(String message) {
        System.out.println("Generating Delivery Report");
        super.send(message);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Retry";
    }
}
