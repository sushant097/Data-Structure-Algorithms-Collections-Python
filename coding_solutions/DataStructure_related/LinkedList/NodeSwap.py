
# Problem: Swap two node in linkedlist
def swap_nodes(self, key1, key2):
    if key1 == key2:
        return 
    
    prev_1 = None
    curr_1 = self.head
    while curr_1.next and curr_1.data != key1:
        prev_1 = curr_1
        curr_1 = curr_1.next
        
    prev_2 = None
    curr_2 = self.head
    while curr_2.next and curr_2.data != key2:
        prev_2 = curr_2
        curr_2 = curr_2.next
        
    if not curr_1 or not curr_2:
        return
    
    
    # if curr_1 is head
    if prev_1:
        prev_1.next = curr_2
    else:
        self.head = curr_2
    
    # if curr_2 is head
    if prev_2:
        prev_2.next = curr_1
    else:
        self.head = curr_1
        
    curr_1.next, curr_2.next = curr_2.next, curr_1.next
 