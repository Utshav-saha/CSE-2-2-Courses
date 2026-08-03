abstract class BaseDecorator implements StorageComponent{
    protected StorageComponent storage;
    public BaseDecorator(StorageComponent storage) {
        this.storage = storage;
    }

    @Override
    public void open() {
        storage.open();
    }

    @Override
    public double getSize() {
        return storage.getSize();
    }

    @Override
    public void display(String indent) {
        storage.display(indent);
    }


}
