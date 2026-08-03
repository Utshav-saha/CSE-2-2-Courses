// ============================================================
// BRIDGE IMPLEMENTOR
// Different communication channels
// ============================================================

interface NotificationChannel {

    void send(String receiver, String message);

    String getChannelName();
}


// Concrete Implementor
class EmailChannel implements NotificationChannel {

    @Override
    public void send(String receiver, String message) {
        System.out.println(
                "Sending Email to " + receiver + ": " + message
        );
    }

    @Override
    public String getChannelName() {
        return "Email";
    }
}


// Concrete Implementor
class SMSChannel implements NotificationChannel {

    @Override
    public void send(String receiver, String message) {
        System.out.println(
                "Sending SMS to " + receiver + ": " + message
        );
    }

    @Override
    public String getChannelName() {
        return "SMS";
    }
}


// Concrete Implementor
class PushChannel implements NotificationChannel {

    @Override
    public void send(String receiver, String message) {
        System.out.println(
                "Sending Push Notification to "
                        + receiver + ": " + message
        );
    }

    @Override
    public String getChannelName() {
        return "Push Notification";
    }
}


// ============================================================
// LEGACY WHATSAPP SERVICE
// This class cannot be modified.
// ============================================================

class OldWhatsAppAPI {

    public void deliverWhatsAppText(
            String phoneNumber,
            String text) {

        System.out.println(
                "Legacy WhatsApp API sending to "
                        + phoneNumber + ": " + text
        );
    }
}


// ============================================================
// ADAPTER
// Converts OldWhatsAppAPI into NotificationChannel
// ============================================================

class WhatsAppAdapter implements NotificationChannel {

    private final OldWhatsAppAPI oldWhatsAppAPI;

    public WhatsAppAdapter(
            OldWhatsAppAPI oldWhatsAppAPI) {

        this.oldWhatsAppAPI = oldWhatsAppAPI;
    }

    @Override
    public void send(String receiver, String message) {

        oldWhatsAppAPI.deliverWhatsAppText(
                receiver,
                message
        );
    }

    @Override
    public String getChannelName() {
        return "WhatsApp";
    }
}


// ============================================================
// COMMON ALERT INTERFACE
// Needed so both normal alerts and decorators are treated uniformly
// ============================================================

interface Alert {

    void send(String receiver);

    String getDescription();
}


// ============================================================
// BRIDGE ABSTRACTION
// Alert type contains a NotificationChannel
// ============================================================

abstract class BaseAlert implements Alert {

    protected final NotificationChannel channel;
    protected final String message;

    public BaseAlert(
            NotificationChannel channel,
            String message) {

        this.channel = channel;
        this.message = message;
    }

    protected abstract String getAlertType();

    @Override
    public void send(String receiver) {

        System.out.println(
                "Preparing " + getAlertType()
        );

        channel.send(receiver, message);
    }

    @Override
    public String getDescription() {

        return getAlertType()
                + " through "
                + channel.getChannelName();
    }
}


// Refined Abstraction
class EmergencyAlert extends BaseAlert {

    public EmergencyAlert(
            NotificationChannel channel,
            String message) {

        super(channel, message);
    }

    @Override
    protected String getAlertType() {
        return "Emergency Alert";
    }
}


// Refined Abstraction
class PaymentAlert extends BaseAlert {

    public PaymentAlert(
            NotificationChannel channel,
            String message) {

        super(channel, message);
    }

    @Override
    protected String getAlertType() {
        return "Payment Alert";
    }
}


// Refined Abstraction
class DeliveryAlert extends BaseAlert {

    public DeliveryAlert(
            NotificationChannel channel,
            String message) {

        super(channel, message);
    }

    @Override
    protected String getAlertType() {
        return "Delivery Alert";
    }
}


// ============================================================
// BASE DECORATOR
// ============================================================

abstract class AlertDecorator implements Alert {

    protected final Alert wrappedAlert;

    public AlertDecorator(Alert wrappedAlert) {
        this.wrappedAlert = wrappedAlert;
    }

    @Override
    public void send(String receiver) {
        wrappedAlert.send(receiver);
    }

    @Override
    public String getDescription() {
        return wrappedAlert.getDescription();
    }
}


// ============================================================
// CONCRETE DECORATORS
// ============================================================

class EncryptionDecorator extends AlertDecorator {

    public EncryptionDecorator(Alert wrappedAlert) {
        super(wrappedAlert);
    }

    @Override
    public void send(String receiver) {

        System.out.println(
                "Encrypting alert message"
        );

        super.send(receiver);
    }

    @Override
    public String getDescription() {

        return super.getDescription()
                + " + Encryption";
    }
}


class LoggingDecorator extends AlertDecorator {

    public LoggingDecorator(Alert wrappedAlert) {
        super(wrappedAlert);
    }

    @Override
    public void send(String receiver) {

        System.out.println(
                "Logging alert delivery attempt"
        );

        super.send(receiver);

        System.out.println(
                "Alert delivery recorded"
        );
    }

    @Override
    public String getDescription() {

        return super.getDescription()
                + " + Logging";
    }
}


// Additional decorator to show extensibility
class PriorityDecorator extends AlertDecorator {

    public PriorityDecorator(Alert wrappedAlert) {
        super(wrappedAlert);
    }

    @Override
    public void send(String receiver) {

        System.out.println(
                "Adding HIGH PRIORITY label"
        );

        super.send(receiver);
    }

    @Override
    public String getDescription() {

        return super.getDescription()
                + " + High Priority";
    }
}


// ============================================================
// CLIENT
// ============================================================

public class Main {

    private static void testAlert(
            String testName,
            Alert alert,
            String receiver) {

        System.out.println(
                "\n========================================"
        );

        System.out.println(testName);

        System.out.println(
                "========================================"
        );

        System.out.println(
                "Configuration: "
                        + alert.getDescription()
        );

        alert.send(receiver);
    }


    public static void main(String[] args) {

        // ====================================================
        // Test 1: Emergency Alert through Email
        // ====================================================

        NotificationChannel email =
                new EmailChannel();

        Alert emergencyEmail =
                new EmergencyAlert(
                        email,
                        "Fire detected in the building"
                );

        testAlert(
                "TEST 1: EMERGENCY ALERT THROUGH EMAIL",
                emergencyEmail,
                "admin@example.com"
        );


        // ====================================================
        // Test 2: Payment Alert through SMS
        // ====================================================

        NotificationChannel sms =
                new SMSChannel();

        Alert paymentSMS =
                new PaymentAlert(
                        sms,
                        "Your payment has failed"
                );

        testAlert(
                "TEST 2: PAYMENT ALERT THROUGH SMS",
                paymentSMS,
                "01700000000"
        );


        // ====================================================
        // Test 3: Delivery Alert through Push
        // ====================================================

        NotificationChannel push =
                new PushChannel();

        Alert deliveryPush =
                new DeliveryAlert(
                        push,
                        "Your order is on the way"
                );

        testAlert(
                "TEST 3: DELIVERY ALERT THROUGH PUSH",
                deliveryPush,
                "User-101"
        );


        // ====================================================
        // Test 4: Emergency Alert through legacy WhatsApp API
        // Adapter converts WhatsApp into NotificationChannel.
        // ====================================================

        OldWhatsAppAPI oldWhatsAppAPI =
                new OldWhatsAppAPI();

        NotificationChannel whatsApp =
                new WhatsAppAdapter(
                        oldWhatsAppAPI
                );

        Alert emergencyWhatsApp =
                new EmergencyAlert(
                        whatsApp,
                        "Unauthorized entry detected"
                );

        testAlert(
                "TEST 4: EMERGENCY ALERT THROUGH WHATSAPP ADAPTER",
                emergencyWhatsApp,
                "01800000000"
        );


        // ====================================================
        // Test 5:
        // Logging outside Encryption
        //
        // Execution:
        // Logging → Encryption → Emergency Alert
        // ====================================================

        Alert loggedEncryptedAlert =
                new LoggingDecorator(
                        new EncryptionDecorator(
                                new EmergencyAlert(
                                        new EmailChannel(),
                                        "Motion detected"
                                )
                        )
                );

        testAlert(
                "TEST 5: LOGGING OUTSIDE ENCRYPTION",
                loggedEncryptedAlert,
                "security@example.com"
        );


        // ====================================================
        // Test 6:
        // Encryption outside Logging
        //
        // Execution:
        // Encryption → Logging → Emergency Alert
        // ====================================================

        Alert encryptedLoggedAlert =
                new EncryptionDecorator(
                        new LoggingDecorator(
                                new EmergencyAlert(
                                        new EmailChannel(),
                                        "Motion detected"
                                )
                        )
                );

        testAlert(
                "TEST 6: ENCRYPTION OUTSIDE LOGGING",
                encryptedLoggedAlert,
                "security@example.com"
        );


        // ====================================================
        // Test 7:
        // Bridge + Adapter + multiple decorators
        // ====================================================

        Alert advancedWhatsAppAlert =
                new PriorityDecorator(
                        new LoggingDecorator(
                                new EncryptionDecorator(
                                        new DeliveryAlert(
                                                new WhatsAppAdapter(
                                                        new OldWhatsAppAPI()
                                                ),
                                                "Your package has arrived"
                                        )
                                )
                        )
                );

        testAlert(
                "TEST 7: WHATSAPP WITH ALL FEATURES",
                advancedWhatsAppAlert,
                "01900000000"
        );


        // ====================================================
        // Test 8:
        // Runtime configuration
        // ====================================================

        boolean encryptRequested = true;
        boolean loggingRequested = true;
        boolean priorityRequested = false;

        NotificationChannel selectedChannel =
                new PushChannel();

        Alert runtimeAlert =
                new PaymentAlert(
                        selectedChannel,
                        "Payment completed successfully"
                );

        if (encryptRequested) {
            runtimeAlert =
                    new EncryptionDecorator(runtimeAlert);
        }

        if (loggingRequested) {
            runtimeAlert =
                    new LoggingDecorator(runtimeAlert);
        }

        if (priorityRequested) {
            runtimeAlert =
                    new PriorityDecorator(runtimeAlert);
        }

        testAlert(
                "TEST 8: RUNTIME CONFIGURATION",
                runtimeAlert,
                "User-202"
        );
    }
}