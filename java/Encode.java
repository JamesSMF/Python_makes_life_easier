import java.io.*;

public class Encode{
   // Get 32-bit IEEE 754 format of the decimal value  
   private static String GetBinary32( float value ) throws IOException{  
      int intBits = Float.floatToIntBits(value); 
      String binary = Integer.toBinaryString(intBits);
      return binary;
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
      String str = GetBinary32(f);
      int decimal = Integer.parseInt(str,2);
      String hexStr = Integer.toString(decimal,16);
      System.out.print( "Encoding result of " + input + ": ");  
      System.out.println(hexStr);
   }
}
