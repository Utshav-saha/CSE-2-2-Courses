public class AssessmentAdapter  extends Content{
    private ExternalAssessment ext;
    public AssessmentAdapter(ExternalAssessment ext) {
        this.ext = ext;

    }

    @Override
    public void play() {
        ext.launchAssessment();
    }

    @Override
    public int getDuration() {
        return ext.estimatedMinutes();
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + ext.estimatedMinutes());
    }
}
