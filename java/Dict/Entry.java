public class Entry<K, V> {

    K key;
    V value;

    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K key() {
        return key;
    }

    public V value() {
        return value;
    }

    @Override
    public String toString() {
        return "(" + key + ", " + value + ")";
    }

    // Methods needed to correctly behave in containers like sets, hashmaps:
    // (I generated those automatically in NetBeans)
    @Override
    public boolean equals(Object obj) {
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        final Entry<K, V> other = (Entry<K, V>) obj;
        if (this.key != other.key && (this.key == null || !this.key.equals(other.key)))
            return false;
        if (this.value != other.value && (this.value == null || !this.value.equals(other.value)))
            return false;
        return true;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 23 * hash + (this.key != null ? this.key.hashCode() : 0);
        hash = 23 * hash + (this.value != null ? this.value.hashCode() : 0);
        return hash;
    }
}
