abstract class Factory {

    public void render(){
        Transport transport = getTransport();
        transport.deliver();
    }
    public abstract Transport getTransport();
}
