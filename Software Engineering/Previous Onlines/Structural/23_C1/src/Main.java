//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static ApiResponse execute(ApiResponse obj, boolean encrypt, boolean compress , boolean reverse){

        if(reverse){
            if(encrypt){
                obj = new Encrypt(obj);
            }
            if(compress){
                obj = new Compress(obj);
            }
        }
        else if(!reverse){
            if(compress){
                obj = new Compress(obj);
            }
            if(encrypt){
                obj = new Encrypt(obj);
            }
        }

        return obj;
    }
    private static void test(
            String testName,
            ApiResponse response) {

        System.out.println(
                "\n===================================="
        );

        System.out.println(testName);

        System.out.println(
                "===================================="
        );

        System.out.println(response.getBody());
    }


    public static void main(String[] args) {

        LegacyInternalXMLService legacyService = new LegacyInternalXMLService();
        ApiResponse response = new JsonAdapter(legacyService);

        /*
         * Test 1:
         * JSON only
         */
        ApiResponse jsonOnly =
                execute(
                        response,
                        false,
                        false,
                        false
                );

        test(
                "Test 1: JSON only",
                jsonOnly
        );


        /*
         * Test 2:
         * JSON → Encrypt
         */
        ApiResponse encrypted =
                execute(response,
                        true,
                        false,
                        false
                );

        test(
                "Test 2: Encryption only",
                encrypted
        );


        /*
         * Test 3:
         * JSON → Compress
         */
        ApiResponse compressed =
                execute(response,
                        false,
                        true,
                        false
                );

        test(
                "Test 3: Compression only",
                compressed
        );


        /*
         * Test 4:
         * JSON → Compress → Encrypt
         */
        ApiResponse compressThenEncrypt =
                execute(response,
                        true,
                        true,
                        true
                );

        test(
                "Test 4: Compress then Encrypt",
                compressThenEncrypt
        );


        /*
         * Test 5:
         * JSON → Encrypt → Compress
         */
        ApiResponse encryptThenCompress =
                execute(response,
                        true,
                        true,
                        false
                );

        test(
                "Test 5: Encrypt then Compress",
                encryptThenCompress
        );


        /*
         * Test 6:
         * Runtime configuration, similar to request parameters:
         * ?encrypt=true&compress=true
         */
        boolean encryptParameter = true;
        boolean compressParameter = true;

        // Suppose the request specifies compression first.
        boolean compressFirstParameter = true;

        ApiResponse runtimeResponse =
                execute(response,
                        encryptParameter,
                        compressParameter,
                        compressFirstParameter
                );

        test(
                "Test 6: Runtime API Parameters",
                runtimeResponse
        );
    }

}