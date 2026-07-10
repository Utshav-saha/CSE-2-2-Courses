public class TransportFactory {
    public Transport getTransport(String type) {

        if(type == null) {
            return null;
        }
        else if (type.equals("Ship")) {
            return new Ship();
        }
        else if (type.equals("Truck")) {
            return new Truck();
        }

        throw new IllegalArgumentException("Unknown Transport");
    }
}
