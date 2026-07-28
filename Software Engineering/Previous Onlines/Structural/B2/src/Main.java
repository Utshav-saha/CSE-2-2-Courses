//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
    LegacyHeater heater = new LegacyHeater();
    OldSmartBulb oldSmartBulb = new OldSmartBulb();

    buldAdapter a1 = new buldAdapter(oldSmartBulb);
    heaterAdapter a2 = new heaterAdapter(heater);

    a1.turnOn();
    a1.turnOff();

    a2.turnOn();
    a2.turnOff();
    }
}