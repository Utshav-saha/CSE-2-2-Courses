import java.util.Scanner;

// don't need this , emni i korlam
class creditCard{
  private int amount;
  private String number;
  private int cvv;

  creditCard(String number, int cvv){
      this.amount = 500;
      this.number = number;
      this.cvv = cvv;
  }

  public void transaction(int price){
      if(price > amount){
          System.out.println("You do not have enough money!");
      }
      else{
          System.out.println(price + "$ debited from " + number + " card ");
      }
  }
}


interface strategy{
    void paybill(int amount);
}

class bkashPay implements strategy{
    @Override
    public void paybill(int amount) {
        System.out.println("Paying " + amount + " through bkash");
    }
}

class cryptoPay implements strategy{
    @Override
    public void paybill(int amount) {
        System.out.println("Paying " + amount + " through bitcoin");
    }
}

class cardPay implements strategy{

    private creditCard card;

    @Override
    public void paybill(int amount) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter card number: ");
        String number = scanner.nextLine();
        System.out.println("Enter cvv: ");
        int cvv = scanner.nextInt();
        creditCard card = new creditCard(number, cvv);
        this.card = card;
        card.transaction(amount);
    }
}

class system{
    strategy payMethod;

    system(){
        this.payMethod = new bkashPay();
    }

    public void setPayMethod(strategy payMethod) {
        this.payMethod = payMethod;
    }

    public void doPayment(int amount){
        payMethod.paybill(amount);
    }
}

public class Main {
    public static void main(String[] args) {

        system system = new system();
        system.doPayment(1000);

        system.setPayMethod(new cardPay());
        system.doPayment(1000);
        system.doPayment(200);
    }
}