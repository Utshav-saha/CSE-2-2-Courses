abstract class Factory {

    public void render(){
        Report report = getReport();
        report.open();
        report.generate();
        System.out.println("Success");

    }

    public abstract Report getReport();
}
