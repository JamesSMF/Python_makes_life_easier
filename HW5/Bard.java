/* James Li                                                               */
/* gli38                                                                  */
/* HW5                                                                    */
/* Bard.java                                                              */
/* This program does vocabulary analysis of William Shakespears's work    */
/* ---------------------------------------------------------------------- */
/* This program parses Shakespeare's work into a hash table. The hash     */
/* table has the structure <the_word_Object, frequency_of_the_word>. The  */
/* input file should have two ints on each line. The first one is the     */
/* length of the word and the second one is the rank of the frequency.    */
/* ---------------------------------------------------------------------- */
/* ----------------------------- Class ---------------------------------- */
/* -------------------------- Descriptions ------------------------------ */
/* ---------------------------------------------------------------------- */
/* In the class Word, there are three variables in its field. The name of */
/* the word, the length of the word, and the frequency of the word. The   */
/* length is important because we will use this to search for the word    */
/* afterwards, and it is the real key value.                              */
/* ---------------------------------------------------------------------- */
/* The class Bard contains the main function. It first parses the work as */
/* a whole into the table. Then it turns to the input file and solve one  */
/* line at a time. The result would be written into the output file.      */
/* ---------------------------------------------------------------------- */
/*                              _ooOoo_                                   */
/*                             o8888888o                                  */
/*                             88" . "88                                  */
/*                             (| *_* |)                                  */
/*                             O\  =  /O                                  */
/*                         _____/`---'\_____                              */
/*                       .'   \\|     |//   `.                            */
/*                      /   \\|||  :  |||//   \                           */
/*                     /   _||||| -:- |||||_   \                          */
/*                     |    | \\\  -  /// |    |                          */
/*                     |    |  ''\---/''  |    |                          */
/*                     \  .-\__   `-`   __/-.  /                          */
/*                   ___`. .'  / --.-- \  `. .'___                        */
/*                ."" '<  `.___\ _<|>_ /___.'  >' "".                     */
/*               | | :  `- \`.;`\ ___ /` ;.`/ - ` : | |                   */
/*               \  \ `- .  \_ __\   /__ _/   . -' /  /                   */
/*         ======`-.______ `.___\_____/___.' ______.-'======              */
/*                              `=---='                                   */
/* ---------------------------------------------------------------------- */
/*      NN      NN     OOOO          BBBBB     UU    UU      GGGGG        */
/*     NNNN    NN    OO    OO        BB  BB    UU    UU    GG             */
/*    NN  NN  NN    OO     OO        BBBBBB    UU    UU   GG   GGGGG      */
/*   NN    NNNN     OO    OO         BB   BB   UU    UU    GG   GG G      */
/*  NN      NN        OOOO           BBBBBB    UUUUUUUU     GGGGG  G      */

/* ---------------------------------------------------------------------- */
/* ------------------------ Code starts here ---------------------------- */
/* ---------------------------------------------------------------------- */

import java.util.*;
import java.io.*;

class Word{
/* ------------------------------------------------------------------------------- */
/* for information protection, this is a private field. This avoids user to change */
/* word or frequency directly.                                                     */
   
   private String word;     // the name of the word
   private int length;      // the frequency of the word
   private int finalFreq;   // the final frequency of the word

/* -------------------------------- Constructor ---------------------------------- */

   public Word(String w){
      word = w;
      length = calculateLen();
      finalFreq = 0;
   }


   /* -------------------------------------- */
   /* calculate the ascii value for the word */
   /* asciiCalculate()                       */

   public static int asciiCalculate(String word){
      int sum = 0;
      for(int i=0; i<word.length(); i++){
         sum += word.charAt(i);
      }
      return sum;
   }


   /* -------------------------------- */
   /* calculate the length of the word */
   /* calculateLen()                   */

   public int calculateLen(){
      int len = 0;
      for(int i=0; i<word.length(); i++) len++;
      return len;
   }


   /* ----------------------------- */
   /* get the frequency of the word */
   /* getFreq()                     */

   public int getFreq(){
      return finalFreq;
   }
   
   public int getLen(){
      return length;
   }


   /* ------------------------ */
   /* get the name of the word */
   /* getWord()                */

   public String getWord(){
      return word;
   }


   /* ----------------------------------- */
   /* set the final frequency of the word */
   /* setFreq()                           */

   public void setFreq(int freq){
      finalFreq = freq;
   }

   public void setWord(String str){
      word = str;
   }

   public boolean equals(Object x){
      boolean eq = false;
      Word theWord;

      if(x instanceof Word){
         theWord = (Word) x;
         eq = (this.word.equals(theWord.word));
      }
      return eq;
   }

   public int hashCode(){
      int totalAscii = asciiCalculate(this.word);
      int hash = totalAscii % 26;
      return hash;
   }
}

class Bard{
   /* ---------------------------------------------------------------------------------- */
   /* global variable: Hashtable table. This table serves as a dictionary to store len   */
   /* of words and corresponding word objects in shakespeare's work.                     */

   static Hashtable<Word, Integer> table = new Hashtable<>();

   /* Hashtable<Length_Of_The_Word, Word_Object> table                                   */
   /* -----------------------------  main() starts here  ------------------------------- */

   static Word[] wordArray;   // a new array to store words with length == wordLength
   static int index;                      // index of the array above

   public static void main(String[] args)throws FileNotFoundException, IOException{
      Scanner sc = new Scanner(new FileReader(args[0]));   // the scanner for input file
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));  // printer to write to the output file

      while(sc.hasNextLine()){
         Scanner shakespeare = new Scanner(new FileReader("FinalDataBase.txt"));
         int wordLength;
         int rank;

         wordLength = sc.nextInt();   // the first number in that line is the length of the word
         rank = sc.nextInt();         // the second number is the rank of frequency
         if(wordLength > 19 || wordLength < 1){     // there is no word with length > 19
            out.println("-");
            continue;
         }

         int linePointer = 0;    // a pointer to line number
         int loopTime = 0;



         if(wordLength == 19){            // index 0 to 10
            while(shakespeare.hasNextLine()){
               if(loopTime == rank) break;
               loopTime++;
               continue;
            }

            if(loopTime > 10){ 
               out.println("-");
               continue;    // to the next line of input file
            }

            String theWord = shakespeare.next();
            out.println(theWord)
         }else if(wordLength == 18){     // index 11 to 23
            linePointer = 11;
            for(int i=0; i<11; i++) shakespeare.nextLine();
            while(shakespeare.hasNextLine()){
               if(loopTime == rank) break;
               loopTime++;
               continue;
            }
         }

      }  // end while (go to next line of input file)

      




      /* --------------------------------------------------------------------- */
      /* This part parses all the words in shakespeare.txt into the hash table */   

      while(shakespeare.hasNextLine()){
         String line = shakespeare.nextLine().trim() + " ";    // input the whole line

      /* ------------------------------------------- */

         String[] token = line.split("\\s+");       // put into array splited by " "
         Word[] parseToken = new Word[token.length];   // a Word array
         for(int i=0; i<token.length; i++){        // loop through the string array
            parseToken[i] = new Word(token[i]);

            if(table.containsKey(parseToken[i])){ // if this word object has already existed
               int currFreq = table.get(parseToken[i]);   // get the current frequency of the word
               table.replace(parseToken[i], currFreq, ++currFreq);

               /* replace the old frequency with the new one (after incrementation) */
               /* increse the frequency by 1                                        */

            }else{                                       // if it is a new word
               table.put(parseToken[i], new Integer(1)); // put a new word with frequency = 1
            } // end if-else   
         }  // end for

      /* To this point, all the words on the current line are stored into the hash table */
      }  // end while(shakespeare.hasNextLine())

   /* To this point, all the words in shakespeare's masterpiece are stored into the hash table */
   /* --------------------------------------------------------------------------------------- */

      Scanner sc = new Scanner(new FileReader(args[0]));   // the scanner for input file
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));  // printer to write to the output file

      while(sc.hasNextLine()){ // while the input file does not hit the end
         int wordLength;
         int rank;
         wordArray = new Word[1024];
         index = 0;

         try{
            wordLength = sc.nextInt();   // the first number in that line is the length of the word
            rank = sc.nextInt();         // the second number is the rank of frequency
         }catch(NoSuchElementException e1){
            break;
         }

         Enumeration<Word> enumKey = table.keys();        // declare an iterator used to find the word
         while (enumKey.hasMoreElements()){    // loop through the entire hash table
            Word key = enumKey.nextElement();   // go to the next element in the hash table
            key.setFreq(table.get(key));    // get the freq of the word and store it also in the word obj
            if(key.getLen() == wordLength){        // if the word is of the correct length
               wordArray[index++] = key;      // store it into the array
               System.out.println(wordArray[index].getWord() + " " + wordArray[index].getFreq());
            }
         }  // end while

      /* To this point, all the words with correct length has been stored into the array */

         quickSort(0, index-1);    // apply quick sort to the array

      /* now the array is sorted by the frequency (but still not alphabetical) */

/*
 *
 *          int freqRank = 0;         // the rank of the frequency
 *                   boolean hasAnswer = false;
 *                            Word currentWord = wordArray[0];
 *                                     int last = -100;
 *                                              for(int i=index-2; i>=0; i--){
 *                                                          if(wordArray[i].getFreq() != wordArray[i+1].getFreq()){
 *                                                                         if(last < 0){
 *                                                                                           insertionSort(i+1, index-1);
 *                                                                                                          }else{
 *                                                                                                                            System.out.println(wordArray[i+1].getWord() + " " + wordArray[last].getWord());
 *                                                                                                                                              insertionSort(i+1, last);
 *                                                                                                                                                             }
 *                                                                                                                                                                            last = i;
 *                                                                                                                                                                                        }  // end outer if
 *                                                                                                                                                                                                 }  // end for
 *
 *                                                                                                                                                                                                 */

         for(int i=0; i<index; i++){
            out.println(wordArray[i].getWord() + " " + wordArray[i].getFreq());
            out.flush();
         }
      }  // end while (go to the next line of input)

   /* ---------------------------------------------- */
   /* close the Scanner and PrintWriter after using. */

      shakespeare.close();
      sc.close();
      out.close();

   /* ---------------------------------------------- */
   }


   static int asciiCalculate(String word){
      int sum = 0;
      for(int i=0; i<word.length(); i++){
         sum += word.charAt(i);
      }
      return sum;
   }
}




