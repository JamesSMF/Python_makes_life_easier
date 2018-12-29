public class DictionaryTest {

    static Dictionary<Integer, Character> dict = new Dictionary<Integer, Character>();

    public static void main(String[] args) {

        /*

        Test cases:

        1. insert(5,A) (5,A) (5,A)
        2. insert(7,B) (7,B) (5,A),(7,B)
        3. insert(2,C) (2,C) (5,A),(7,B),(2,C)
        4. insert(8,D) (8,D) (5,A),(7,B),(2,C),(8,D)
        5. insert(2,E) (2,E) (5,A),(7,B),(2,C),(8,D),(2,E)
        6. find(7) (7,B) (5,A),(7,B),(2,C),(8,D),(2,E)
        7. find(4) null (5,A),(7,B),(2,C),(8,D),(2,E)
        8. find(2) (2,C) (5,A),(7,B),(2,C),(8,D),(2,E)
        9. findAll(2) (2,C),(2,E) (5,A),(7,B),(2,C),(8,D),(2,E)
        10. size() 5 (5,A),(7,B),(2,C),(8,D),(2,E)
        11. remove(find(5)) (5,A) (7,B),(2,C),(8,D),(2,E)
        12. find(5) null (7,B),(2,C),(8,D),(2,E)
         */

        // Test case #1:
        test("insert(5,A)", dict.insert(5, 'A'));

        // Test case #2:
        test("insert(7,B)", dict.insert(7, 'B'));

        // Test case #3:
        test("insert(2,C)", dict.insert(2, 'C'));

        // ...

        // Test case #6:
        test("find(7))", dict.find(7));

        // implement all and check them during implementation


    }

    private static void test(String string, Object result) {
        System.out.print(string + " ");
        System.out.print(result);
        System.out.println(" " + dict);
    }
}
