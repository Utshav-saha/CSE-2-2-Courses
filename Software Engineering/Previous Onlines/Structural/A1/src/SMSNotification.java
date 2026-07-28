public class SMSNotification implements Notification{

    @Override
    public void send(String message) {
        System.out.println("Sending SMS Notification: " + message);
    }

    @Override
    public String getDescription() {
        return "SMS Notification";
    }
}
