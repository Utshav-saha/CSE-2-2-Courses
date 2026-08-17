import org.w3c.dom.Text;

abstract class ThemeFactory {
    abstract Button createButton();
    abstract TextField createTextField();
    abstract Dialog createDialog();

}
