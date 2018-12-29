import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class Dictionary<K, V> {

    private List<Entry<K, V>> set;

    public Dictionary() {
        this.set = new LinkedList<Entry<K, V>>();
    }

    /**
     * find(k): if the dictionary has an entry with key k, returns it, else, returns null
     */
    public Entry<K, V> find(K key) {
        // for all entries in set...
        //   check if key mathches
        //     - if it does than return it

        // else
        return null;
    }

    /**
     * findAll(k): returns an iterator of all entries with key k
     * @return
     */
    public Iterator<Entry<K, V>> findAll(K key) {
        // make a temporary list
        // for all entries in set...
        //   check if key matches
        //     - if it does than add it to temporary list

        // return the temporary list iterator (list.iterator())
        return null;
    }

    /**
     * insert(k, o): inserts and returns the entry (k, o)
     */
    public Entry<K, V> insert(K key, V value) {
        // obvious
        return null;
    }

    /**
     * remove(e): remove the entry e from the dictionary
     */
    public Entry<K, V> remove(Entry<K, V> entry) {
        return entry;
    }

    public int size() {
        return set.size();
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    @Override
    public String toString() {
        return set.toString();
    }
}
