public class EncryptionDecorator extends BaseDecorator{

    EncryptionDecorator(Notification notification) {
        super(notification);
    }

    @Override
    public void send(String message) {
        System.out.println("Encrypting Message");
        super.send(message);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Encryption";
    }
}
