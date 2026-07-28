public class heaterAdapter implements SmartDevice{

    private LegacyHeater wrapee;

    heaterAdapter(LegacyHeater wrapee) {
        this.wrapee = wrapee;
    }

    @Override
    public void turnOn(){
        wrapee.startHeating();
    }

    @Override
    public void turnOff(){
        wrapee.stopHeating();
    }
}
