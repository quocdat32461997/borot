// define parent package
package data;

// import dependencies
import java.util.UUID;

public class User {
  /*
  Class User -  manage User object
  */
  String userName = new String();
  String name = new String();
  UUID userId = null;

  public User(String userName, String name) {
    // register user
    register(userName = userName, name = name);
  }

  private boolean register(String userName, String name) {
    try {
      this.userName = userName;
      this.name = name;
      this.userId = UUID.randomUUID();
      System.out.println("Successfully registered user.");
      return true;
    }
    catch (Exception e) {
      System.out.println("Failed to register user.");
      System.out.println(e);
    }

    return false;
  }
}
