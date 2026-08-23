import java.util.HashMap;
import java.util.Map;

public class Coordinator implements Mediator{

    private Dept dept;
    private Controller controller;
    private Dsw dsw;
    private Map<String, Student> students = new HashMap<>();
    private Map<Student, States> states = new HashMap<>();


    @Override
    public void registerDept(Dept dept) {
        this.dept = dept;
    }

    @Override
    public void registerController(Controller controller) {
        this.controller = controller;
    }

    @Override
    public void registerDsw(Dsw dsw) {
        this.dsw = dsw;
    }

    @Override
    public void registerStudent(Student student, String id) {
        students.put(id, student);
        states.put(student,States.start);
    }

    public void deptConfirm(States state, Student student) {
        if(state == States.start ) {
            states.put(student, States.deptConfirmed);
            System.out.println("Dept Confirmed");
        }
        else {
            System.out.println("Coordinator: Already Confirmed");
        }

    }

    public void issueOrder(States state, Student student) {

        if(state.ordinal() < States.deptConfirmed.ordinal()) {
            System.out.println("Coordinator: Cannot issue Order , get Dept confirmation first");
        } else if (state == States.deptConfirmed) {
            states.put(student, States.orderIssued);
            System.out.println("Coordinator: Order Issued");
            student.update("Your final result publication order has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued order");
        }

    }

    public void issueTestimonial(States state, Student student) {

        if(state.ordinal() < States.orderIssued.ordinal()) {
            System.out.println("Coordinator: Cannot issue Testimonial , get Order Issued first");
        } else if (state == States.orderIssued) {
            states.put(student, States.testimonialIssued);
            System.out.println("Coordinator: Testimonial Issued");
            student.update("Your Testimonial has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued testimonial");
        }
    }

    public void issueCertificate(States state, Student student) {

        if(state.ordinal() < States.testimonialIssued.ordinal()) {
            System.out.println("Coordinator: Cannot issue Certificate , get Testimonial first");
        } else if (state == States.testimonialIssued) {
            states.put(student, States.done);
            System.out.println("Coordinator: Certificate Issued");
            student.update("Your Certificate has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued certificate");
        }

    }

    public void display(States state, Student student) {

        System.out.println("Current State: " + student.getId() +" "+ state.name());

    }

    @Override
    public void notify(Component sender, String event, String id) {

        Student student = students.get(id);
        States state = states.get(student);

        if(student == null) {
            System.out.println("Coordinator:Student not found");
        }

        if(event.equals("issueOrder")) {
            issueOrder(state, student);
        }
        else if(event.equals("issueTestimonial")) {
            issueTestimonial(state, student);
        }
        else if(event.equals("issueCertificate")) {
            issueCertificate(state, student);
        }
        else if(event.equals("deptConfirm")) {
            deptConfirm(state, student);
        }
        else if(event.equals("getStatus")){
            display(state, student);
        }

    }



}
