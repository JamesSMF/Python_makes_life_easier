import java.io.*;
import java.util.Scanner;

class FileReverse{
   static char[] theStack;        // a simple stack
   static int top = -1;           // current top index of the stack

   public static void main(String[] args) throws IOException{
      if(args.length < 2){
         System.out.println("Usage: java -jar FileTokens.jar <input file> <output file>");
         System.exit(1);
      }

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));

      while( sc.hasNextLine() ){
         String line = sc.nextLine().trim() + " ";    // input the whole line
         String[] token = line.split("\\s+");       // put into array splited by " "
         int n = token.length;

         for (int i=0; i<n; i++){       // for each token in the array
            String temp = token[i];     // stores next token temporarily
            int size = temp.length();
            theStack = new char[size];
            for (int j=0; j<size; j++){
               char ch = temp.charAt(j);   // take the char
               push(ch);                   // push it into the stack;
            }
         
            while (!isEmpty()){
               out.print(pop());       // print the last one out
            }
            out.println();             // new line
         }
      }

      sc.close();
      out.close();
   }

   static void push(char ch){ theStack[++top] = ch; } // push in a new char
   static char pop(){ return theStack[top--]; }       // pop the top element from the stack
   static boolean isEmpty(){ return top == -1; }  // true if the stack is empty
}


