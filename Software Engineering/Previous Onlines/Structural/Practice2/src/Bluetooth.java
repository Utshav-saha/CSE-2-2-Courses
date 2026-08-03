public class Bluetooth implements MonitoringProtocol{

    @Override
    public void check(String deviceName) {
        System.out.println("Checking via Bluetooth of " + deviceName);
    }
}
