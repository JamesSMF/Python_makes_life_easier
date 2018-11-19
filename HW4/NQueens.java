import java.util.Scanner;
import java.io.*;

class Stack{
   public int top;
   public int bottom;
   public int[] theStack;
   public int size;

   public Stack(int maxSize){
      size = maxSize;
      theStack = new int[size];
      top = -1;
      bottom = 0;
   }

   public boolean isEmpty() { return bottom > top; }
   public boolean isEmpty(int a) { return top < 0; }
   public void push(int index, int val) {
      theStack[index] = val;
      top++;
   }
   public void push(int val) { theStack[++top] = val; }
   public int pop() { return theStack[bottom++]; }
   public int popEnd() { return theStack[top--]; }
   public int peek() { return theStack[top]; }   // just peek, but do not delete
   public int peekArbitrary(int index){ return theStack[index]; }
}

class NQueens{
   static int[] chessArray;
   static int size;     // the size of the chess board
   static int[] xcoord;
   static int[] ycoord;
   static boolean noSol;   // check if has solution
   static int[] result = new int[10000];    // the result array
   static int nextEmpty = 0;    // the index of next empty slot in result
   static int nextElem = 0;     // the index of the next used slot

   public static void main(String[] args) throws IOException{
      if(args.length != 2){
        System.out.println("Usage: java -jar NQueens.jar <input file><output file>.");
        System.exit(1);
      }

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));

      while (sc.hasNextLine()){           // while has next line
         String line = sc.nextLine().trim() + " ";    // input the whole line
         String[] token = line.split("\\s+");       // put into array splited by " "
         int[] lineData = new int[token.length];
         for(int i=0; i<token.length; i++){
            lineData[i] = Integer.parseInt(token[i]);    // parse the string into int
         }

         size = lineData[0];

      /* Now split the input into xcoord[] and ycoord[] */   
         int index = 0;
         xcoord = new int[(lineData.length - 1) / 2];
         ycoord = new int[xcoord.length];
         while(index < xcoord.length){
            xcoord[index] = lineData[2 * index + 1] - 1;
            ycoord[index] = lineData[2 * index + 2] - 1;
            index ++;
         }

         chessArray = new int[size];
         for (int i=0; i<size; i++)    // initialize queens
            chessArray[i] = i;
         
         noSol = true;         // initialize noSol

         if(size == 1){
            out.println("1 1");
            out.flush();
            continue;
         }

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
      }  // end while   (proceed to the next line)
   }

   static long fac(int n){      // factorial of n
      Stack numberStack = new Stack(n);
      while(n >= 1) numberStack.push(n--);
      int sum = 1;
      while(!numberStack.isEmpty(1)){
         sum *= numberStack.popEnd();
      }
      return sum;
   }

   static void doPermutation(int newSize){
      if(size <= 3) return;    // size 2 or 3 definitely has no solution
      if(size == 13){      // if size is 13, the factorial is out of int's bound
         int Caozuoshu = 0;             // total rotation times
         for(int i=1; i<12; i++){
            Caozuoshu += fac(12) / fac(i);
         }

      /* Caozuoshu is the number of rotations needed for size = newSize */
         Stack generalStack = new Stack(Caozuoshu+1);   // extra one slot for 13
         int currentSize = 3;     // start with level 3
         for(int k=0; k<3; k++){
            generalStack.push(2);
            generalStack.push(2);
            generalStack.push(3);
         }

         for(int ShiSan = 0; ShiSan < 13; ShiSan++){
            while(currentSize < 12){
               generalStack.push(++currentSize);
               int currentTop = generalStack.top + 1;
               for(int outer=1; outer<currentSize; outer++){    // copy currentSize times
                  for(int inner=0; inner < currentTop; inner++){   // copy generalStack.top items
                     int currentSlot = generalStack.peekArbitrary(inner);
                     generalStack.push(currentSlot);
                  }
               }  // end outer for
            }  // end while

            generalStack.push(13);

         /* Push process ends here. Following are pop process. */

            while(!generalStack.isEmpty()){
               int rotationSize = generalStack.pop();
               rotate(rotationSize);
               storeAnswer();
               if(noSol == false) return;     // only print one possible sol out
            }  // end while (pop)
         }   // end for (13)
         return;
      }  // end if (size == 13)

      int Caozuoshu = 0;             // total rotation times
      for(int i=1; i<newSize; i++){
         Caozuoshu += fac(newSize) / fac(i);
      }

      /* Caozuoshu is the number of rotations needed for size = newSize */
      Stack generalStack = new Stack(Caozuoshu);
      int currentSize = 3;     // start with level 3
      for(int k=0; k<3; k++){
         generalStack.push(2);
         generalStack.push(2);
         generalStack.push(3);
      }

      while(currentSize < newSize){
         generalStack.push(++currentSize);
         int currentTop = generalStack.top + 1;
         for(int outer=1; outer<currentSize; outer++){    // copy currentSize times
            for(int inner=0; inner < currentTop; inner++){   // copy generalStack.top items
               int currentSlot = generalStack.peekArbitrary(inner);
               generalStack.push(currentSlot);
            }
         }  // end outer for
      }  // end while

   /* Push process ends here. Following are pop process. */

      while(!generalStack.isEmpty()){
         int rotationSize = generalStack.pop();
         rotate(rotationSize);
         storeAnswer();
         if(noSol == false) return;     // only print one possible sol out
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

   static boolean finalAnswer(int[] x, int[] y){    // make the solution match the input
      for(int i=0; i<x.length; i++){
         if(chessArray[x[i]] != y[i]) return false;   // if it does not match the input
      }
      return true;
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
}

