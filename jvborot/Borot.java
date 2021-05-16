// import dependencies
import ui.Interface;
//.ChatInterface;

public class Borot {
  public static void main(String []args) {
    try {
      // NOTI: start of program
      System.out.println("Borot is starting.");

      // NOTI: initialize bot interface
      System.out.println("Initializing interface");
      Interface interfaceObj = new Interface();
      System.out.println("Finished initializing interface");

      // running interface
      System.out.println("Interface is running.");
      interfaceObj.run();
    }
    catch (Exception e) {
        System.out.println(e);
    }
  }
}
