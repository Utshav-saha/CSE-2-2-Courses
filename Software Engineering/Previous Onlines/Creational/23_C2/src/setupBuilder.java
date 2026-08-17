public class setupBuilder implements Builder{

    private String name;
    private String Monitor;
    private String Keyboard;
    private String Mouse;

    @Override
    public void setMonitor(String monitor) {
        this.Monitor = monitor;
    }

    @Override
    public void setKeyboard(String keyboard) {
        this.Keyboard = keyboard;
    }

    @Override
    public void setMouse(String mouse) {
        this.Mouse = mouse;
    }

    @Override
    public void setName(String name){
        this.name = name;
    }

    public Setup getProduct(){
        return new Setup(name, Monitor, Keyboard, Mouse);
    }
}
