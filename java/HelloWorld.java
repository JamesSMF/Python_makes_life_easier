abstract class AbstractPrint{
   protected String n;

   abstract void RevPrint();

   void reassign(String n){
      this.n = n;
   }
}

class HW extends AbstractPrint{
   HW(String n){
      this.n = n;
   }

   void RevPrint(){
      for(int i=n.length()-1; i>=0; i--)
         System.out.print(n.charAt(i));
      System.out.println();
   }
}

public class HelloWorld{
   public static void main(String[] args){
      HW a = new HW("!dlroW olleH");
      a.RevPrint();
      a.reassign(".9102 yppaH");
      a.RevPrint();
   }
}
