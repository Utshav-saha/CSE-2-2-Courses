//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Director director = new Director();
        Builder builder1 = new setupBuilder();
        Builder builder2 = new setupBuilder();

        director.buildCompetitive(builder1);
        director.buildCasual(builder2);

        Setup Setup1 = builder1.getProduct();
        Setup Setup2 = builder2.getProduct();

        System.out.println(Setup1);
        System.out.println(Setup2);
    }
}