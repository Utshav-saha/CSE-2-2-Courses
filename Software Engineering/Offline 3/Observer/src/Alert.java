public class Alert {
    private String title;
    private Categories category;
    private String location;
    private int severity;
    private String instruction;

    public Alert(String title, Categories category, String location, int severity, String instruction) {
        this.title = title;
        this.category = category;
        this.location = location;
        this.severity = severity;
        this.instruction = instruction;
    }

    public Categories getCategory() {
        return category;
    }

    @Override
    public String toString() {
        return "Alert{" +
                "title='" + title + '\'' +
                ", category='" + category + '\'' +
                ", affected location='" + location + '\'' +
                ", severity level=" + severity +
                ", Safety instruction='" + instruction + '\'' +
                '}';
    }
}
