import java.io.*;
import java.util.Scanner;

class Coordinate{
   public int x;    // x-coordinate
   public int y;    // y-coordinate

   public Coordinate(int x, int y){   // constructor
      this.x = x;
      this.y = y;
   }
}

class NQueens{
   static int size;     // the size of the chess board
   static Coordinate[] chessArray;
   static int xcoord;
   static int ycoord;
   static boolean noSol = true;   // check if has solution

   public static void main(String[] args){
      Scanner sc = new Scanner(System.in);
      size = sc.nextInt();        // get the size
      xcoord = sc.nextInt() - 1;      // get the x-coord
      ycoord = sc.nextInt() - 1;      // get the y-coord

      chessArray = new Coordinate[size];
      for (int i=0; i<size; i++)    // initialize queens
         chessArray[i] = new Coordinate(i, i);

      doPermutation(size);
      if (noSol) System.out.println("No solution");
   }

   static void doPermutation(int newSize){
      if(newSize == 1) return;    // size is too small
      for(int j=0; j<newSize; j++){
         doPermutation(newSize-1);
         if(newSize == 2) printAnswer();
         rotate(newSize);
      }
   }

   static void rotate(int newSize){
      int j;
      int position = size - newSize;       // start from the position
      int temp = chessArray[position].y;       // take the first element out
      for(j=position+1; j<size; j++)         // shift all elements from
         chessArray[j-1].y = chessArray[j].y;          // position+1 to left by 1
      chessArray[j-1].y = temp;           // put the first element into the 
                                     // last slot
   }

   static boolean isSolution(Coordinate[] A){    // test for diagonal attacks
      for(int i=0; i<size-1; i++){
         for(int j=i+1; j<size; j++){
            if (A[i].x-A[j].x == A[i].y-A[j].y
               || A[i].x-A[j].x == A[j].y-A[i].y) return false;
         }
      }
      return true;
   }

   static boolean finalAnswer(int x, int y){    // make the solution match the input
      return chessArray[x].y == y; 
   }

   static void printAnswer(){      // print out the final answer
      if(isSolution(chessArray) && finalAnswer(xcoord, ycoord)){
         for(int j=0; j<size; j++){
            noSol = false;
            System.out.print(chessArray[j].x+1 + " ");
            System.out.print(chessArray[j].y+1 + " ");
         }
      System.out.println();
      }
   }
}



