interface Channel {
    void send(String message);
}

class EmailChannel implements Channel {

    @Override
    public void send(String message) {
        System.out.println(
                "Sending email: " + message);
    }
}

class SMSChannel implements Channel {

    @Override
    public void send(String message) {
        System.out.println(
                "Sending SMS: " + message);
    }
}

abstract class Notification {

    protected final Channel channel;

    public Notification(Channel channel) {
        this.channel = channel;
    }

    public abstract void notifyUser();
}

class EmergencyNotification
        extends Notification {

    public EmergencyNotification(
            Channel channel) {

        super(channel);
    }

    @Override
    public void notifyUser() {
        channel.send("Emergency occurred");
    }
}

class PaymentNotification
        extends Notification {

    public PaymentNotification(
            Channel channel) {

        super(channel);
    }

    @Override
    public void notifyUser() {
        channel.send("Payment failed");
    }
}

public class bridge_template {
    public static void main(String[] args) {

        Notification n1 = new EmergencyNotification(
                new EmailChannel());

        Notification n2 = new EmergencyNotification(
                new SMSChannel());

        Notification n3 = new PaymentNotification(
                new EmailChannel());
    }
}