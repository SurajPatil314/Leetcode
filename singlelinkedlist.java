class MyLinkedList {
    
    class ListNode {
        ListNode next;
        int val;
        public ListNode(int x) {
            val = x;
        }
    }
    
    public int size = 0;
    public ListNode head = null;

    /** Initialize your data structure here. */
    public MyLinkedList() {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        int count = 0;
        ListNode currentNode = head;
        while(currentNode != null) {
            if(index == count) {
                return currentNode.val;
            }
            currentNode = currentNode.next;
            count++;
        }
        
        return -1;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        ListNode newNode = new ListNode(val);
        newNode.next = head;
        head = newNode;
        size++;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        if(head == null) {
            addAtHead(val);
            return;
        }
        ListNode currentNode = head;
        ListNode newNode = new ListNode(val);
        newNode.next = null;
        while(currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = newNode;
        size++;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if(index <= 0) {
            addAtHead(val);
            return;
        } else if (index == size) {
            addAtTail(val);
            return;
        }
        
        int count = 1;
        ListNode currentNode = head;
        
        while(currentNode != null) {
            if(count == index) {
                ListNode newNode = new ListNode(val);
                newNode.next = currentNode.next;
                currentNode.next = newNode;
                size++;
                return;
            }
            currentNode = currentNode.next;
            count++;
        }
        
        
        
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if(head == null){
            return;
        }
        
        if(index == 0) {
            head = head.next;
            size--;
            return;
        }
        
        ListNode currentNode = head;
        int count = 1;
        
        while(currentNode.next != null) {
            if(count == index) {
                currentNode.next = currentNode.next.next;
                size--;
                return;
            }
            
            currentNode = currentNode.next;
            count++;
        }
        
    }
}