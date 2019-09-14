import java.util.*; 
  
public class ArrayListEg{ 
   public static void main(String[] args) { 
  
      // create a ArrayList String type 
      // and Initialize an ArrayList with asList() 

      ArrayList<String> arr = new ArrayList<String> (Arrays.asList("Holy", "shit", "it", "works")); 

      arr.add("I");
      arr.add("Hello");
      arr.add("How");
      arr.add("Are");
      arr.add("You");
      // print ArrayList 
      System.out.println("ArrayList : " + arr); 

      // check if contains a certain string
      boolean ans = arr.contains("Are");
      System.out.println(ans);

      int index = arr.indexOf("shit");
      arr.remove("I");
      arr.remove(1);     // remove the item with index 1

      System.out.println("ArrayList : " + arr);  
   } 
} 
