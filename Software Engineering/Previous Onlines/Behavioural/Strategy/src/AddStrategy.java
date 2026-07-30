public class AddStrategy implements Strategy {

    @Override
    public void execute(int a, int b) {
        System.out.printf("%d + %d = %d", a, b, a + b);
    }
}
