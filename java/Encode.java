import java.io.*;
import java.lang.Math;

class Encode{
   public static void main(String[] args) throws IOException{
      System.out.print("Enter the number to be encoded: ");
      System.out.flush();
      double input = getDouble();    // get the input
      int fstBit = (input > 0 ? 0 : 1);

      // split input into decimal and integer parts
      String inputString = String.valueOf(input);
      int index = inputString.indexOf(".");
      int intPart = Integer.parseInt(inputString.substring(0,index));
      String rep = inputString.substring(index).replace(".","");
      int decPart = Integer.parseInt(rep);

      // calculates for binary for each part
      int[] bInt = decToBinary(intPart, 4);
      int[] bDec = decPartBin(decPart, 4);
      int bias = bInt.length + 126;
      int[] Bbias = decToBinary(bias, 8);

      // combine and get a binary array
      int[] combArray = combine(bInt, bDec);
      printArray(bInt);
      // printArray(bDec);
      combArray = combine(Bbias, combArray);
      // printArray(combArray);
      int [] temp = {fstBit};
      combArray = combine(temp, combArray);
      // printArray(combArray);

      // convert the combined binary array to an array of hex
      char[] hex = new char[8];
      int slot = 0;
      char ans = '0';
      for(int i=0; i<32; i++){
         if((i+1)%4==0){
            int newInt = combArray[i-3] * 8 + combArray[i-2] * 4 + combArray[i-1] * 2 + combArray[i];
            // System.out.println(newInt);
            if(newInt > 9){
               switch(newInt){
                  case 10:
                     ans = 'A';
                     break;

                  case 11:
                     ans = 'B';
                     break;

                  case 12:
                     ans = 'C';
                     break;

                  case 13:
                     ans = 'D';
                     break;

                  case 14:
                     ans = 'E';
                     break;
                
                  case 15:
                     ans = 'F';
                     break;
               }   // end of switch
               hex[slot++] = ans;
            }else{
               hex[slot++] = (char) (newInt + '0');
               // System.out.println(ans);
            }  // end of String conversion
         }
      }
      printArray(hex);
   }

   static String getString() throws IOException{
      InputStreamReader isr = new InputStreamReader(System.in);
      BufferedReader br = new BufferedReader(isr);
      String s = br.readLine();
      return s;
   }

   static double getDouble() throws IOException{
      String s = getString();
      return Double.parseDouble(s);
   }


   static int[] decToBinary(int n, int len){
      int[] binaryNum = new int[len];
   
      while (n > 0){ 
         // storing remainder in binary array 
         if(len==0) break;
         binaryNum[--len] = n % 2; 
         n = n / 2;
      }
      
      return binaryNum;  
   }

   static int[] decPartBin(int n, int len){
      int[] binaryNum = new int[len];

      int whatever = 10;
      while()

      double target = 0.5 * Math.pow(10,len);
      // System.out.println(target);
      int count = 0;
      while(n>0){
         while(n < target){
            target /= 2;
            binaryNum[count++] = 0;
         }

         n -= target;
         binaryNum[count++] = 1;
      }

      return binaryNum;
   }

   static int[] combine(int[] a, int[] b){
      int length = a.length + b.length;
      int[] result = new int[length];
      System.arraycopy(a, 0, result, 0, a.length);
      System.arraycopy(b, 0, result, a.length, b.length);
      return result;
   }

   static void printArray(char[] theArray){
      for(int i=0; i<theArray.length; i++)
         System.out.print(theArray[i]);
      System.out.println();
   }

   static void printArray(int[] theArray){
      for(int i=0; i<theArray.length; i++)
         System.out.print(theArray[i]);
      System.out.println();
   }

}

