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
- 배열([]) 내 원소를 삭제하고 싶을 때, ArrayList 로 변환 해서 remove 메서드를 쓰는 것은 계산량이 많다. 최악의 경우 O(n) 이다. 
우회적인 방법으로 HashMap 안에 원소들과 등장 빈도를 저장해두고 삭제하고 싶으면 등장빈도 - 1 하는 것을 생각해보자. 
- 어떤 배열A 내 원소가 다른 배열B 안에 포함되어 있는지를 보고 싶을 때 -> B 에 HashSet 을 사용하자

  ```java
  Set<Character> vowels = new HashSet<>(Arrays.asList('a','e','i','o','u'));
  char[] strArr = s.toCharArray();
  int count = 0;
  
  for (int i = 0 ; i < strArr.length ; i++){
      if (vowels.contains(strArr[i])){
          count++;
      }
  }
  ```
  
- Integer 배열 내에서 max / min 값 구할때, `Arrays.stream(intArr).max().getAsInt()` 를 사용하는 방법과 for 문을 사용하는 방법이 있는데, for 문을 사용하는것이 시간 상 더 빨랐다.
- BFS 에서는 queue 를 사용하자. Binary Tree 에서 queue 를 이용해서 가장 오른쪽 노드를 추가하는 코드
  ```java
  List<Integer> traverse(TreeNode node, List<Integer> answer, Queue<TreeNode> q) {
    if (node == null) {
        return answer;
    }
    q.add(node);
    while (!q.isEmpty()) {
        int levelSize = q.size();
        for (int i = 0; i < levelSize; i++) {
            TreeNode currentNode = q.poll();
            if (i == levelSize - 1) {
                answer.add(currentNode.val);
            }
            if (currentNode.left != null) {
                q.add(currentNode.left);
            }
            if (currentNode.right != null) {
                q.add(currentNode.right);
            }
        }
    }
    return answer;
  }
  ```