public class DarkFactory implements ThemeFactory{

    public Button createButton(){
        return  new DarkButton();
    }
    public TextField createTextField(){
        return new DarkText();
    }
    public Dialog createDialog(){
        return new DarkDialog();
    }
}
