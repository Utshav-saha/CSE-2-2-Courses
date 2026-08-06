public class Student extends Component{

    String name;
    public Student(Mediator mediator, String name) {
        super(mediator);
        this.name = name;
    }

    public void update(String msg){
        System.out.println(name + " Got notification: " + msg);
    }

    public void getStatus(){
        mediator.display();
    }
}
