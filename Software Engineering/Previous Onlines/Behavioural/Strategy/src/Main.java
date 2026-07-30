//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Context c = new Context();

        String action = "sub";
        if(action.equals("add")) {
            c.setStrategy(new AddStrategy());
        }
        else if(action.equals("sub")) {
            c.setStrategy(new SubStrategy());
        }
        else if(action.equals("mul")) {
            c.setStrategy(new MulStrategy());
        }

        c.executeStrategy(5,6);
    }
}