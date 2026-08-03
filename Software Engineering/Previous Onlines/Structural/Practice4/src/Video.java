public class Video implements StorageComponent{

    private String filename;
    private double size;
    public Video(String filename, double size) {
        this.filename = filename;
        this.size = size;
    }
    @Override
    public void open() {
        System.out.println("Opening video " + filename);
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
