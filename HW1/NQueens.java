// James Li
// gli38
// NQueens.java
// This program prints solutions for N-Queens problem.

import java.util.Scanner;
import java.io.*;

class NQueens{
   static int[] theQueue;     // the queue is for the input
   static int front;    // the front index of the queue
   static int rear;     // the rear index of the queue
   static int nElems;   // the number of elems in the queue

   static int[] chessArray;
   static int size;     // the size of the chess board
   static int xcoord;
   static int ycoord;
   static boolean noSol;   // check if has solution
   static int[] result = new int[10000];    // the result array
   static int nextEmpty = 0;    // the index of next empty slot in result
   static int nextElem = 0;     // the index of the next used slot

   public static void main(String[] args) throws IOException{
      if(args.length != 2){
        System.out.println("Usage: java -jar NQueens.jar <input file><output file>.");
        System.exit(1);
      }
       
      theQueue = new int[3000];
      nElems = 0;
      front = 0;
      rear = -1;
      int[] Line = new int[3];     // store the 3 data on each line

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));
      while (sc.hasNextInt())           // while has next int
         push(sc.nextInt());           // push into the queue

      while (!isEmpty()){
         for(int k=0; k<3; k++)
            Line[k] = pop();
         size = Line[0];
         xcoord = Line[1] - 1;
         ycoord = Line[2] - 1;

         chessArray = new int[size];
         for (int i=0; i<size; i++)    // initialize queens
            chessArray[i] = i;
         
         noSol = true;         // initialize noSol

         doPermutation(size);
         if (noSol){
            out.println("No solution");
            out.flush();
            continue;
         }

         for (int i=nextElem; i<nextElem+2*size; i++)
            out.print(result[i] + " ");
         out.flush();
         out.println();
         nextElem += 2*size;
      }
   }

   static void doPermutation(int newSize){
      if(newSize == 1) return;    // size is too small
      for(int j=0; j<newSize; j++){
         doPermutation(newSize-1);
         if(newSize == 2) storeAnswer();
         if(noSol == false) return;     // only print one possible sol out
         rotate(newSize);
      }
   }

   static void rotate(int newSize){
      int j;
      int position = size - newSize;       // start from the position
      int temp = chessArray[position];       // take the first element out
      for(j=position+1; j<size; j++)         // shift all elements from
         chessArray[j-1] = chessArray[j];          // position+1 to left by 1
      chessArray[j-1] = temp;           // put the first element into the last slot
   }

   static boolean isSolution(int[] A){    // test for diagonal attacks
      for(int i=0; i<size-1; i++){
         for(int j=i+1; j<size; j++){
            if (i-j == A[i]-A[j]
               || i-j == A[j]-A[i]) return false;
         }
      }
      return true;
   }

   static boolean finalAnswer(int x, int y){    // make the solution match the input
      return chessArray[x] == y; 
   }

   static void storeAnswer(){      // print out the final answer
      if(isSolution(chessArray) && finalAnswer(xcoord, ycoord)){
         for(int j=0; j<2*size; j += 2){
            noSol = false;
            result[nextEmpty++] = (j+2)/2;
            result[nextEmpty++] = chessArray[j/2]+1;
         }
      }
   }

   static void push(int j){      // push one int into the queue
      if(rear == 2999) rear = -1;
      theQueue[++rear] = j;
      nElems++;
   }

   static int pop(){     // truncanate an elem out
      int temp = theQueue[front++];
      if(front==3000) front = 0;
      nElems--;
      return temp;
   }

   static boolean isEmpty() { return nElems==0; }
}
