public class main {
    public static void main(String[] args) {
        Employee e = new Employee("Utshav");
        TimeSheetReport tsr = new TimeSheetReport();
        System.out.println(e.getname());
//        e.printTimeSheetReport();
        tsr.printTimeSheetReport(e);
    }
}
