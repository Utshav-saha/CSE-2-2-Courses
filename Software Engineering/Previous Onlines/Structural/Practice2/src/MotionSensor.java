public class MotionSensor extends SmartDevice{
    
    private String name;
    MotionSensor(MonitoringProtocol monitoring){
        super(monitoring);
        name = "Motion Sensor";
    }

    @Override
    public void monitor() {
        super.monitoring.check(name);
    }
}
