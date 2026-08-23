public class Controller extends Component{

    public Controller(Mediator mediator) {
        super(mediator);
    }

    public void issueOrder(String id){
        System.out.println("Controller : Issuing the office order for final result publication");
        mediator.notify(this,"issueOrder", id);
    }

    public void issueCertificate(String id){
        System.out.println("Issuing certificate and academic transcript.");
        mediator.notify(this,"issueCertificate", id);
    }
}
