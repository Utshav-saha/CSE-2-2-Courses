abstract class BaseDecorator implements Notification{
    private Notification wrappee;
    public BaseDecorator(Notification wrappee){
        this.wrappee = wrappee;
    }

    @Override
    public void send(String message) {
        wrappee.send(message);
    }

    @Override
    public String getDescription() {
        return wrappee.getDescription();
    }
}
