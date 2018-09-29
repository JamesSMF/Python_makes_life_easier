//-----------------------------------------------------------------------------
// James Li
// gli38
// HelloUser2.java
// Prints greeting to stdout, then prints out some environment information.
//-----------------------------------------------------------------------------


class HelloUser2{
   public static void main(String[] args){
      String userName = System.getProperty("user.name");
      System.out.println("Hello "+userName);
   }
}
