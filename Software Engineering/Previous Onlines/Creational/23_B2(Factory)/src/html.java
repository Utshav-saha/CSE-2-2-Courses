public class html implements Report{
    @Override
    public void open() {
        System.out.println("Opening html report");
    }

    @Override
    public void generate() {
        System.out.println("Generating html report");
    }
}
