package org.openjfx.pokemon_ui_fx;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import org.jsoup.nodes.Element;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import java.awt.Desktop;
import java.net.URI;

public class WindowController implements Initializable {

    @FXML
    private ChoiceBox<String> setChooser;
    @FXML
    private Label totalSetNumLabel;
    @FXML
    private TextField numTextArea;
    @FXML
    private TextArea outputArea;
    @FXML
    private Hyperlink setLinkLabel;

    WebCrawler crawler;


    @Override
    public void initialize(URL location, ResourceBundle resources) {

        crawler = new WebCrawler();
        ArrayList<Element> list = crawler.getSetList();

        setChooser.setValue("Select desired set:");
        setChooser.getItems().addAll(crawler.toStringList(list));
        setChooser.setOnAction(this::onSetSelect);

        numTextArea.textProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observable, String oldValue, String newValue) {
                if (!newValue.matches("\\d*")) {
                    numTextArea.setText(newValue.replaceAll("\\D", ""));
                }
            }
        });
    }

    /*****************************************************************************************************************
     * Functions:           onSetSelect
     * Author:              Peter Pham
     * Date Started:        11/19/2022
     * Description:
     * Gets the card count per set and displays it on the screen using the label
     * Parameters:
     *      e         ActionEvent      Specified the details of the
     *****************************************************************************************************************/
    public void onSetSelect(ActionEvent e) {
        Desktop desktop = Desktop.getDesktop();
        int total = crawler.getCardNumber(setChooser.getValue());
        totalSetNumLabel.setText("/ " + total);

    }

    /*****************************************************************************************************************
     * Functions:           onCalcClick
     * Author:              Peter Pham
     * Date Started:        11/19/2022
     * Description:
     * Initializes the
     * Parameters:
     *      e         ActionEvent      Specified the details of the
     *****************************************************************************************************************/
    @FXML
    protected void onCalcClick() {


        int userInput = Integer.parseInt(numTextArea.getText());

        int pageNum = (int) Math.floor(((double) userInput / 9) + 1);
        int index;
        String side;
        String output;

        if (pageNum % 2 == 0)
            side = " (Left)";
        else
            side = " (Right)";

        index = (userInput - ((pageNum - 1) * 9));

        output = "Your card is located at:\n\n" +
                "Page Num: " + pageNum + side + "\n" +
                "Index: " + index;

        outputArea.setText(output);

    }

    public void onLinkClick (ActionEvent e) throws URISyntaxException, IOException {
        Desktop desktop = Desktop.getDesktop();
        desktop.browse(new URI(crawler.getSetURL(setChooser.getValue())));
    }

}