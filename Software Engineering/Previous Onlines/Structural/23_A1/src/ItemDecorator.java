abstract class ItemDecorator implements Item {
    protected final Item wrappedItem;

    public ItemDecorator(Item wrappedItem) {
        this.wrappedItem = wrappedItem;
    }

    @Override
    public double getPrice() {
        return wrappedItem.getPrice();
    }

    @Override
    public String getDescription() {
        return wrappedItem.getDescription();
    }
}
