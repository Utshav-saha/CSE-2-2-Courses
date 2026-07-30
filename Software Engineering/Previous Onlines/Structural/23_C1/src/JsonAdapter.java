public class JsonAdapter implements ApiResponse {

    private final LegacyInternalXMLService legacyService;

    public JsonAdapter(LegacyInternalXMLService legacyService) {
            this.legacyService = legacyService;
    }

    @Override
    public String getBody() {

        String xml = legacyService.getDataAsXML();

        return "JSON converted from: " + xml;
    }
}