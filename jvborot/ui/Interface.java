// define parent package
package ui;
// import dependencies
import java.util.Scanner;

public class Interface {
  Scanner inputObj;

  // constructur
  public Interface() {
    this.inputObj = new Scanner(System.in);
  }

  // run interface method
  public void run() {
    try {
      boolean exitFlag = false; // exit signal
      String cmdInput = new String(""); // command input

      // start of conversation
      System.out.println("Hello, I am Borot");
      while (!exitFlag) {
         /* Prompt-and-reploy here */
         cmdInput = this.inputObj.nextLine();
      }
    }
    catch (Exception e) {
      System.out.println(e);
    }
  }
}
