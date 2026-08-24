interface SubmissionStrategy {
    void submit(String file);
}

class ServerUpload implements SubmissionStrategy {
    @Override
    public void submit(String file) {
        System.out.println("Answer uploaded directly to server: " + file);
    }
}

class CloudUpload implements SubmissionStrategy {
    @Override
    public void submit(String file) {
        System.out.println("Answer uploaded through cloud: " + file);
    }
}

class EmailBackup implements SubmissionStrategy {
    @Override
    public void submit(String file) {
        System.out.println("Answer submitted through email backup: " + file);
    }
}

class ExamProcess {

    private SubmissionStrategy strategy;

    ExamProcess(SubmissionStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(SubmissionStrategy strategy) {
        this.strategy = strategy;
    }

    public final void submitExam(String student, String file) {
        verifyStudent(student);
        validateFile(file);
        strategy.submit(file);
        generateReceipt();
    }

    private void verifyStudent(String student) {
        System.out.println("Student verified");
    }

    private void validateFile(String file) {
        System.out.println("File validated");
    }

    private void generateReceipt() {
        System.out.println("Receipt generated");
    }
}

public class Main {
    public static void main(String[] args) {

        ExamProcess exam = new ExamProcess(new ServerUpload());

        exam.submitExam("Rahim", "answer.pdf");

        exam.setStrategy(new CloudUpload());

        exam.submitExam("Rahim", "answer2.pdf");
    }
}