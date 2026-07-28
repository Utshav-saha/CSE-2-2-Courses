public class CycleBuilder implements Builder{
    private  String type;
    private  String frame;
    private  String GearSystem;
    private  String TireType;

    @Override
    public void setType(String type) {
        this.type = type;
    }

    @Override
    public void setGear(String gear) {
        this.GearSystem = gear;
    }

    @Override
    public void setFrame(String frame) {
        this.frame = frame;
    }

    @Override
    public void setTireType(String tireType) {
        this.TireType = tireType;
    }

    public Bicycle getCycle() {
        return new Bicycle(type, frame, GearSystem, TireType);
    }
}
