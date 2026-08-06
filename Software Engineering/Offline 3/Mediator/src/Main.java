//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Mediator Coordinator = new Coordinator();

        Dept dept = new Dept(Coordinator);
        Controller coe = new Controller(Coordinator);
        Dsw dsw = new Dsw(Coordinator);
        Student student = new Student(Coordinator, "Utshav");

        Coordinator.registerDept(dept);
        Coordinator.registerController(coe);
        Coordinator.registerDsw(dsw);
        Coordinator.registerStudent(student);

        coe.issueCertificate(); // Wrong
        System.out.println();

        dept.confirm();
        System.out.println();

        coe.issueCertificate(); // Wrong
        System.out.println();

        student.getStatus();
        System.out.println();

        coe.issueOrder();
        System.out.println();

        dsw.issueTestimonial();
        System.out.println();

        coe.issueCertificate();
        System.out.println();

        dept.confirm(); // Already Done
        System.out.println();

        student.getStatus();
        System.out.println();


    }
}