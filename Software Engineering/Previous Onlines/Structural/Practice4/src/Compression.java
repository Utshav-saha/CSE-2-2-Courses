public class Compression extends BaseDecorator{

    public Compression(StorageComponent storage) {
       super(storage);
    }

    @Override
    public void open(){
        System.out.println("Decompressing Document");
        super.open();
    }

    @Override
    public double getSize() {
        return super.getSize()*0.7;
    }


}
