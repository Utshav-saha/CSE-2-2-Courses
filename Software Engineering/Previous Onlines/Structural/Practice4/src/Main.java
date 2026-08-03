public class Main {

    private static void printHeading(String title) {
        System.out.println(
                "\n========================================"
        );
        System.out.println(title);
        System.out.println(
                "========================================"
        );
    }

    public static void main(String[] args) {

        // =========================================
        // Create individual files
        // =========================================

        StorageComponent requirements =
                new Text("Requirements.txt", 10);

        StorageComponent finalReport =
                new Text("Final Report.pdf", 40);

        StorageComponent architecture =
                new Image("Architecture.png", 20);

        StorageComponent presentation =
                new Video("Presentation.mp4", 200);


        // =========================================
        // Create Documents folder
        // =========================================

        Folder documents = new Folder("Documents");

        documents.addComponent(requirements);
        documents.addComponent(finalReport);


        // =========================================
        // Create Media folder
        // =========================================

        Folder media = new Folder("Media");

        media.addComponent(architecture);
        media.addComponent(presentation);


        // =========================================
        // Create root folder
        // =========================================

        Folder projectBackup =
                new Folder("Project Backup");

        projectBackup.addComponent(documents);
        projectBackup.addComponent(media);


        // =========================================
        // Case 1: Normal hierarchy
        // =========================================

        printHeading("CASE 1: NORMAL HIERARCHY");

        projectBackup.display("");

        System.out.println(
                "Original total size: "
                        + projectBackup.getSize()
                        + " MB"
        );

        // Expected:
        // 10 + 40 + 20 + 200 = 270 MB


        // =========================================
        // Case 2: Decorated individual file
        // Restricted → Encryption → File
        // =========================================

        printHeading(
                "CASE 2: DECORATED INDIVIDUAL FILE"
        );

        StorageComponent protectedReport =
                new Restricted(
                        new Encryption(finalReport)
                );

        protectedReport.open();


        // =========================================
        // Case 3: Compressed Media folder
        // =========================================

        printHeading(
                "CASE 3: COMPRESSED MEDIA FOLDER"
        );

        StorageComponent compressedMedia =
                new Compression(media);

        compressedMedia.display("");

        System.out.println(
                "Original media size: "
                        + media.getSize()
                        + " MB"
        );

        System.out.println(
                "Compressed media size: "
                        + compressedMedia.getSize()
                        + " MB"
        );

        // Expected:
        // Original: 20 + 200 = 220 MB
        // Compressed: 220 × 0.70 = 154 MB


        // =========================================
        // Case 4: Decorate the complete root folder
        //
        // Restricted
        //   → Encryption
        //       → Compression
        //           → Project Backup
        // =========================================

        printHeading(
                "CASE 4: MULTIPLE FEATURES ON ROOT FOLDER"
        );

        StorageComponent securedBackup =
                new Restricted(
                        new Encryption(
                                new Compression(projectBackup)
                        )
                );

        System.out.println("Opening decorated backup:");

        securedBackup.open();

        System.out.println(
                "\nReported compressed size: "
                        + securedBackup.getSize()
                        + " MB"
        );

        // Expected:
        // 270 × 0.70 = 189 MB

        System.out.println(
                "\nDisplaying through decorated object:"
        );

        securedBackup.display("");


        // =========================================
        // Case 5A:
        // Restriction outside Encryption
        // =========================================

        printHeading(
                "CASE 5A: RESTRICTION OUTSIDE ENCRYPTION"
        );

        StorageComponent first =
                new Restricted(
                        new Encryption(finalReport)
                );

        first.open();


        // =========================================
        // Case 5B:
        // Encryption outside Restriction
        // =========================================

        printHeading(
                "CASE 5B: ENCRYPTION OUTSIDE RESTRICTION"
        );

        StorageComponent second =
                new Encryption(
                        new Restricted(finalReport)
                );

        second.open();
    }
}