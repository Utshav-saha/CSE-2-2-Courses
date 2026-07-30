public class Encrypt extends BaseDecorator{

    Encrypt(ApiResponse apiResponse) {
        super(apiResponse);
    }

    @Override
    public String getBody() {
        return " Encrypting " + super.getBody();
    }
}
