public class word implements Report{
    @Override
    public void open() {
        System.out.println("Opening word report");
    }

    @Override
    public void generate() {
        System.out.println("Generating word report");
    }
}
