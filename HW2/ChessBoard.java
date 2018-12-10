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

   public void delete(){        // override
      first = null;
   }

   public char find(int col, int row){
      Link current = first;
      Coordinate key = new Coordinate('z', col, row);
      while(!current.data.equals(key)){
         if(current.next==null) return 'z';     // did not find
         current = current.next;
      }
      return current.data.type;
   }

   public boolean bishopAttack(char ch, int c, int r){
      Coordinate theBishop = new Coordinate(ch, c, r);
      Link current = first;
      while(current.next != null){
         if(current.data.type==ch){
            current = current.next;
            continue;
         }
         if(current.data.c - theBishop.c == current.data.r - theBishop.r ||
            current.data.c - theBishop.c == theBishop.r - current.data.r){
            switch(ch){
               case 'B':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'b':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;
            }  // end switch
         }  // end if
         current = current.next;
      }  // end while

      if(current.data.type==ch) return false;
      if(current.data.c - theBishop.c == current.data.r - theBishop.r ||
         current.data.c - theBishop.c == theBishop.r - current.data.r){
         switch(ch){
            case 'B':
               if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                  || current.data.type == 'b' || current.data.type == 'n')
                  return true;
               break;

            case 'b':
               if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                  || current.data.type == 'B' || current.data.type == 'N')
                  return true;
               break;
         }  // end switch
      }  // end if
      return false;
   }

   public boolean rookAttack(char ch, int c, int r){
      Coordinate theRook = new Coordinate(ch, c, r);
      Link current = first;
      while(current.next != null){
         if(current.data.type==ch){
            current = current.next;
            continue;
         }
         if(current.data.c == theRook.c || current.data.r == theRook.r){
            switch(ch){
               case 'R':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'r':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;             
            }  // end switch
         }  // end if
         current = current.next;
      }  // end while

      if(current.data.type==ch) return false;
      if(current.data.c == theRook.c || current.data.r == theRook.r){
         switch(ch){
            case 'R':
               if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                  || current.data.type == 'b' || current.data.type == 'n')
                  return true;
               break;

            case 'r':
               if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                  || current.data.type == 'B' || current.data.type == 'N')
                  return true;
               break;             
         }  // end switch
      }
      return false;
   }

   public boolean queenAttack(char ch, int c, int r){
      switch(ch){
         case 'Q':
            return (rookAttack('R', c, r) || bishopAttack('B', c, r));
         case 'q':
            return (rookAttack('r', c, r) || bishopAttack('b', c, r));
      }
      return false;
   }

   public boolean kingAttack(char ch, int c, int r){
      Coordinate theKing = new Coordinate(ch, c, r);
      Link current = first;
      while(current.next != null){
         if(current.data.type==ch){
            current = current.next;
            continue;
         }
         if(current.data.c == theKing.c && (current.data.r - theKing.r == 1  ||
            theKing.r - current.data.r == 1) || current.data.r == theKing.r &&
            (current.data.c - theKing.c == 1 || theKing.c - current.data.c ==1)
            || ((theKing.c - current.data.c == 1 || current.data.c - theKing.c == 1)
            && (theKing.r - current.data.r == 1 || current.data.r - theKing.r == 1))){
            switch(ch){
               case 'K':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'k':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;             
            }  // end switch
         }  // end if
         current = current.next;
      }  // end while

      if(current.data.type==ch) return false;
      if(current.data.c == theKing.c && (current.data.r - theKing.r == 1  ||
         theKing.r - current.data.r == 1) || current.data.r == theKing.r &&
         (current.data.c - theKing.c == 1 || theKing.c - current.data.c ==1)
         || ((theKing.c - current.data.c == 1 || current.data.c - theKing.c == 1)
         && (theKing.r - current.data.r == 1 || current.data.r - theKing.r == 1))){
         switch(ch){
            case 'K':
               if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                  || current.data.type == 'b' || current.data.type == 'n')
                  return true;
               break;

            case 'k':
               if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                  || current.data.type == 'B' || current.data.type == 'N')
                  return true;
               break;             
         }  // end switch
      }  // end if
      return false;
   }

   public boolean knightAttack(char ch, int c, int r){
      Coordinate theKnight = new Coordinate(ch, c, r);
      Link current = first;
      while(current.next.next != null){
         if(current.data.type==ch){
            current = current.next;
            continue;
         }
         if(((current.data.c - theKnight.c == 2 || current.data.c - theKnight.c == -2) &&
            (current.data.r - theKnight.r == 1 || theKnight.r - current.data.r == 1)) ||
            ((current.data.r - theKnight.r == 2 || current.data.r - theKnight.r == -2) &&
            (current.data.c - theKnight.c == 1 || theKnight.c - current.data.c ==1))){
            switch(ch){
               case 'N':
                  if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                     || current.data.type == 'b' || current.data.type == 'n')
                     return true;
                  break;

               case 'n':
                  if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                     || current.data.type == 'B' || current.data.type == 'N')
                     return true;
                  break;             
            }  // end switch           
         }  // end if
         current = current.next;
      }  // end while

      if(current.data.type==ch) return false;
      if(((current.data.c - theKnight.c == 2 || current.data.c - theKnight.c == -2) &&
         (current.data.r - theKnight.r == 1 || theKnight.r - current.data.r == 1)) ||
         ((current.data.r - theKnight.r == 2 || current.data.r - theKnight.r == -2) &&
         (current.data.c - theKnight.c == 1 || theKnight.c - current.data.c ==1))){
         switch(ch){
            case 'N':
               if(current.data.type == 'k' || current.data.type == 'q' || current.data.type == 'r'
                  || current.data.type == 'b' || current.data.type == 'n')
                  return true;
               break;

            case 'n':
               if(current.data.type == 'K' || current.data.type == 'Q' || current.data.type == 'R'
                  || current.data.type == 'B' || current.data.type == 'N')
                  return true;
               break;             
         }  // end switch           
      }  // end if
      return false;
   }

   public boolean pawnAttack(char ch, int c, int r){
      Coordinate thePawn = new Coordinate(ch, c, r);
      Link current = first;
      while(current.next.next != null){
         if(current.data.type==ch){
            current = current.next;
            continue;
         }
         switch(ch){
            case 'P':
               if((thePawn.r - current.data.r == 1 && (thePawn.c - current.data.c == 1 ||
                  current.data.c - thePawn.c == 1)) && current.data.type > 95)
                  return true;
               break;

            case 'p':
               if((current.data.r - thePawn.r == 1 && (thePawn.c - current.data.c == 1 ||
                  current.data.c - thePawn.c == 1)) && current.data.type < 95)
                  return true;
               break;
         }  // end switch
         current = current.next;
      }  // end while

      if(current.data.type == ch) return false;
      else if((thePawn.r - current.data.r == 1 && (thePawn.c - current.data.c == 1 ||
      current.data.c - thePawn.c == 1)) && current.data.type > 95){
         if(ch == 'P') return true;
      }else if((current.data.r - thePawn.r == 1 && (thePawn.c - current.data.c == 1 ||
      current.data.c - thePawn.c == 1)) && current.data.type < 95){
         if(ch == 'p') return true;
      }  // end if-else
      return false;
   }
}

class ChessBoard{
   static LinkedList chess = new LinkedList();   // the most important thing in this prog.

   public static void main(String[] args) throws IOException{
      if(args.length != 2){
         System.out.println("Usage: java -jar ChessBoard.jar <input file><output file>.");
         System.exit(1);
      }

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));

      Link target, current;

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

         boolean isValid = false;

         target = chess.first;
         if(chess.isEmpty()){
            out.println("-");
            out.flush();
            continue;
         }else if(target.next == null)
            isValid = true;
         else{
            current = target.next;
            while(! target.data.equals(current.data)){
               if(current.next==null){           // current hits the end
                  if(target.next==current){
                     isValid = true;     // target hits the end
                     break;
                  }else{
                     target = target.next;
                     current = target;
                  }
               }
               current = current.next;
            }
         }

         if(!isValid){    // checks for validity
            out.println("Invalid");
            out.flush();
            chess.delete();
            continue;
         }

         if(chess.find(ccc, rrr)=='z'){   // checks for existence of the chess
            out.println("-");
            out.flush();
            chess.delete();
            continue;
         }

         char targetChess = chess.find(ccc, rrr);

         out.print(targetChess + " ");
         out.flush();

         switch(targetChess){
            case 'B':
            case 'b':
               if(chess.bishopAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;

            case 'Q':
            case 'q':
               if(chess.queenAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;

            case 'R':
            case 'r':
               if(chess.rookAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;

            case 'K':
            case 'k':
               if(chess.kingAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;

            case 'N':
            case 'n':
               if(chess.knightAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;

            case 'P':
            case 'p':
               if(chess.pawnAttack(targetChess,ccc,rrr)) out.println("y");
               else out.println("n");
               out.flush();
               break;              
         }  // end switch
         chess.delete();
      }   // end while (proceed to the next line of input)
   }  // end main
}  // end class




