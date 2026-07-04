package service;

import model.*;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * Coordinates order creation.
 *
 * Several methods below repeat long Order constructor calls with many optional
 * parameters. That is intentional assignment material for refactoring.
 */
public class OrderService {
    private int nextNumber = 1001;
    private final OrderDirector director = new OrderDirector();

    public OrderItem createOrderItem(MenuItem item, int quantity, Size size, boolean extraCheese, boolean spicy, String note) {
//        return new OrderItem(item, quantity, size, extraCheese, spicy, note);
        ItemBuilder builder = new ItemBuilder(item,quantity);
        builder.setSize(size);
        builder.setExtraCheese(extraCheese);
        builder.setSpicy(spicy);
        builder.setNote(note);
        return builder.getResult();
    }

    public Order createDeliveryOrder(String customerName,
                                     String phone,
                                     String address,
                                     List<OrderItem> items,
                                     String couponCode,
                                     boolean rushOrder,
                                     String specialInstructions){


        NormalOrderBuilder builder = new NormalOrderBuilder(nextOrderId(), customerName, phone, items);
        director.DeliveryOrderBuild(builder, address, couponCode, rushOrder, specialInstructions);

        return builder.getResult();
    }

    public Order createPickupOrder(String customerName, String phone, List<OrderItem> items) {


        NormalOrderBuilder builder = new NormalOrderBuilder(nextOrderId(), customerName, phone, items);
        director.PickupOrderBuild(builder);

        return builder.getResult();
    }

    public Order createScheduledGiftOrder(String customerName,
                                          String phone,
                                          String address,
                                          List<OrderItem> items,
                                          LocalDateTime scheduledTime) {

        NormalOrderBuilder builder = new NormalOrderBuilder(nextOrderId(), customerName, phone, items);
        director.ScheduledGiftOrderBuild(builder,address, scheduledTime);
        return builder.getResult();
    }

    public Order createSampleFamilyOrder(MenuCatalog catalog) {


        List<OrderItem> items = new ArrayList<>();
//        items.add(new OrderItem(catalog.findByCode("P01"), 2, Size.LARGE, true, false, "half spicy"));
//        items.add(new OrderItem(catalog.findByCode("B02"), 3, Size.MEDIUM, true, true, ""));
//        items.add(new OrderItem(catalog.findByCode("D02"), 4, Size.MEDIUM, false, false, "less sugar"));
//        items.add(new OrderItem(catalog.findByCode("S02"), 2, Size.LARGE, false, true, ""));

        ItemBuilder i1 = new ItemBuilder(catalog.findByCode("P01"), 2);
        i1.setSize(Size.LARGE);
        i1.setExtraCheese(true);
        i1.setNote("half spicy");
        items.add(i1.getResult());


        ItemBuilder i2 = new ItemBuilder(catalog.findByCode("B02"), 3);
        i2.setExtraCheese(true);
        i2.setSpicy(true);
        items.add(i2.getResult());

        ItemBuilder i3 = new ItemBuilder(catalog.findByCode("D02"), 4);
        i3.setNote("less sugar");
        items.add(i3.getResult());

        ItemBuilder i4 = new ItemBuilder(catalog.findByCode("S02"), 2);
        i4.setSize(Size.LARGE);
        i4.setSpicy(true);
        items.add(i4.getResult());

        NormalOrderBuilder builder = new NormalOrderBuilder(nextOrderId(), "Sample Family", "01711111111", items);
        director.FamilyOrderBuild(builder, "House 25, Road 4, Dhanmondi", "FAMILY15", 50, "Deliver together");

        return builder.getResult();
    }

    private String nextOrderId() {
        return "FF-" + nextNumber++;
    }
}

