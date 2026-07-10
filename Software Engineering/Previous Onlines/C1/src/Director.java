public class Director {

    public void constructCommuter(Builder b){
        b.setType("Commuter");
        b.setFrame("Aluminum Frame");
        b.setGear("Single Speed Gear");
        b.setTireType("Road tires");

    }

    public void constructMountain(Builder b){
        b.setType("Mountain Beast");
        b.setFrame("Carbon Fibre Frame");
        b.setGear("12 Speed Gear");
        b.setTireType("Off-Road Grip tires");
    }
}
