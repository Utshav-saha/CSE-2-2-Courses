public class Application {
    private Button button;
    private TextField textField;
    private Dialog dialog;

    Application(ThemeFactory factory){
        button = factory.createButton();
        textField = factory.createTextField();
        dialog = factory.createDialog();
    }

    public void render(){
        button.render();
        textField.render();
        dialog.render();
    }
}
