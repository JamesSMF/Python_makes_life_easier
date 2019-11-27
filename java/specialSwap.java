class specialSwap{
   public static void main(String[] args){
      int x = 3;
      int y = 4;

      // ^ means bitwise XOR
      x = x^y;
      y = x^y;      // y = (x^y)^y = x^0 = x
      x = x^y;      // x = (x^y)^x = y^0 = y

      System.out.println("x = " + x + " , y = " + y);
   }
}

// Note: this program only works for int
