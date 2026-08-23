public class Dept extends Component {

    public Dept(Mediator mediator) {
        super(mediator);
    }
    public void confirm(String id){
        System.out.println("Department Head : Confirming Request");
        mediator.notify(this,"deptConfirm", id);

    }
}
