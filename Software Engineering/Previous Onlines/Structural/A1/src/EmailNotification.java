public class EmailNotification implements Notification{

    @Override
    public void send(String message) {
        System.out.println("Sending Email Notification: " + message);
    }

    @Override
    public String getDescription() {
        return "Email Notification";
    }
}
