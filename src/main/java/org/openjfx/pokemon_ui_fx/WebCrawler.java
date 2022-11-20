package org.openjfx.pokemon_ui_fx;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.IOException;
import java.util.ArrayList;

public class WebCrawler {



    static String baseUrl = "https://www.pokellector.com";
    static String scrapeURL = baseUrl + "/sets";

    private ArrayList<Element> setList;
    private ArrayList<String> setName;
    private final int[] setTotal;
    private final String[] setUrl;



    /*****************************************************************************************************************
     * Functions:           WebCrawler constructor
     * Author:              Peter Pham
     * Date Started:        11/19/2022

     * Description:
     * Initializes the

     * Parameters:
     *      username        I/P         string      The username that the user has inputted.
     *      password        O/P         string      The password that the user has inputted.
    *****************************************************************************************************************/
    public WebCrawler() {
        updateSetList();
        this.setTotal = new int[this.setList.size()];
        this.setUrl = new String[this.setList.size()];
    }

    /*****************************************************************************************************************
     * Functions:           getters
     * Author:              Peter Pham
     * Date Started:        11/19/2022

     * Description:
     * Gets the needed variables
     *****************************************************************************************************************/
    public ArrayList<Element> getSetList() { return this.setList; }

    public ArrayList<String> toStringList(ArrayList<Element> elements) {

        ArrayList<String> returnArr = new ArrayList<>();
        for (Element element : elements) {
            returnArr.add(element.text());
        }
        return returnArr;
    }

    /*****************************************************************************************************************
     * Functions:           getSetList
     * Author:              Peter Pham
     * Date Started:        11/19/2022

     * Description:
     * Grabs the names of the sets on the website

     * Parameters:
     *      username        I/P         string      The username that the user has inputted.
     *      password        O/P         string      The password that the user has inputted.
     *****************************************************************************************************************/
    public int getCardNumber(String setName) {

        int i = setSearch(setName);
        String url;
        Document doc;
        int total;

        if (setTotal[i] != 0)
            return setTotal[i];

        url = baseUrl + this.setName.get(i);
        setUrl[i] = url;

        try {

            doc = Jsoup.connect(url).get();

            total = doc.select("div.card").size();

            setTotal[i] = total;

            return total;

        } catch (IOException e) {
            e.printStackTrace();
        }

        return -1;
    }

    public String getSetURL(String name) {

        String url;
        int index = setSearch(name);

        return setUrl[index];
    }

    /*****************************************************************************************************************
     * Functions:           getSetList
     * Author:              Peter Pham (pxp180041)
     * Date Started:        11/19/2022

     * Description:
     * Updates the set

     * Parameters:
     *      username        I/P         string      The username that the user has inputted.
     *      password        O/P         string      The password that the user has inputted.
     *****************************************************************************************************************/
    private void updateSetList() {
        Document doc;
        ArrayList<Element> buttons;
        ArrayList<String> nameList = new ArrayList<>();

        try {

            doc = Jsoup.connect(scrapeURL).get();

            buttons = doc.select("a.button");

            this.setList = buttons;

            for (Element setName: buttons) {
                nameList.add(setName.attr("href"));
            }

            this.setName = nameList;

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private int setSearch(String name) {

        // loops through and searches for the set name
        for (int i = 0; i < setList.size(); i++) {
            if (name.equals(setList.get(i).text())) {
                return i;
            }
        }

        return -1;
    }




}
