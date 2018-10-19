import java.util.Scanner;
import java.io.*;

class Coordinate{
   public int c;
   public int r;
   public char type;    // the name of the chess

   public Coordinate(char type, int c, int r){
      this.type = type;
      this.c = c;
      this.r = r;
   }

   public boolean equals(Coordinate coord){
      return (c == coord.c && r == coord.r);
   }
}

class Link{
   public Coordinate data;
   public Link next;

   public Link(Coordinate coord){
      data = coord;
      next = null;
   }
}

class LinkedList{
   public Link first;

   public LinkedList(){ first = null; }    // constructor

   public boolean isEmpty(){ return first == null; }
   public void insertFirst(Coordinate coord){
      Link newLink = new Link(coord);
      newLink.next = first;
      first = newLink;
   }

   public Link delete(int c, int r){
      Link current = first, previous = first;
      while(current.data.c != c || current.data.r != r){     // find the Link
         if(current.next == null) return null;     // did not find
         else{                       // proceed to the next one
            previous = current;
            current = current.next;
         }
      }  // end while
      if(current == first) first = first.next;      // delete the first Link
      else previous.next = current.next;             // delete the Link
      return current;
   }

   public boolean isValid(){      // check if two chesses take up the same square
      Link target = first, current = first;
      while(! target.data.equals(current.data)){
         if(current.next==null){           // current hits the end
            if(target.next==null) return true;     // target hits the end
            target = target.next;
            current = target;
         }
         current = current.next;
      }
      return false;
   }

   public char find(int col, int row){
      Link current = first;
      Coordinate key = new Coordinate('z', col, row);
      while(current.data.equals(key)){
         if(current.next==null) return 'z';     // did not find
         current = current.next;
      }
      return current.data.type;
   }

   public boolean queenAttacks(char ch, int c, int r){    // checks for queen attacks
      Coordinate theQueen;
      Link current = first;
      int copyC = c, copyR = r;
      while(c < 7 && r < 7){
         c++;
         r++;
         theQueen = new Coordinate(ch,c,r);
         if(!current.data.equals(theQueen)){
            if(current.next == null) return false;
            current = current.next;
         }else{
            switch(ch){
               case 'Q':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'q':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;
            }  // end switch
         }
      }  // end while

      c = copyC;
      r = copyR;

      while(c < 7 && r > 1){
         c++;
         r--;
         theQueen = new Coordinate(ch,c,r);
         if(!current.data.equals(theQueen)){
            if(current.next == null) return false;
            current = current.next;
         }else{
            switch(ch){
               case 'Q':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'q':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;
            }  // end switch
         }
      }  // end while

      c = copyC;
      r = copyR;

      while(c > 1 && r > 1){
         c--;
         r--;
         theQueen = new Coordinate(ch,c,r);
         if(!current.data.equals(theQueen)){
            if(current.next == null) return false;
            current = current.next;
         }else{
            switch(ch){
               case 'Q':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'q':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;
            }  // end switch
         }
      }  // end while

      c = copyC;
      r = copyR;

      while(c > 1 && r < 7){
         c--;
         r++;
         theQueen = new Coordinate(ch,c,r);
         if(!current.data.equals(theQueen)){
            if(current.next == null) return false;
            current = current.next;
         }else{
            switch(ch){
               case 'Q':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'q':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;
            }  // end switch
         }
      }  // end while

      return false;
   }
}

class ChessBoard{
   public static void main(String[] args) throws IOException{
      if(args.length != 2){
         System.out.println("Usage: java -jar ChessPiece.jar <input file><output file>.");
         System.exit(1);
      }

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));
      
      LinkedList chess = new LinkedList();   // the most important thing in this prog.

      while(sc.hasNextLine()){
         String nextLine = sc.nextLine();   // store the whole line
         int lineLen = nextLine.length() - 5;
         for(int i=5; i<lineLen+6; i += 6){
            int col = Character.getNumericValue(nextLine.charAt(i+2)) - 1;
            int row = Character.getNumericValue(nextLine.charAt(i+4)) - 1;
            Coordinate newChess = new Coordinate(nextLine.charAt(i), col, row);   // generate
            chess.insertFirst(newChess);           // put onto the chess board
         }

         int ccc = Character.getNumericValue(nextLine.charAt(0)) - 1;
         int rrr = Character.getNumericValue(nextLine.charAt(2)) - 1;

         System.out.println(chess.isValid());

         if(!chess.isValid()){    // checks for validity
            out.println("Invalid");
            continue;
         }

         if(chess.find(ccc, rrr)=='z'){   // checks for existence of the chess
            out.println("-");
            continue;
         }

         char targetChess = chess.find(ccc, rrr);

         out.print(targetChess + " ");

         switch(targetChess){
            case 'Q':
            case 'q':
               if(chess.queenAttacks(targetChess,ccc,rrr) == true) out.println("y");
               else out.println("n");
               break;
         }
      }   // end while (proceed to the next line of input)
   }  // end main
}  // end class






