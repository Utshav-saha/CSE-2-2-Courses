//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        NotificationFactory nf = new NotificationFactory();

        Notification n1 = nf.getNotification("sms");
        Notification n2 = nf.getNotification("email");
        Notification n3 = nf.getNotification("push");

        n1.notifyUser();
        n2.notifyUser();
        n3.notifyUser();
    }
}