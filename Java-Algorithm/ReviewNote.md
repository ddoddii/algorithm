## Review Note 

- Array 에서 배열의 길이 추적하는 방법 (leetcode p443)
  - array[idx++] 를 사용 
    
    아래 코드에서 index가 chars 의 길이가 된다. 
    ```java
    int i = 0;
    int index = 0;
    while( i < chars.length){
            char currentChar = chars[i];
            int count = 0;

            while(i < chars.length && chars[i] == currentChar){
                i++;
                count++;
            }

            chars[index++] = currentChar;
    }
    ```

- 배열 내 순서를 바꾸거나 할 때 sorting 알고리즘과 pointer를 떠올리자 -> Quicksort, Megersort .. 
