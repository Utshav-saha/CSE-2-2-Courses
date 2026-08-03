public class Zigbee implements MonitoringProtocol{

    @Override
    public void check(String deviceName) {
        System.out.println("Checking via Zigbee of " + deviceName);
    }
}
