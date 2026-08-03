public class Encryption extends BaseDecorator{

    public Encryption(StorageComponent storage) {
        super(storage);
    }

    @Override
    public void open(){
        System.out.println("Decrypting Document");
        super.open();
    }

}
