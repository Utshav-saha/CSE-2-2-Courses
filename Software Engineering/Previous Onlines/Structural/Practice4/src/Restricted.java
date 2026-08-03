public class Restricted extends BaseDecorator{

    public Restricted(StorageComponent storage) {
        super(storage);
    }

    @Override
    public void open(){
        System.out.println("Checking access permission");
        super.open();
    }

}
