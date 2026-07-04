package model;

public interface OrderItemBuilder {

    public void setSize(Size size);
    public void setExtraCheese(boolean extraCheese);
    public void setSpicy(boolean spicy);
    public void setNote(String note);
}
