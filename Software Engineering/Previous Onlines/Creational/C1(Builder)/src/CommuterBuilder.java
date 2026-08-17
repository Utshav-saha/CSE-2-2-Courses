public class CommuterBuilder implements Builder{
    private  String type;
    private  String frame;
    private  String GearSystem;
    private  String TireType;

    @Override
    public void setType() {
        this.type = "Commuter";
    }

    @Override
    public void setGear() {
        this.GearSystem = "Single Speed Gear";
    }

    @Override
    public void setFrame() {
        this.frame = "Aluminum Frame";
    }

    @Override
    public void setTireType() {
        this.TireType = "Road tires";
    }

    public Bicycle getCycle() {
        return new Bicycle(type, frame, GearSystem, TireType);
    }
}
