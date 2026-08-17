public class MountainBuilder implements Builder{
    private  String type;
    private  String frame;
    private  String GearSystem;
    private  String TireType;

    @Override
    public void setType() {
        this.type = "Mountain Beast";
    }

    @Override
    public void setGear() {
        this.GearSystem = "12 Speed Gear";
    }

    @Override
    public void setFrame() {
        this.frame = "Carbon Fibre Frame";
    }

    @Override
    public void setTireType() {
        this.TireType = "Off-Road Grip tires";
    }

    public Bicycle getCycle() {
        return new Bicycle(type, frame, GearSystem, TireType);
    }
}
