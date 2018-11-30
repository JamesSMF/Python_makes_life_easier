import java.util.Scanner;
import java.io.*;

class Reverter{
   public static void main(String[] args) throws IOException{
      int[] numberArray = new int[31492];
      String[] wordArray = new String[31492];
      int freqPointer = 0;
      int wordPointer = 0;

      Scanner sc = new Scanner(new FileReader("file"));
      PrintWriter out = new PrintWriter(new FileWriter(args[0]));

      while(sc.hasNextLine()){
         int wordFreq;
         String theWord;

         try{
            theWord = sc.next();
            wordFreq = sc.nextInt();
         }catch(Exception e1){
            break;
         }

         wordArray[wordPointer++] = theWord;
         numberArray[freqPointer++] = wordFreq;
      }

      while(wordPointer >= 0){
         String newWord = wordArray[wordPointer--];
         int newFreq = numberArray[freqPointer--];

         out.println(newWord + " " + newFreq);
      }
   }
}
