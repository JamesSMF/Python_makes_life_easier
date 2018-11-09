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

   public void revise(int c, int r){
      data.c = c;
      data.r = r;
   }

   public void displayLink(){
      System.out.println(data.type + " " + data.c + " " + data.r);
   }
}

class LinkedList{
   public Link first;
   public Coordinate gua_le;      // the coordinate of dead chess

   public LinkedList(){       // constructor
      first = null;
      gua_le = null;
   }

   public boolean isEmpty(){ return first == null; }
   public void insertFirst(Coordinate coord){
      Link newLink = new Link(coord);
      newLink.next = first;
      first = newLink;
   }

   public void insertFirst(Link theLink){      // override to accept Links
      theLink.next = first;
      first = theLink;
   }

   public void displayList(){
      Link current=first;
      while(current != null){
         current.displayLink();
         current = current.next;
      }
   }

   public void insertFirst(char ch, int c, int r){
      Coordinate newCoord = new Coordinate(ch, c, r);
      Link newLink = new Link(newCoord);
      newLink.next = first;
      first = newLink;
   }

   public Link delete(int c, int r){
      Link current = first, previous = first;
      if(first.next == null){    // only one elem in the list
         first = null;
         return null;
      }
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

   public boolean bishopMove(char ch, int c, int r, int targetcol, int targetrow){
      if(Math.abs(c-targetcol) != Math.abs(r-targetrow)) return false;   // can't go there
      Coordinate theBishop = new Coordinate(ch, c, r);
      Link current = first;
      Coordinate target = new Coordinate('z', 0, 0);
      Link destination = new Link(target);
      while(current.next != null){
         if(current.data.c == targetcol && current.data.r == targetrow){
            target.type = current.data.type;
            target.c = targetcol;
            target.r = targetrow;
            destination.data = target;
         }
         if(current.data.c==c && current.data.r==r){
            current = current.next;
            continue;
         }
         if(
            (current.data.c - theBishop.c == current.data.r - theBishop.r ||
            current.data.c - theBishop.c == theBishop.r - current.data.r) 
            &&
               (
               ((current.data.c > targetcol) && (current.data.r < theBishop.r) 
               ||
               (current.data.c < targetcol) && (current.data.r > theBishop.r))
               )
            )
         {                    // check for blocks on the way
            return false;
         }  // end if
         current = current.next;
      }  // end while

      boolean isBishop = false;

      if(current.data.c==c && current.data.r==r)     // if the last one is bishop
         isBishop = true;             // No block is possible

      if(current.data.c == targetcol && current.data.r == targetrow){
         target.type = current.data.type;
         target.c = targetcol;
         target.r = targetrow;
         destination.data = target;
      }
      if(!isBishop  &&
         (current.data.c - theBishop.c == current.data.r - theBishop.r ||
         current.data.c - theBishop.c == theBishop.r - current.data.r) 
         &&
            (
            ((current.data.c > targetcol) && (current.data.r < theBishop.r) 
            ||
            (current.data.c < targetcol) && (current.data.r > theBishop.r))
            )
         )
      {            // check for the last one
         return false;
      }  // end if
      /* Up to here, there is no block on the half way */
      /* Check for destination square */
      
      if(destination.data.type == 'z'){      // mei_ren, sui_bian_she
         return true;
      }else if((destination.data.type-95) * (theBishop.type-95) < 0){
         gua_le = destination.data;           // gei_wo_wang_si_li_nong
         return true;
      }else                     // zi_ji_ren, bie_kai_qiang
         return false;
   }

   public boolean rookMove(char ch, int c, int r, int targetcol, int targetrow){
      if(c != targetcol && r != targetrow) return false;   // can't go there
      Coordinate theRook = new Coordinate(ch, c, r);
      Link current = first;
      Coordinate target = new Coordinate('z', 0, 0);
      Link destination = new Link(target);
      while(current.next != null){
         if(current.data.c == targetcol && current.data.r == targetrow){
            target.type = current.data.type;
            target.c = targetcol;
            target.r = targetrow;
            destination.data = target;
         }

         if(current.data.c==c && current.data.r==r){
            current = current.next;
            continue;
         }

         if(
            (current.data.c == theRook.c || theRook.r == current.data.r) 
            &&
               (
               (Math.abs(current.data.c - theRook.c) < Math.abs(targetcol - theRook.c))
               ||
               (Math.abs(current.data.r - theRook.r) < Math.abs(targetrow - theRook.r))
               )
            )
         {                    // check for blocks on the way
            return false;
         }  // end if
         current = current.next;
      }  // end while

      boolean isRook = false;

      if(current.data.c==c && current.data.r==r)     // if the last one is rook
         isRook = true;             // No block is possible

      if(current.data.c == targetcol && current.data.r == targetrow){
         target.type = current.data.type;
         target.c = targetcol;
         target.r = targetrow;
         destination.data = target;
      }

      System.out.println(current.data.c + " " + current.data.r);
      System.out.println(theRook.c + " " + theRook.r);
      if(!isRook &&
         (current.data.c == theRook.c) 
         &&
         Math.abs(current.data.r - theRook.r) < Math.abs(targetrow - theRook.r)
         )
      {                    // check for the last one
         return false;
      }else if(!isRook && 
      theRook.r == current.data.r &&
      Math.abs(current.data.c - theRook.c) < Math.abs(targetcol - theRook.c))
      {
         return false;
      }

      /* Up to here, there is no block on the half way */
      /* Check for destination square */
      
      if(destination.data.type == 'z'){      // mei_ren, sui_bian_she
         return true;
      }else if((destination.data.type-95) * (theRook.type-95) < 0){
         gua_le = destination.data;           // gei_wo_wang_si_li_nong
         return true;
      }else{                     // zi_ji_ren, bie_kai_qiang
         return false;
      }
   }

   public boolean queenMove(char ch, int c, int r, int targetcol, int targetrow){
      switch(ch){
         case 'Q':
            return (rookMove('R', c, r, targetcol, targetrow) || bishopMove('B', c, r, targetcol, targetrow));
         case 'q':
            return (rookMove('r', c, r, targetcol, targetrow) || bishopMove('b', c, r, targetcol, targetrow));
      }
      return false;
   }

   public boolean kingMove(char ch, int c, int r, int targetcol, int targetrow){
      if(Math.abs(c-targetcol) > 1 || Math.abs(r-targetrow) > 1) 
         return false;   // can't go there
      Coordinate theKing = new Coordinate(ch, c, r);
      Link current = first;
      Coordinate target = new Coordinate('z', 0, 0);
      Link destination = new Link(target);

      /* No blocks on King's way is possible, so we only need to find the destination chess */
      while(current.next != null){
         if(current.data.c == targetcol && current.data.r == targetrow){
            target.type = current.data.type;
            target.c = targetcol;
            target.r = targetrow;
            destination.data = target;
         }

         current = current.next;
      }  // end while

      if(current.data.c == targetcol && current.data.r == targetrow){
         target.type = current.data.type;
         target.c = targetcol;
         target.r = targetrow;
         destination.data = target;
      }

      /* Check for destination square */
      
      if(destination.data.type == 'z'){      // mei_ren, sui_bian_she
         return true;
      }else if((destination.data.type-95) * (theKing.type-95) < 0){
         gua_le = destination.data;           // gei_wo_wang_si_li_nong
         return true;
      }else{                     // zi_ji_ren, bie_kai_qiang
         return false;
      }
   }

   public boolean knightMove(char ch, int c, int r, int targetcol, int targetrow){
      if(!((Math.abs(c-targetcol) == 1 && Math.abs(r-targetrow) == 2)
      || (Math.abs(r-targetrow) == 1) && Math.abs(c-targetcol) == 2))
         return false;                          // can't go there
      Coordinate theKnight = new Coordinate(ch, c, r);
      Link current = first;
      Coordinate target = new Coordinate('z', 0, 0);
      Link destination = new Link(target);

      /* No blocks on Knight's way is possible, so we only need to find the destination chess */
      while(current.next != null){
         if(current.data.c == targetcol && current.data.r == targetrow){
            target.type = current.data.type;
            target.c = targetcol;
            target.r = targetrow;
            destination.data = target;
         }

         current = current.next;
      }  // end while

      if(current.data.c == targetcol && current.data.r == targetrow){
         target.type = current.data.type;
         target.c = targetcol;
         target.r = targetrow;
         destination.data = target;
      }

      /* Check for destination square */
      
      if(destination.data.type == 'z'){      // mei_ren, sui_bian_she
         return true;
      }else if((destination.data.type-95) * (theKnight.type-95) < 0){
         gua_le = destination.data;           // gei_wo_wang_si_li_nong
         return true;
      }else{                     // zi_ji_ren, bie_kai_qiang
         return false;
      }
   }


   public boolean pawnMove(char ch, int c, int r, int targetcol, int targetrow){
      switch(ch){
         case 'P':
            if(!(r - targetrow == 1 && Math.abs(c - targetcol) == 1))
               return false;              // can't go there
            break;

         case 'p':
            if(!(targetrow - r == 1 && Math.abs(c - targetcol) == 1))
               return false;              // can't go there
            break; 
      }  // end switch

      Coordinate thePawn = new Coordinate(ch, c, r);
      Link current = first;
      Coordinate target = new Coordinate('z', 0, 0);
      Link destination = new Link(target);

      /* No blocks on Pawn's way is possible, so we only need to find the destination chess */
      while(current.next != null){
         if(current.data.c == targetcol && current.data.r == targetrow){
            target.type = current.data.type;
            target.c = targetcol;
            target.r = targetrow;
            destination.data = target;
         }

         current = current.next;
      }  // end while

      if(current.data.c == targetcol && current.data.r == targetrow){
         target.type = current.data.type;
         target.c = targetcol;
         target.r = targetrow;
         destination.data = target;
      }

      /* Check for destination square */
      
      if(destination.data.type == 'z'){      // mei_ren, sui_bian_she
         return true;
      }else if((destination.data.type-95) * (thePawn.type-95) < 0){
         gua_le = destination.data;           // gei_wo_wang_si_li_nong
         return true;
      }else{                     // zi_ji_ren, bie_kai_qiang
         return false;
      }
   }
}

class ChessMoves{
   static LinkedList chess = new LinkedList();   // the most important thing in this prog.

   public static void main(String[] args) throws IOException{
      if(args.length != 2){
         System.out.println("Usage: java -jar ChessBoard.jar <input file><output file>.");
         System.exit(1);
      }

      /* file reader and writer */

      Scanner sc = new Scanner(new File(args[0]));
      PrintWriter out = new PrintWriter(new FileWriter(args[1]));

      /* read lines from the input file */

      while(sc.hasNextLine()){
         boolean fuckUp = false;       // if something go wrong, this turns into true
         String nextLine = sc.nextLine();   // store the whole line
         int lineLen = nextLine.length();   // the length of the line
         char currentChar = 'z';       // take one char from the current line
         int colonPosition = 0;        // the position of the colon

         for(int outer=0; outer<lineLen; outer += 6){
            Link nextChess = new Link(new Coordinate('z', 0, 0));   // initialize
            for(int inner=0; inner<6; inner++){
               currentChar = nextLine.charAt(outer + inner);

               if(inner==0) nextChess.data.type = currentChar;
               if(inner==2) nextChess.data.c = Character.getNumericValue(currentChar) - 1;
               if(inner==4) nextChess.data.r = Character.getNumericValue(currentChar) - 1;
               if(currentChar == ':'){      // All chesses are placed on the board
                  colonPosition = outer+inner;
                  break;
               }
            }  // end inner for
            chess.insertFirst(nextChess);
            if(currentChar == ':') break;    // finish inputting chess locations
         }  // end outer for

         /* To this point, all chessBoard information is stored in the list */

         int[] startPos = new int[2];
         int[] endPos = new int[2];

         for(int move=colonPosition+1; move<lineLen; move += 8){
            startPos[0] = Character.getNumericValue(nextLine.charAt(move+1)) - 1;
            startPos[1] = Character.getNumericValue(nextLine.charAt(move+3)) - 1;
            endPos[0] = Character.getNumericValue(nextLine.charAt(move+5)) - 1;
            endPos[1] = Character.getNumericValue(nextLine.charAt(move+7)) - 1;

            char chessType = chess.find(startPos[0], startPos[1]);

            if(chessType == 'b' || chessType == 'B'){
               if(!chess.bishopMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }  // end if
            }else if(chessType == 'r' || chessType == 'R'){
               if(!chess.rookMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }  // end if
            }else if(chessType == 'q' || chessType == 'Q'){
               if(!chess.queenMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }
            }else if(chessType == 'k' || chessType == 'K'){
               if(!chess.kingMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }
            }else if(chessType == 'n' || chessType == 'N'){
               if(!chess.knightMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }
            }else if(chessType == 'p' || chessType == 'P'){
               if(!chess.pawnMove(chessType, startPos[0], startPos[1], endPos[0], endPos[1])){
                  fuckUp = true;
                  out.print(startPos[0]+1 + " ");
                  out.print(startPos[1]+1 + " ");
                  out.print(endPos[0]+1 + " ");
                  out.println(endPos[1]+1 + " illegal");
                  out.flush();
                  break;
               }
            }else{                     // did not find the chess on the board
               fuckUp = true;
               out.print(startPos[0]+1 + " ");
               out.print(startPos[1]+1 + " ");
               out.print(endPos[0]+1 + " ");
               out.println(endPos[1]+1 + " illegal");
               out.flush();
               break;           
            }

         /* if it is not fucked up, change the coordinate of the moved chess */

            if(chess.gua_le != null)     // some chess is dead
               chess.delete(chess.gua_le.c, chess.gua_le.r);   // delete the dead chess


         /* revise the coordination of the moved chess */

            chess.delete(startPos[0], startPos[1]);
            chess.insertFirst(chessType, endPos[0], endPos[1]);

            chess.displayList();
            System.out.println();
         }  // end for

         if(!fuckUp){
            out.println("legal");
            out.flush();
         }

         chess.delete();
      }   // end while (proceed to the next line of input)

      sc.close();
      out.close();
   }  // end main
}  // end class




