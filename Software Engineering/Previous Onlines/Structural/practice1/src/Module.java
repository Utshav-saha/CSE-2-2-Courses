import java.util.ArrayList;
import java.util.List;

public class Module implements LearningContent{
    private String name;
    private List<Content> contents;

    public Module(String name){
        this.name = name;
        contents = new ArrayList<Content>();
    }

    public void addContent(Content content){
        contents.add(content);
    }

    @Override
    public void play() {
        for(Content c : contents){
            c.play();
        }
    }

    @Override
    public int getDuration() {
        int total = 0;
        for(Content c : contents){
            total += c.getDuration();
        }
        return total;
    }

    @Override
    public void display(String indent) {
        for(Content c : contents){
            c.display("Module " + name + " ");
        }
    }

    public void removeContent(Content content){
        contents.remove(content);
    }


}
