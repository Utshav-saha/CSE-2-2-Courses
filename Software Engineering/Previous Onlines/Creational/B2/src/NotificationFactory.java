public class NotificationFactory {

    public Notification getNotification(String type) {

        if(type == null) return null;

        else if(type.equals("sms")) {
            return new sms();
        }
        else if(type.equals("email")) {
            return new email();
        }
        else if(type.equals("push")) {
            return new pushNotification();
        }

        throw new IllegalArgumentException("Unknown Type");


    }
}
