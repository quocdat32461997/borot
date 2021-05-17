// define packages
package data;

// import dependencies
import java.util.Date;
import java.util.UUID;

public class ChatSection {
  /*
  Class ChatSection - manage every chat section that is distinguished by userid, and timestamp.
  */
  UUID sectionId = null;
  UUID userId = null;
  Date timeStamp = null;

  public ChatSection (UUID userId) {
    createSection(userId = userId);
  }

  private boolean createSection(UUID userId) {
      try {
        // unknown-user chat-section -> set to zeros
        this.userId = (userId != null) ? userId : new UUID(0,0);

        this.sectionId = UUID.randomUUID();
        this.timeStamp = new Date();
        System.out.println("Successfully created a new chat section.");
        return true;
      }
      catch (Exception e) {
        System.out.println("Failed to create a new chat section.");
        System.out.println(e);
      }
      return false;
  }
}
