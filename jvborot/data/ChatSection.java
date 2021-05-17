// define packages
package data;

// import dependencies
import java.util.*;

public class ChatSection {
  /*
  Class ChatSection - manage every chat section that is distinguished by userid, and timestamp.
  */
  private UUID sectionId = null;
  private UUID userId = null;
  private Date timeStamp = null;
  private ArrayList<String> texts = null;

  public ChatSection (UUID userId) {
    // create a new section
    createSection(userId = userId);

    // initalize empty array of texts
    this.texts = new ArrayList<String>();
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

  public void addText(String text) {
    this.texts.add(text); // add text
  }

  public UUID getSectionId () {
    return this.sectionId;
  }

  public Date getTimeStamp () {
    return this.timeStamp;
  }

  public ArrayList<String> getTexts () {
    return this.texts;
  }
}
