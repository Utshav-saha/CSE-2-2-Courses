public class Theme {

    private Button button;
    private Dialog dialog;
    private TextField text;

    public Theme(ThemeFactory factory) {
        button = factory.createButton();
        dialog = factory.createDialog();
        text = factory.createTextField();
    }

    public void print(){
        button.print();
        dialog.print();
        text.print();
    }


}
