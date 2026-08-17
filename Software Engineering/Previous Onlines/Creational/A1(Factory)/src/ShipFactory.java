public class ShipFactory extends Factory{

    public Transport getTransport(){
        return new Ship();
    }
}
