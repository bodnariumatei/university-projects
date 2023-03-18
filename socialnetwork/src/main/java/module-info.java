module com.sn.socialnetwork {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires java.sql;

    opens com.sn.socialnetwork to javafx.fxml;
    exports com.sn.socialnetwork;

    opens com.sn.socialnetwork.ui.gui to javafx.fxml;
    exports com.sn.socialnetwork.ui.gui;
}