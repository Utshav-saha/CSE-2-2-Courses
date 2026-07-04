package model;

import java.util.Objects;

public class ItemBuilder implements OrderItemBuilder{

    public static final double EXTRA_CHEESE_PRICE = 60.0;

    private  MenuItem menuItem;
    private  int quantity;
    private  Size size = Size.MEDIUM;
    private  boolean extraCheese = false;
    private  boolean spicy = false;
    private  String note = "";

    public ItemBuilder(MenuItem menuItem, int quantity) {
        this.menuItem = menuItem;
        this.quantity = quantity;
    }

    public void setSize(Size size){
        this.size = size;
    };
    public void setExtraCheese(boolean extraCheese){
        this.extraCheese = extraCheese;
    };
    public void setSpicy(boolean spicy){
        this.spicy = spicy;
    };
    public void setNote(String note){
        this.note = note;
    };

    public OrderItem getResult(){
        this.menuItem = Objects.requireNonNull(menuItem, "Menu item cannot be null");
        if (quantity <= 0) {
            throw new IllegalArgumentException("Quantity must be positive");
        }
        this.note = note != null ? note.trim() : "";

        return new OrderItem(menuItem, quantity, size, extraCheese, spicy, note);
    }


}
