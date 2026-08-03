public class Camera extends SmartDevice{

    private String name;
    Camera(MonitoringProtocol monitoring){
        super(monitoring);
        name = "Camera";
    }

    @Override
    public void monitor() {
        super.monitoring.check(name);
    }
}
