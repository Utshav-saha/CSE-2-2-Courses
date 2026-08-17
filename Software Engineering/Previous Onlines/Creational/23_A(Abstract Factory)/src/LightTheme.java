public class LightTheme extends ThemeFactory {
    @Override
    Button createButton() {
        return new LightButton();
    }

    @Override
    TextField createTextField() {
        return new LightText();
    }

    @Override
    Dialog createDialog() {
        return new LightDialog();
    }
}
