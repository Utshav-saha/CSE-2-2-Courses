public class Text implements StorageComponent{

    private String filename;
    private double size;
    public Text(String filename, double size) {
        this.filename = filename;
        this.size = size;
    }
    @Override
    public void open() {
        System.out.println("Opening Text " + filename);
    }

    @Override
    public double getSize() {
        return size;

    }

    @Override
    public void display(String indent) {
        System.out.println(indent + filename + ": " + size);
    }


}
