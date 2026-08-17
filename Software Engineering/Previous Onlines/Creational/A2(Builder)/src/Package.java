public class Package {

    private String name;
    private String Flight;
    private String Hotel;
    private String DailyActivity;

    public Package(String name, String flight, String hotel, String dailyActivity) {
        this.name = name;
        Flight = flight;
        Hotel = hotel;
        DailyActivity = dailyActivity;
    }

    @Override
    public String toString() {
        return "Package{" +
                "name='" + name + '\'' +
                ", Flight='" + Flight + '\'' +
                ", Hotel='" + Hotel + '\'' +
                ", DailyActivity='" + DailyActivity + '\'' +
                '}';
    }
}
