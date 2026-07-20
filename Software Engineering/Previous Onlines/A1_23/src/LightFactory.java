public class LightFactory implements ThemeFactory{

    public Button createButton(){
        return  new LightButton();
    }
    public TextField createTextField(){
        return new LightText();
    }
    public Dialog createDialog(){
        return new LightDialog();
    }

}
