class DigitalRoot{
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

   public static void main(String[] args){
      for(int i=100; i<1000; i++)
         System.out.print(dig_root(i) + " ");
      System.out.println();
   }
}
