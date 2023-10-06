package DataStructure.HashTable;

public class Main {
    public static void main(String[] args) {
        HashTable myHashTable = new HashTable();

        myHashTable.set("nails",500);
        myHashTable.set("keys",200);
        myHashTable.set("screw",200);

        myHashTable.printTable();
    }

}
