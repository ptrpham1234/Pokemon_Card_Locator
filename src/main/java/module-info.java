module org.openjfx.pokemon_ui_fx {
    requires javafx.controls;
    requires javafx.fxml;
    requires org.jsoup;
    requires java.desktop;


    opens org.openjfx.pokemon_ui_fx to javafx.fxml;
    exports org.openjfx.pokemon_ui_fx;
}