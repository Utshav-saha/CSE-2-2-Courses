public class buldAdapter implements SmartDevice{

    private OldSmartBulb wrapee;

    public buldAdapter(OldSmartBulb wrapee) {
        this.wrapee = wrapee;
    }

    @Override
    public void turnOn(){
        wrapee.powerOn();
    }

    @Override
    public void turnOff(){
        wrapee.powerOff();
    }
}
