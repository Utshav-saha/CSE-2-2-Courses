class Employee {
    private String name;

    Employee(String s){
        this.name=s;
    }

    public String getname(){
        return this.name;
    }

    // Bad design , violates single responsibility - this should be a separate class
    public void printTimeSheetReport() {
        System.out.println("===================================");
        System.out.println("TIMESHEET REPORT");
        System.out.println("Employee Name: " + this.name);
        System.out.println("Hours Worked: 40"); // Example data
        System.out.println("===================================");
    }
}
