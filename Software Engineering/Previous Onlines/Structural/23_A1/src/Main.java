public class Main {
    public static void main(String[] args) {

        System.out.println("====== CASE 1 ======");

        Item case1Item = new Gift("Vase",40.0);
        case1Item = new GiftWrapping(case1Item);

        DeliveryRegion local = new Local();
        Standard package1 = new Standard(local, case1Item, 10);

        System.out.println(package1.getTotalCost());
        System.out.println("Total Cost: $" + package1.getTotalCost());
        System.out.println("Time: " + package1.getTime());


        System.out.println("\n====== CASE 2 ======");

        Item case2Item = new Gift("Wooden",60.0);
        case2Item = new GiftWrapping(case2Item);

        DeliveryRegion national = new National();
        Express package2 = new Express(national, case2Item, 50);

        System.out.println(package2.getTotalCost());
        System.out.println("Total Cost: $" + package2.getTotalCost());
        System.out.println("Time: " + package2.getTime());


        System.out.println("\n====== CASE 3 ======");

        Item case3Item = new Gift("Crystal",150.0);

        DeliveryRegion international = new International();
        Priority package3 = new Priority(international, case3Item, 50);

        System.out.println(package2.getTotalCost());
        System.out.println("Total Cost: $" + package3.getTotalCost());
        System.out.println("Time: " + package3.getTime());
    }
}