public class DarkTheme extends ThemeFactory {
    @Override
    Button createButton() {
        return new DarkButton();
    }

    @Override
    TextField createTextField() {
        return new DarkText();
    }

    @Override
    Dialog createDialog() {
        return new DarkDialog();
    }
}
