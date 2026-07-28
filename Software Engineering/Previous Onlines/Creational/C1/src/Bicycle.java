public class Bicycle {
    private final String type;
    private final String frame;
    private final String GearSystem;
    private final String TireType;

    public Bicycle(String type, String frame, String GearSystem, String TireType) {
        this.type = type;
        this.frame = frame;
        this.GearSystem = GearSystem;
        this.TireType = TireType;
    }

    @Override
    public String toString() {
        return "Bicycle{" +
                "type='" + type + '\'' +
                ", frame='" + frame + '\'' +
                ", GearSystem='" + GearSystem + '\'' +
                ", TireType='" + TireType + '\'' +
                '}';
    }
}
