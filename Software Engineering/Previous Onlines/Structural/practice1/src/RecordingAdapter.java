public class RecordingAdapter  extends Content{
    private LegacyRecordedClass recording;

    RecordingAdapter(LegacyRecordedClass recording) {
        this.recording = recording;
    }

    @Override
    public void play() {
        recording.startRecording();
    }

    @Override
    public int getDuration() {
        return recording.recordingLength();
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + recording.recordingLength());
    }
}
