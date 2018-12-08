class UnitTest{
   static boolean noSol;   // check if has solution
   static int[] result = new int[10000];    // the result array
   static int nextEmpty = 0;    // the index of next empty slot in result
   static int nextElem = 0;     // the index of the next used slot
   static int[] chessArray;

   public static void main(String[] args){
      chessArray = new int[5];
      chessArray[0] = 1;
      chessArray[1] = 3;
      chessArray[2] = 0;
      chessArray[3] = 2;
      chessArray[4] = 4;
      System.out.println(isSolution(chessArray));
      int[] xcoord = {0, 1};
      int[] ycoord = {1, 3};
      System.out.println(finalAnswer(xcoord, ycoord));
   }

   static boolean isSolution(int[] A){    // test for diagonal attacks
      for(int i=0; i<4; i++){
         for(int j=i+1; j<5; j++){
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
}
