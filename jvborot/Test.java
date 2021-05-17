// import dependencies
import core.DialogueSystem;
import data.User;
import data.ChatSection;

public class Borot {
  public static void main(String []args) {
    try {
      // NOTI: start of program
      System.out.println("Borot is starting.");

      // NOTI: initialize user
      User tempUser = new User (
        "fishsauce40", "Dat Quoc Ngo"
      );

      // NOTI: initialize bot interface
      System.out.println("Initializing interface");
      DialogueSystem diaSys = new DialogueSystem(tempUser.getUserId());
      System.out.println("Finished initializing interface");

      // running interface
      System.out.println("Interface is running.");
      diaSys.run();
    }
    catch (Exception e) {
        System.out.println(e);
    }
  }
}
