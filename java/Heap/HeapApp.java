import java.util.Arrays;

class Heap{
   private int capacity;    // the max capacity of the heap
   private int size = 0;         // current size of the heap
   private int[] items;

   public Heap(int cap){
      capacity = cap;
      items = new int[capacity];
   }

   public int getLeftChild(int parentIndex){ return 2 * parentIndex + 1; }
   public int getRightChild(int parentIndex){ return 2 * parentIndex + 2; }
   public int getParent(int childIndex){ return (childIndex - 1) / 2; }

   public boolean hasLeft(int index){ return getLeftChild(index) < size; }
   public boolean hasRight(int index){ return getRightChild(index) < size; }
   public boolean hasParent(int index){ return getParent(index) >= 0; }

   public int left(int index){ return items[getLeftChild(index)]; }
   public int right(int index){ return items[getRightChild(index)]; }
   public int parent(int index){ return items[getParent(index)]; }

   public void swap(int index1, int index2){
      int temp = items[index1];
      items[index1] = items[index2];
      items[index2] = temp;
   }

   public void ensureEnoughSpace(){
      if(size == capacity){
         items = Arrays.copyOf(items, capacity*2);   // double the capacity
         capacity *= 2;
      }
   }

   public int peek(){
      if(size == 0) throw new IllegalStateException();
      return items[0];
   }

   public int poll(){
      if(size == 0) throw new IllegalStateException();
      int item = items[0];             // store the item to be deleted
      items[0] = items[--size];        // put the last item to the top
      heapifyDown();
      return item;
   }

   public void add(int item){
      ensureEnoughSpace();
      items[size++] = item;
      heapifyUp();
   }

   public void heapifyUp(){
      int index = size - 1;
      while(hasParent(index) && items[index] < parent(index)){
         swap(index, getParent(index));
         index = getParent(index);
      }
   }

   public void heapifyDown(){
      int index = 0;
      while(hasLeft(index)){
         int smaller = getLeftChild(index);
         if(hasRight(index) && right(index) < smaller) smaller = right(index);
         if(items[index] < items[smaller]) break;
         else{
            swap(index, smaller);
         }
         
         index = smaller;
      }
   }

   public void printHeap(){
      for(int i=0; i<size; i++){
         System.out.print(items[i] + " ");
      }
      System.out.println();
   }
}

public class HeapApp{
   public static void main(String[] args){
      Heap newHeap = new Heap(16);
      newHeap.add(5);
      newHeap.add(3);
      newHeap.add(6);
      newHeap.add(8);
      newHeap.add(2);
      newHeap.add(9);
      newHeap.add(1);
      newHeap.add(10);
      newHeap.add(25);
      newHeap.add(6);
      newHeap.add(13);  
      newHeap.add(14);

      newHeap.printHeap();
   }
}




