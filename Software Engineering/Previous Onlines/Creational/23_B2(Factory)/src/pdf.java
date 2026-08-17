public class pdf implements Report{
    @Override
    public void open() {
        System.out.println("Opening pdf report");
    }

    @Override
    public void generate() {
        System.out.println("Generating pdf report");
    }
}
