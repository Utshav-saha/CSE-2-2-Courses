public class Student extends Component{

    String name;
    String id;
    public Student(Mediator mediator, String name, String id) {
        super(mediator);
        this.name = name;
        this.id = id;
    }

    public void update(String msg){
        System.out.println(name + " Got notification: " + msg);
    }

    public void getStatus(){
        mediator.notify(this,"getStatus",id);
    }

    public String getId(){
        return id;
    }
}
