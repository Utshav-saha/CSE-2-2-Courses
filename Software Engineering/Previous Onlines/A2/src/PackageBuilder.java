public class PackageBuilder implements Builder{

    private String name;
    private String Flight;
    private String Hotel;
    private String DailyActivity;

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void setFlight(String Flight) {
        this.Flight = Flight;
    }

    @Override
    public void setHotel(String Hotel) {
        this.Hotel = Hotel;
    }

    @Override
    public void setActivity(String Activity) {
        this.DailyActivity = Activity;
    }

    public Package getPackage(){
        return new Package(name, Flight, Hotel, DailyActivity);
    }
}
