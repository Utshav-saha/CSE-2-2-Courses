public class DisasterManagement {
    public Authority authority;
    private Alert alert;

    public DisasterManagement(){
        this.authority = new Authority();
    }

    public void createAlert(Alert alert){
        this.alert = alert;
        authority.notify(alert);
    }
}
