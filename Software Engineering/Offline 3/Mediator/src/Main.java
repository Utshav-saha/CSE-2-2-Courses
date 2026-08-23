//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Mediator Coordinator = new Coordinator();

        Dept dept = new Dept(Coordinator);
        Controller coe = new Controller(Coordinator);
        Dsw dsw = new Dsw(Coordinator);
        String id1 = "77";
        Student student1 = new Student(Coordinator, "Utshav", id1);

        String id2 = "100";
        Student student2 = new Student(Coordinator, "abc", id2);

        Coordinator.registerDept(dept);
        Coordinator.registerController(coe);
        Coordinator.registerDsw(dsw);
        Coordinator.registerStudent(student1, student1.getId());
        Coordinator.registerStudent(student2, student2.getId());

        coe.issueCertificate(id1); // Wrong
        dept.confirm(id2);
        System.out.println();

        dept.confirm(id1);
        System.out.println();

        coe.issueCertificate(id1); // Wrong
        coe.issueOrder(id2);
        System.out.println();

        student1.getStatus();
        student2.getStatus();
        System.out.println();

        coe.issueOrder(id1);
        System.out.println();

        dsw.issueTestimonial(id1);
        dsw.issueTestimonial(id2);
        System.out.println();

        coe.issueCertificate(id1);
        coe.issueOrder(id2);
        coe.issueCertificate(id2);
        System.out.println();

        dept.confirm(id1); // Already Done
        System.out.println();

        student1.getStatus();
        student2.getStatus();
        System.out.println();


    }
}