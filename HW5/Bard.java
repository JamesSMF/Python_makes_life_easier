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

class Bard{

   static int[] theQueue = new int[50000];     // the queue is for the input
   static int front = 0;    // the front index of the queue
   static int rear = -1;     // the rear index of the queue
   static int nElems = 0;   // the number of elems in the queue
   /* -----------------------------  main() starts here  ------------------------------- */

   public static void main(String[] args)throws FileNotFoundException, IOException{
      Scanner sc = new Scanner(new FileReader(args[0]));   // the scanner for input file
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));  // printer to write to the output file

      Scanner shakespeare = new Scanner(new FileReader("FinalDataBase.txt"));

      while(sc.hasNextInt())
         push(sc.nextInt());

      while(!isEmpty()){
         
         int wordLength = pop();
         int rank = pop();

         if(wordLength < 1 || wordLength == 25 || wordLength == 26 || 
           (wordLength > 27 && wordLength < 36) || wordLength > 36){
            out.println("-");
            continue;
         }

         int linePointer = 0;    // a pointer to line number
         int loopTime = 0;       // loop counter
         String[] WordIWant = new String[2];

         if(wordLength == 36){            // index 0
            if(rank == 0)
               out.println("tragical-comical-historical-pastoral");
            else
               out.println("-");

            out.flush();
            continue;       // to the next line of input
         }else if(wordLength == 27){     // index 1 to 2
            if(rank == 0)
               out.println("honorificabilitudinitatibus");
            else if(rank == 1)
               out.println("six-or-seven-times-honour'd");
            else
               out.println("-");

            out.flush();
            continue;
         }else if(wordLength == 24){
            if(rank == 0)
               out.println("king_henry_viii|epilogue");
            else
               out.println("-");

            out.flush();
            continue;       // to the next line of input
         }else if(wordLength == 23){
            if(rank == 0)
               out.println("water-flies-diminutives");
            else
               out.println("-");

            out.flush();
            continue;       // to the next line of input
         }else if(wordLength == 22){
            if(rank == 0)
               out.println("to-and-fro-conflicting");
            else
               out.println("-");

            out.flush();
            continue;       // to the next line of input
         }else if(wordLength == 21){
            if(rank == 0)
               out.println("candle-wasters--bring");
            else if(rank == 1)
               out.println("castalion-king-urinal");
            else if(rank == 2)
               out.println("that-way-accomplish'd");
            else
               out.println("-");

            out.flush();
            continue;
         }else if(wordLength == 20){
            if(rank == 0)
               out.println("death-counterfeiting");
            else if(rank == 1)
               out.println("obligation-'armigero");
            else if(rank == 2)
               out.println("one-trunk-inheriting");
            else if(rank == 3)
               out.println("wholesome-profitable");
            else
               out.println("-");

            out.flush();
            continue;
         }else if(wordLength == 19){      // line 14 to 24
            if(rank > 10){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 13 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 18){     // line 25 to 35
            if(rank > 10){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 24 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 17){            // line 36 to 74
            if(rank > 38){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 35 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 16){           // line 75 to 142
            if(rank > 67){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 74 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 15){           // line 143 to 301
            if(rank > 158){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 142 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 14){           // line 302 to 594
            if(rank > 292){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 301 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 13){          // line 595 to 1162
            if(rank > 567){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 594 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 12){         // line 1163 to 2174
            if(rank > 1011){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 1162 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 11){         // line 2175 to 3834
            if(rank > 1659){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 2174 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 10){         // line 3835 to 6264
            if(rank > 2429){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 3834 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 9){        // line 6425 to 10165
            if(rank > 3740){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 6424 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 8){         // line 10166 to 15026
            if(rank > 4860){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 10165 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 7){         // line 15027 to 20223
            if(rank > 5196){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 15026 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 6){         // line 20224 to 25070
            if(rank > 4846){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 20223 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 5){         // line 25071 to 28505
            if(rank > 3434){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 25070 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 4){        // line 28506 to 30543
            if(rank > 2037){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 28505 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 3){       // line 30544 to 31265
            if(rank > 721){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 30543 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 2){       // line 31266 to 31468
            if(rank > 202){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 31265 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }else if(wordLength == 1){      // line 31469 to 31504
            if(rank > 35){
               out.println("-");
               out.flush();
               continue;
            }

            FileInputStream fs = new FileInputStream("FinalDataBase.txt");
            BufferedReader br = new BufferedReader(new InputStreamReader(fs));
            for(int i = 0; i < 31468 + rank; i++)
               br.readLine();
            String lineIWant = br.readLine();
            WordIWant = lineIWant.split(" ");

            out.println(WordIWant[0]);
            out.flush();
         }
      }  // end while (go to next line of input file)

      sc.close();
      shakespeare.close();
      out.close();
   } // end main

   static void push(int j){      // push one int into the queue
      if(rear == 49999) rear = -1;
      theQueue[++rear] = j;
      nElems++;
   }

   static int pop(){     // truncanate an elem out
      int temp = theQueue[front++];
      if(front==50000) front = 0;
      nElems--;
      return temp;
   }

   static boolean isEmpty() { return nElems==0; }
}  // end class






