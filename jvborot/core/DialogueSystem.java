// define parent package
package core;

// import dependencies
import java.util.Scanner;
import java.util.*;

import data.ChatSection;
import nlp.*;

public class DialogueSystem {
  Scanner inputObj;
  String botText = new String("Hello, I am Borot");
  String userText = new String();
  ChatSection chatSection = null;

  public DialogueSystem(UUID userId) {
    /*
    Constructor of Interface class
    Args:
      userId : UUID object
        Unique user id
    Returns: None
    */
    this.inputObj = new Scanner(System.in);
    this.chatSection = new ChatSection(userId);
  }

  private String botSay () {
    /*
    botSay - function to ask and reply against users' input
    Args: None
    Returns:
      botText - String
        Bot prompt and response
    */

    // generate response
    this.botText = "";
    // print prompt text
    System.out.println(this.botText);

    // add propt text
    this.chatSection.addText(this.botText);

    return this.botText;
  }

  private String userSay() {
    /*
    userSay - function to prompt user input
    Args: none
    Returns:
      userText - String
        User input
    */
    // prompt user input
    this.userText = this.inputObj.nextLine();

    // add text
    this.chatSection.addText(userText);

    return this.userText;
  }
  public void run() {
    /*
    run - function to run promt-and-rpely operations
    Args: None
    Returns: None
    */
    try {
      // define variables
      boolean exitFlag = false; // exit signal

      /*
      prompt-and-reply loop
      */
      // print start prompt text
      System.out.println(botText);

      // core operations
      while (!exitFlag) {
        /* Prompt-and-reploy here */
        // user say
        userSay();

        // bot say
        botSay();
      }
    }
    catch (Exception e) {
      System.out.println(e);
    }
  }
}
