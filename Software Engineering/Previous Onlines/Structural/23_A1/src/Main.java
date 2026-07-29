public class Main {

    private static void printCase(
            String caseName,
            Delivery delivery) {

        System.out.println(
                "\n========================================"
        );

        System.out.println(caseName);

        System.out.println(
                "========================================"
        );

        delivery.displayDetails();
    }

    public static void main(String[] args) {

        /*
         * Case 1
         *
         * Decorative vase: $40
         * Gift wrapping: $2
         * Local delivery: 10 miles × $1 = $10
         *
         * Total: $52
         * Time: 1 week
         */

        Item vase = new Gift(
                "Decorative Vase",
                40
        );

        vase = new GiftWrapping(vase);

        Delivery case1 = new LocalDelivery(
                vase,
                10,
                new StandardDeliveryMode()
        );

        printCase("CASE 1", case1);


        /*
         * Case 2
         *
         * Wooden souvenir: $60
         * Gift wrapping: $2
         * National delivery:
         *     50 miles × $1 + $20 = $70
         * Express delivery: $10
         *
         * Total: $142
         * Time: 2 days
         */

        Item souvenir = new Gift(
                "Wooden Souvenir",
                60
        );

        souvenir = new GiftWrapping(souvenir);

        Delivery case2 = new NationalDelivery(
                souvenir,
                50,
                new ExpressDeliveryMode()
        );

        printCase("CASE 2", case2);


        /*
         * Case 3
         *
         * Crystal showpiece: $150
         * International delivery: $500
         * Priority delivery: $25
         *
         * Total: $675
         * Time: 5 days
         */

        Item showpiece = new Gift(
                "Crystal Showpiece",
                150
        );

        Delivery case3 = new InternationalDelivery(
                showpiece,
                new PriorityDeliveryMode()
        );

        printCase("CASE 3", case3);


        /*
         * Additional Test 1:
         * Local delivery with Priority mode
         */

        Item ornament = new Gift(
                "Decorative Ornament",
                30
        );

        Delivery localPriority = new LocalDelivery(
                ornament,
                5,
                new PriorityDeliveryMode()
        );

        printCase(
                "ADDITIONAL TEST: LOCAL PRIORITY",
                localPriority
        );


        /*
         * Additional Test 2:
         * International delivery with Express mode
         */

        Item souvenirSet = new Gift(
                "Souvenir Set",
                100
        );

        souvenirSet = new GiftWrapping(souvenirSet);

        Delivery internationalExpress =
                new InternationalDelivery(
                        souvenirSet,
                        new ExpressDeliveryMode()
                );

        printCase(
                "ADDITIONAL TEST: INTERNATIONAL EXPRESS",
                internationalExpress
        );
    }
}