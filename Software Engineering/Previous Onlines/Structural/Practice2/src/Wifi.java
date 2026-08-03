public class Wifi implements MonitoringProtocol{

    @Override
    public void check(String deviceName) {
        System.out.println("Checking via wifi of " + deviceName);
    }
}
