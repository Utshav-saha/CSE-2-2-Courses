public class Dept extends Component {

    public Dept(Mediator mediator) {
        super(mediator);
    }
    public void confirm(){
        System.out.println("Department Head : Confirming Request");
        mediator.notify(this,"deptConfirm");

    }
}
