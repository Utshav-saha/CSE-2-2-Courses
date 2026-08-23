public interface Mediator {

    void registerDept(Dept dept);
    void registerController(Controller controller);
    void registerDsw(Dsw dsw);
    void registerStudent(Student student, String id);

    void notify(Component sender, String event, String id);

}
