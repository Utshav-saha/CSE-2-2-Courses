abstract class state{
    protected trafficLight light;
    state(trafficLight light){
        this.light = light;
    }
    public abstract void run();
}

class red extends state{
    public red(trafficLight light){
        super(light);
    }

    @Override
    public void run() {
        System.out.println("Red");
        try {
            Thread.sleep(5000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        light.setState(new yellow(light));
    }
}

class yellow extends state{
    public yellow(trafficLight light){
        super(light);
    }

    @Override
    public void run() {
        System.out.println("Yellow");
        try {
            Thread.sleep(2000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        light.setState(new green(light));
    }
}

class green extends state{
    public green(trafficLight light){
        super(light);
    }

    @Override
    public void run() {
        System.out.println("Green");
        try {
            Thread.sleep(10000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        light.setState(new red(light));
    }
}

class trafficLight{
    private state state;
    public trafficLight(){
        this.state = new red(this);
    }

    public void setState(state state){
        this.state = state;
    }

    public void run(){
        state.run();
    }

}
public class Main {
    public static void main(String[] args) {
        trafficLight light = new trafficLight();
        while(true){
            light.run();
        }
    }
}