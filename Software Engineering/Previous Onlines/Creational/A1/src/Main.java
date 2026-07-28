
public class Main {
    public static void main(String[] args) {

        TransportFactory tf = new TransportFactory();

        Transport t1 = tf.getTransport("Truck");
        Transport t2 = tf.getTransport("Ship");

        t1.deliver();
        t2.deliver();
    }
}