// Name of the Game: Sum of Digits
// Definition:
//    -- Sum of Digits: the sum of numbers on each digits
//    -- Digital root: do the process of sum of digits repeatedly until
//                     the sum is finally less than 10
//
// Game rules: the program will generate an array of ints randomly. The player
//             is prompted to choose a number either from the beginning of the
//             array or the tail of the array (namely A[0] or A[A.length-1]).
//             The Digital root is then calculated and stored in a new array
//             called Temp Array. After that, the computer will choose a 
//             number following the same rule.
//
//             When the array finally becomes empty, numbers in Temp Array are
//             multiplied up. If the player's product is higher, then the player 
//             wins, and vice versa.

import java.util.Random;
import java.io.*;

class Game{
   static int[] user_tempArray;
   static int[] comp_tempArray;
   static int arrayLen = 8;
   static int uDex = 0;
   static int cDex = 0;

   public static void main(String[] args) throws IOException{
      System.out.println("欢迎试玩少儿数学游戏：掐头龙");
      System.out.println("开发者：James Li");
      System.out.println("游戏开始，电脑会随机生成8个数字，游戏玩家可以选择");
      System.out.println("取第一个数字或者取最后一个数字。随后，计算机将计算");
      System.out.println("所选数字的digital root，并将其结果存入tempArray里。");
      System.out.println();
      System.out.println(">>> digital root: 例如数字1354，首先计算各位之和:");
      System.out.println(">>> 1+3+5+4 = 13");
      System.out.println(">>> 由于13大于等于10，故需要再次计算13的digital root:");
      System.out.println(">>> 1+3 = 4");
      System.out.println(">>> 由于4小于10，故不需要进一步计算。");
      System.out.println(">>> 所以最终得到1354的digital root等于4。");
      System.out.println();
      System.out.println("玩家的回合结束后，电脑会根据一定的算法，根据同样的规则");
      System.out.println("进行选择。相应的digital root会保存在电脑方的tempArray里。");
      System.out.println("待8个数字被全部选择完毕，程序会计算两方tempArray中数字的");
      System.out.println("积，作为游戏最终得分。得分较高者胜出。");
      System.out.println();

      Random rand = new Random();
      int[] init_array = new int[8];
      user_tempArray = new int[4];
      comp_tempArray = new int[4];
      int nextNum=0;

      // generate a random array
      for(int i=0; i<8; i++){
         nextNum = rand.nextInt(10000) + 1;
         init_array[i] = nextNum;
      }

      // prompts
      while(arrayLen != 0){
         prompt(init_array);
         comp_choice(init_array);
         System.out.println();
      }

      // calculate points on both sides
      System.out.println("Your score: " + mult(user_tempArray) + "      Comp score: " + mult(comp_tempArray));
      if(mult(user_tempArray) > mult(comp_tempArray))
         System.out.println("You win!");
      else if(mult(user_tempArray) < mult(comp_tempArray))
         System.out.println("You lose.");
      else
         System.out.println("Draw!");
   }

   static void prompt(int[] theArray) throws IOException{
      System.out.println("Now the array looks like this: ");
      for(int i=0; i<arrayLen; i++)
         System.out.print(theArray[i] + "  ");
      System.out.println();

      int user_choice = -1;
      while(user_choice != theArray[0] && user_choice != theArray[arrayLen - 1]){
         System.out.println("Please choose either " + theArray[0] + " or " + theArray[arrayLen - 1]);
         user_choice = getInt();
      }

      // check what the user got
      if(user_choice == theArray[0]) 
         shift(theArray);
      /* if the user instead chooses the last item, I don't give a fuck about that. */

      // store user choice
      user_tempArray[uDex++] = dig_root(user_choice);

      // shrink the size of the array
      arrayLen--;
   }

   /*
   General Strategy:
   * if abs(head-tail) > 2
   *    if head < tail then tail
   *    else head
   * else 比较倒数第二个
   */
   static void comp_choice(int[] theArray){
      int digHead = dig_root(theArray[0]);
      int digTail = dig_root(theArray[arrayLen - 1]);
      int digSecTail = 0;
      int digSecHead = 0;
      if(arrayLen>1){
         digSecHead = dig_root(theArray[1]);
         digSecTail = dig_root(theArray[arrayLen - 2]);
      }
      int absValue = Math.abs(digHead - digTail);

      if(absValue>2 || arrayLen <= 3){     // if abs diff is large or array len is less than or equal to 3
         if(arrayLen==1){
            comp_tempArray[cDex++] = digHead;
            System.out.println("\nYour rival chose " + theArray[0]);
         }else{
            if(digHead < digTail){
               comp_tempArray[cDex++] = digTail;
               System.out.println("\nYour rival chose " + theArray[arrayLen-1]);
            }else{
               comp_tempArray[cDex++] = digHead;
               System.out.println("\nYour rival chose " + theArray[0]);
               shift(theArray);
            }
         }
      }else if(digHead<5 && digTail<5){  // if abs diff is small and both number is less than 5
         if(digSecHead < digSecTail){
            comp_tempArray[cDex++] = digHead;
            System.out.println("\nYour rival chose " + theArray[0]);
            shift(theArray);
         }else{
            comp_tempArray[cDex++] = digTail;
            System.out.println("\nYour rival chose " + theArray[arrayLen-1]);
         }
      }else{
         if(digHead < digSecHead && digTail > digSecTail){
            comp_tempArray[cDex++] = digTail;
            System.out.println("\nYour rival chose " + theArray[arrayLen-1]);
         }else if(digHead > digSecHead && digTail < digSecTail){
            comp_tempArray[cDex++] = digHead;
            System.out.println("\nYour rival chose " + theArray[0]);
            shift(theArray);
         }else{                             // Random choice (to make the game easier)
            int ranNum = (int)(Math.random() * 2);
            if(ranNum==0){
               comp_tempArray[cDex++] = digTail;
               System.out.println("\nYour rival chose " + theArray[arrayLen-1]);
            }else{
               comp_tempArray[cDex++] = digHead;
               System.out.println("\nYour rival chose " + theArray[0]);
               shift(theArray);
            }
         }
      }

      arrayLen--;
   }

   static void shift(int[] theArray){
      for(int i=0; i<arrayLen - 1; i++)
         theArray[i] = theArray[i+1];
   }

   static int mult(int[] theArray){
      int prod = 1;
      for(int elem : theArray){
         prod *= elem;
      }
      return prod;
   }

   static int sum(int[] theArray){
      int Sum = 0;
      for(int elem : theArray){
         Sum += elem;
      }
      return Sum;
   }

   static int[] int_to_array(int theNum){
      String tempString = Integer.toString(theNum);
      int[] theArray = new int[tempString.length()];
      for(int i=0; i<tempString.length(); i++)
         theArray[i] = tempString.charAt(i) - '0';
      return theArray;
   }

   static int dig_root(int theNum){
      // base case
      if(theNum < 10) return theNum;

      // calculate the digital root
      int[] numArray = int_to_array(theNum);
      theNum = sum(numArray);
      return dig_root(theNum);
   }

   static String getString() throws IOException{
      InputStreamReader isr = new InputStreamReader(System.in);
      BufferedReader br = new BufferedReader(isr);
      return br.readLine();
   }

   static int getInt() throws IOException{
      String s = getString();
      return Integer.parseInt(s);
   }
}




