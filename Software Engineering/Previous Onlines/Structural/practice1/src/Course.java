import java.util.ArrayList;
import java.util.List;

public class Course implements LearningContent{

    private String name;
    private List<LearningContent> contents;

    public Course(String name){
        this.name = name;
        contents = new ArrayList<LearningContent>();
    }

    public void addContent(LearningContent content){
        contents.add(content);
    }

    @Override
    public void play() {
        for(LearningContent c : contents){
            c.play();
        }
    }

    @Override
    public int getDuration() {
        int total = 0;
        for(LearningContent c : contents){
            total += c.getDuration();
        }
        return total;
    }

    @Override
    public void display(String indent) {
        for(LearningContent c : contents){
            c.display("Course " + name + " ");
        }
    }

    public void removeContent(LearningContent content){
        contents.remove(content);
    }

}
