public class Coordinator implements Mediator{

    private Dept dept;
    private Controller controller;
    private Dsw dsw;
    private Student student;
    private States state = States.start;

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
    public void registerStudent(Student student) {
        this.student = student;
    }

    public void deptConfirm() {
        if(state == States.start ) {
            state = States.deptConfirmed;
            System.out.println("Dept Confirmed");
        }
        else {
            System.out.println("Coordinator: Already Confirmed");
        }

    }

    public void issueOrder() {

        if(state.ordinal() < States.deptConfirmed.ordinal()) {
            System.out.println("Coordinator: Cannot issue Order , get Dept confirmation first");
        } else if (state == States.deptConfirmed) {
            state = States.orderIssued;
            System.out.println("Coordinator: Order Issued");
            student.update("Your final result publication order has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued order");
        }

    }

    public void issueTestimonial() {

        if(state.ordinal() < States.orderIssued.ordinal()) {
            System.out.println("Coordinator: Cannot issue Testimonial , get Order Issued first");
        } else if (state == States.orderIssued) {
            state = States.testimonialIssued;
            System.out.println("Coordinator: Testimonial Issued");
            student.update("Your Testimonial has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued testimonial");
        }
    }

    public void issueCertificate() {

        if(state.ordinal() < States.testimonialIssued.ordinal()) {
            System.out.println("Coordinator: Cannot issue Certificate , get Testimonial first");
        } else if (state == States.testimonialIssued) {
            state = States.done;
            System.out.println("Coordinator: Certificate Issued");
            student.update("Your Certificate has been issued");

        }
        else {
            System.out.println("Coordinator: Already issued certificate");
        }

    }

    public void display() {

        System.out.println("Current State: " + state.name());

    }

    @Override
    public void notify(Component sender, String event) {

        if(event.equals("issueOrder")) {
            issueOrder();
        }
        else if(event.equals("issueTestimonial")) {
            issueTestimonial();
        }
        else if(event.equals("issueCertificate")) {
            issueCertificate();
        }
        else if(event.equals("deptConfirm")) {
            deptConfirm();
        }
        else if(event.equals("getStatus")){
            display();
        }

    }



}
