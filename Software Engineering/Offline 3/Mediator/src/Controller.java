public class Controller extends Component{

    public Controller(Mediator mediator) {
        super(mediator);
    }

    public void issueOrder(){
        System.out.println("Controller : Issuing the office order for final result publication");
        mediator.issueOrder();
    }

    public void issueCertificate(){
        System.out.println("Issuing certificate and academic transcript.");
        mediator.issueCertificate();
    }
}
