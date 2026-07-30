public class Compress extends BaseDecorator{

    Compress(ApiResponse apiResponse) {
        super(apiResponse);
    }

    @Override
    public String getBody() {
        return " Compressing " + super.getBody();
    }
}
