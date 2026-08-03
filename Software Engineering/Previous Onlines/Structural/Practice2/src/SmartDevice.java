abstract class SmartDevice implements SmartComponent{
    MonitoringProtocol monitoring;

    SmartDevice(MonitoringProtocol monitoring){
        this.monitoring = monitoring;
    }
}
