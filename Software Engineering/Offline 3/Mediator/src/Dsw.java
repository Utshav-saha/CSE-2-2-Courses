public class Dsw extends Component{

    public Dsw(Mediator mediator) {
        super(mediator);
    }

    public void issueTestimonial(String id){
        System.out.println("DSW: Issuing testimonial");
        mediator.notify(this,"issueTestimonial", id);
    }

}
