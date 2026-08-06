public class Coordinator implements Mediator{

    private Dept dept;
    private Controller controller;
    private Dsw dsw;
    private Student student;
    
    private boolean start = true;
    private boolean deptConfirmed = false;
    private boolean issuedOrder = false;
    private boolean testimonial = false;
    private boolean complete = false;


    @Override
    public void registerDept(Dept dept) {

    }

    @Override
    public void registerController(Controller controller) {

    }

    @Override
    public void registerDsw(Dsw dsw) {

    }

    @Override
    public void registerStudent(Student student) {

    }

    @Override
    public void deptConfirm() {

    }

    @Override
    public void issueOrder() {

    }

    @Override
    public void issueTestimonial() {

    }

    @Override
    public void issueCertificate() {

    }

    @Override
    public void display() {

    }
}
