interface Strategy{
    void sendNotification(String message);
}
class email implements Strategy{
    @Override
    public void sendNotification(String message) {
        System.out.println("Email sent: " + message);
    }
}

class sms implements Strategy{
    @Override
    public void sendNotification(String message) {
        System.out.println("SMS sent: " + message);
    }
}

class app implements Strategy{
    @Override
    public void sendNotification(String message) {
        System.out.println("Mobile app notification sent: " + message);
    }
}

class system{
    Strategy transactionStrategy;
    Strategy balanceStrategy;
    Strategy offerStrategy;

    system(){
        transactionStrategy = new email();
        balanceStrategy = new email();
        offerStrategy = new email();
    }

    public void setTransactionStrategy(Strategy strategy){
        transactionStrategy = strategy;
    }

    public void setBalanceStrategy(Strategy strategy){
        balanceStrategy = strategy;
    }

    public void setOfferStrategy(Strategy strategy){
        offerStrategy = strategy;
    }

    public void TransactionNotification(){
        transactionStrategy.sendNotification("You have a transaction update");
    }

    public void BalanceNotification(){
        balanceStrategy.sendNotification("Your current Balance is 100k");
    }
    public void OfferNotification(){
        offerStrategy.sendNotification("Check out these new offers");
    }
}
public class Main {
    public static void main(String[] args) {
        system system = new system();
        system.TransactionNotification();
        system.BalanceNotification();
        system.OfferNotification();

        system.setTransactionStrategy(new sms());
        system.setBalanceStrategy(new sms());
        system.setOfferStrategy(new app());

        system.TransactionNotification();
        system.BalanceNotification();
        system.OfferNotification();
    }
}