package leetcode;
//841. Keys and Rooms

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class P841 {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int roomSize = rooms.size();
        Set<Integer> visited = new HashSet<>();
        dfs(rooms, 0, visited);
        return visited.size() == roomSize;

    }

    public void dfs(List<List<Integer>> rooms, int roomIndex, Set<Integer> visited) {
        if (visited.contains(roomIndex)) {
            return;
        }

        visited.add(roomIndex);
        List<Integer> keys = rooms.get(roomIndex);

        for (int key : keys) {
            dfs(rooms, key, visited);
        }

    }

    public static void main(String[] args) {
        List<List<Integer>> rooms = new ArrayList<>();
        rooms.add(List.of(1, 3));
        rooms.add(List.of(3, 0, 1));
        rooms.add(List.of(2));
        rooms.add(List.of(0));
        P841 p841 = new P841();
        System.out.println(p841.canVisitAllRooms(rooms));
    }

}
