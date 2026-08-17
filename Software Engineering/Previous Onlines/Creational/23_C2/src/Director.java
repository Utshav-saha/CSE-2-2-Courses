public class Director {

    public void buildCompetitive(Builder builder){
        builder.setName("Competitive Setup");
        builder.setMonitor("240 Hz Monitor");
        builder.setKeyboard("Mechanical Keyboard");
        builder.setMouse("LightWeight Mouse");
    }

    public void buildCasual(Builder builder){
        builder.setName("Casual Setup");
        builder.setMonitor("Standard Monitor");
        builder.setKeyboard("Wireless Keyboard");
        builder.setMouse("Wireless Mouse");
    }
}
