import java.util.ArrayList;
import java.util.List;

public class Folder implements StorageComponent{

    private String folderName;
    private List<StorageComponent> components;
    public Folder(String folderName){
        this.folderName = folderName;
        components = new ArrayList<StorageComponent>();

    }

    public void addComponent(StorageComponent component){
        components.add(component);
    }

    public void removeComponent(StorageComponent component){
        components.remove(component);
    }

    @Override
    public void open() {
        for(StorageComponent c : components){
            c.open();
        }
    }

    @Override
    public double getSize() {
        double total = 0;
        for(StorageComponent c : components){
            total += c.getSize();
        }
        return total;

    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "Folder: " + folderName);
        for(StorageComponent c : components){
            c.display(indent + "  ");
        }
    }
}
