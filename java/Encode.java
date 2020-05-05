import java.io.*;

public class Encode{
   // Get 32-bit IEEE 754 format of the decimal value  
   private static String GetHex32( float value ) throws IOException{  
      int intBits = Float.floatToIntBits(value);     // convert to IEEE 756 shit notation
      System.out.print("Choose output type: (hex, binary, oct, dec) ");
      String outputOption = getString();
      String hexS = String.valueOf(intBits);
      switch(outputOption){
         case "hex":
            hexS = Integer.toHexString(intBits);
            break;
         case "oct":
            hexS = Integer.toOctalString(intBits);
            break;
         default:
            break;
      }
      return hexS;
   }

   private static String getString() throws IOException{
      InputStreamReader isr = new InputStreamReader(System.in);
      BufferedReader br = new BufferedReader(isr);
      return br.readLine();
   }
 
   /**
   * @param args
   */
   public static void main(String[] args) throws IOException{
      System.out.print("Please enter the number to Encode: ");
      String input = getString();
      float f = Float.valueOf(input.trim()).floatValue();
      String str = GetHex32(f);
      System.out.print( "Encoding result of " + input + ": ");  
      System.out.println(str);
   }
}
