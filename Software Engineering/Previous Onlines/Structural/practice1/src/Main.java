//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Content video = new VideoLesson();
        Content audio = new AudioLecture();
        Content quiz = new QuizSession();

        LegacyRecordedClass recording = new LegacyRecordedClass();
        Content recordingAdapter = new RecordingAdapter(recording);

        ExternalAssessment assessment = new ExternalAssessment();
        Content assessmentAdapter = new AssessmentAdapter(assessment);

        video.play();
        recordingAdapter.play();

        System.out.println("Starting Module 1");
        Module m1 = new Module("Module 1");
        m1.addContent(video);
        m1.addContent(audio);
        m1.addContent(assessmentAdapter);
        m1.play();


        System.out.println("Starting Module 2");
        Module m2 = new Module("Module 2");
        m2.addContent(quiz);
        m2.play();

        System.out.println("Starting Course 1");
        Course c = new Course("Course 1");
        c.addContent(m1);
        c.addContent(m2);
        c.addContent(recordingAdapter);
        c.play();
        System.out.println(c.getDuration());
    }
}