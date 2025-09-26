import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        TreeMap<Integer, Integer> tm = new TreeMap<>();
        int key;
        int val;
        
        for (String op : operations) {
            String[] parts = op.split(" ");
            
            if (parts[0].equals("I")) {
                int num = Integer.parseInt(parts[1]);
                if (!tm.containsKey(num)) {
                    tm.put(num, 1);
                } else {
                    val = tm.get(num);
                    tm.put(num, val + 1);
                }
            }
            else if (parts[0].equals("D")) {
                if (!tm.isEmpty()) {
                    if (parts[1].equals("1")){
                        if (tm.get(tm.lastKey()) != 1) {
                            key = tm.lastKey();
                            val = tm.get(key);
                            tm.put(key, val - 1);
                        } else {
                            tm.remove(tm.lastKey());
                        }
                    }
                    else if (parts[1].equals("-1")){
                        if (tm.get(tm.firstKey()) != 1) {
                            key = tm.firstKey();
                            val = tm.get(key);
                            tm.put(key, val - 1);
                        } else {
                            tm.remove(tm.firstKey());
                        }
                    }
                }
                
            }
        }
        
        if (tm.isEmpty()) {
            return new int[]{0, 0};
        } else {
            return new int[]{tm.lastKey(), tm.firstKey()};
        }
    }
}