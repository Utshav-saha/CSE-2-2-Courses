import java.util.HashMap;
import java.util.List;
import java.util.Map;

abstract class Department{

    private static int id = 1;
    private Map<Integer, String> patients = new HashMap<>();
    final void run(String name){
        registerPatient(name);
        recordVitals();
        assessment();
        treatment();
        discharge();
    }

    public void registerPatient(String name){
        int visitId = id++;
        patients.put(visitId, name);
        System.out.println("Registered Patient " + name + " at " + id);
    }

    public void recordVitals(){
        System.out.println("Temperature : 101 degree farenheit + Blood Pressure: 75/110");
    }

    public abstract void assessment();
    public abstract void treatment();
    public void discharge(){
        System.out.println("Patient discharged");
    }

}

class General extends Department {
    @Override
    public void assessment() {
        System.out.println("Doctor performs normal diagnosis");
    }

    @Override
    public void treatment() {
        System.out.println("Prescribe standard medicine");
    }
}

class Pediatrics extends Department {
    @Override
    public void assessment() {
        System.out.println("Doctor checks symptoms by ensuring child comfort level");
    }

    @Override
    public void treatment() {
        System.out.println("Give child safe medicine, friendly reassurance message");
    }
}

class Emergency extends Department {
    @Override
    public void assessment() {
        System.out.println("Quick triage check");
    }

    @Override
    public void treatment() {
        System.out.println("Immediate emergency procedure");
    }
}

public class Main {
    public static void main(String[] args) {

        Department general = new General();
        Department pediatrics = new Pediatrics();
        Department emergency = new Emergency();

        System.out.println("=== GENERAL DEPARTMENT ===");
        general.run("Rahim");

        System.out.println("\n=== PEDIATRICS DEPARTMENT ===");
        pediatrics.run("Karim");

        System.out.println("\n=== EMERGENCY DEPARTMENT ===");
        emergency.run("Sakib");
    }
}