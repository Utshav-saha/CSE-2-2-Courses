class GiftWrapping extends ItemDecorator {

    private static final double WRAPPING_CHARGE = 2.0;

    public GiftWrapping(Item wrappedItem) {
        super(wrappedItem);
    }

    @Override
    public double getPrice() {
        return super.getPrice() + WRAPPING_CHARGE;
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " + Gift Wrapping";
    }
}
