public class QuizSession  extends Content{

    @Override
    public void play() {
        System.out.println("Quiz Ongoing");
    }

    @Override
    public int getDuration() {
        return 60;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "Quiz Ongoing");
    }

}
