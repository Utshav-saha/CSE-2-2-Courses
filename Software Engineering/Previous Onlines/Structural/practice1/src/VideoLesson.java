public class VideoLesson extends Content{
    @Override
    public void play() {
        System.out.println("Video Playing");
    }

    @Override
    public int getDuration() {
        return 60;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "Video Playing");
    }
}
