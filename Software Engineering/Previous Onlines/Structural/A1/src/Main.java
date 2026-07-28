public class Main {

    private static void testNotification(
            String testName,
            Notification notification,
            String message) {

        System.out.println("\n========================================");
        System.out.println(testName);
        System.out.println("========================================");

        System.out.println("Configuration: "
                + notification.getDescription());

        System.out.println("Sending notification:");
        notification.send(message);
    }

    public static void main(String[] args) {

        /*
         * Test 1:
         * Basic Email Notification
         */
        Notification email = new EmailNotification();

        testNotification(
                "Test 1: Basic Email",
                email,
                "Motion detected near the front door"
        );


        /*
         * Test 2:
         * Basic SMS Notification
         */
        Notification sms = new SMSNotification();

        testNotification(
                "Test 2: Basic SMS",
                sms,
                "Smoke detected in the kitchen"
        );


        /*
         * Test 3:
         * Basic Push Notification
         */
        Notification push = new PushNotification();

        testNotification(
                "Test 3: Basic Push Notification",
                push,
                "Window opened unexpectedly"
        );


        /*
         * Test 4:
         * Email with one feature
         */
        Notification encryptedEmail =
                new EncryptionDecorator(
                        new EmailNotification()
                );

        testNotification(
                "Test 4: Encrypted Email",
                encryptedEmail,
                "Unknown person detected"
        );


        /*
         * Test 5:
         * SMS with multiple features
         */
        Notification secureSMS =
                new LoggingDecorator(
                        new PriorityDecorator(
                                new EncryptionDecorator(
                                        new SMSNotification()
                                )
                        )
                );

        testNotification(
                "Test 5: Encrypted, Priority and Logged SMS",
                secureSMS,
                "Possible security breach"
        );


        /*
         * Test 6:
         * Push notification with all available features
         */
        Notification advancedPush =
                new DeliveryReportDecorator(
                        new RetryDecorator(
                                new LoggingDecorator(
                                        new PriorityDecorator(
                                                new EncryptionDecorator(
                                                        new PushNotification()
                                                )
                                        )
                                )
                        )
                );

        testNotification(
                "Test 6: Push Notification with All Features",
                advancedPush,
                "Emergency alert"
        );


        /*
         * Test 7:
         * Demonstrating that decorator order may be changed
         */
        Notification firstOrder =
                new LoggingDecorator(
                        new EncryptionDecorator(
                                new EmailNotification()
                        )
                );

        Notification secondOrder =
                new EncryptionDecorator(
                        new LoggingDecorator(
                                new EmailNotification()
                        )
                );

        testNotification(
                "Test 7A: Logging Outside Encryption",
                firstOrder,
                "Garage door opened"
        );

        testNotification(
                "Test 7B: Encryption Outside Logging",
                secondOrder,
                "Garage door opened"
        );


        /*
         * Test 8:
         * Reusing the same basic notification object
         * to construct two independent configurations
         */
        Notification basicPush = new PushNotification();

        Notification loggedPush =
                new LoggingDecorator(basicPush);

        Notification priorityPush =
                new PriorityDecorator(basicPush);

        testNotification(
                "Test 8A: Logged Push",
                loggedPush,
                "Device disconnected"
        );

        testNotification(
                "Test 8B: Priority Push",
                priorityPush,
                "Device disconnected"
        );


        /*
         * Test 9:
         * Runtime configuration
         */
        Notification runtimeNotification =
                new EmailNotification();

        boolean encryptionEnabled = true;
        boolean priorityEnabled = true;
        boolean loggingEnabled = false;
        boolean retryEnabled = true;
        boolean deliveryReportEnabled = true;

        if (encryptionEnabled) {
            runtimeNotification =
                    new EncryptionDecorator(runtimeNotification);
        }

        if (priorityEnabled) {
            runtimeNotification =
                    new PriorityDecorator(runtimeNotification);
        }

        if (loggingEnabled) {
            runtimeNotification =
                    new LoggingDecorator(runtimeNotification);
        }

        if (retryEnabled) {
            runtimeNotification =
                    new RetryDecorator(runtimeNotification);
        }

        if (deliveryReportEnabled) {
            runtimeNotification =
                    new DeliveryReportDecorator(runtimeNotification);
        }

        testNotification(
                "Test 9: Runtime User Configuration",
                runtimeNotification,
                "Multiple failed login attempts"
        );
    }
}