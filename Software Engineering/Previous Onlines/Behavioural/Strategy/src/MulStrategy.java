public class MulStrategy implements Strategy {

    @Override
    public void execute(int a, int b) {
        System.out.printf("%d x %d = %d", a, b, a * b);
    }
}
