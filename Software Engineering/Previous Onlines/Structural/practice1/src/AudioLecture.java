public class AudioLecture  extends Content{

    @Override
    public void play() {
        System.out.println("Audio Playing");
    }

    @Override
    public int getDuration() {
        return 60;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "Audio Playing");
    }

}
