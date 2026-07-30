abstract class BaseDecorator implements ApiResponse{

    protected ApiResponse wrappee;
    public BaseDecorator(ApiResponse apiResponse){
        this.wrappee = apiResponse;
    }

    @Override
    public String getBody() {
        return wrappee.getBody();
    }
}
