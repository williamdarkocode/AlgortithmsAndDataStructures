import random


class Empty(Exception):
    pass

# stacks are LIFO data structures; Last In, First Out. You can only remove, and access from the top
class ArrayStack:
    def __init__(self, _data = []):
        self._data = _data

    # takes O(1) time
    def __len__(self):
        return len(self._data)

    # takes O(1) time
    def is_empty(self):
        return len(self._data) == 0

    # takes O(1) time
    def push(self, e):
        self._data.append(e)

    #takes O(1) time
    def pop(self):
        if self.is_empty():
            raise Empty('Cannot pop on an Empty Stack')
        else:
            return self._data.pop()

    #takes O(1) time
    def peek(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._data[-1]
        
    def to_string(self):
        print(self._data)


# FIFO data structure; First in First out.
class ArrayQueue:
    DEFAULT_CAP = 10
    def __init__(self):
        self._data = [None] * self.DEFAULT_CAP
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_atcap(self):
        return self._size == len(self._data)

    def first(self):
        if self.is_empty():
            raise Empty('Empty Queue')
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty Queue')
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size-=1
        # reduce capacity to 1/2 if size is at or below 1/4 of capacity
        if 0 < self._size < len(self._data)//4:
            self.resize(len(self._data)//2)
    
    def enqueue(self, elem):
        if self.is_atcap():
            self.resize(len(self._data)*2)
        next_avail_pos = (self._front + self._size) % len(self._data)
        self._data[next_avail_pos] = elem
        self._size+=1
        return
    
    def resize(self, new_len):
        old_data = self._data
        self._data = [None]*new_len
        step = self._front
        for i in range(self._size):
            self._data[i] = old_data[step]
            step = (step+1) % len(old_data)
        self._front = 0
    
    def to_string(self):
        print('---QUEUE---')
        print(self._data[self._front:len(self._data)])


class DoubleEndedQueue:
    DEFAULT_CAP = 10
    def __init__(self):
        self._data = [None]*self.DEFAULT_CAP
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def at_max_cap(self):
        return self._size == len(self._data)

    def first(self):
        if self.is_empty():
            raise Empty('Empty Double Ended Queue')
        return self._data[self._front]
    
    def last(self):
        if self.is_empty():
            raise Empty('Empty Doube Ended Queue')
        back = (self._front+self._size-1)%len(self._data)
        return self._data[back]

    def add_first(self, e):
        if self.at_max_cap():
            self.resize(len(self._data)*2)
        next_availale = (self._front-1)%len(self._data)
        self._data[next_availale] = e
        self._front = next_availale
        self._size+=1
        
        
    def add_last(self, e):
        if self.at_max_cap():
            self.resize(len(self._data)*2)
        next_available  = (self._front + self._size) %len(self._data)
        self._data[next_available] = e
        self._size+=1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Empty Queue')
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)
        self._size-=1
        # reduce capacity to 1/2 if size is at or below 1/4 of capacity
        if 0 < self._size < len(self._data)//4:
            self.resize_l(len(self._data)//2)
        
    def remove_last(self):
        if self.is_empty():
            raise Empty('Empty Queue')

        back  = (self._front + self._size-1) %len(self._data)
        self._data[back] = None
        self._size-=1

    def resize_l(self, new_len):
        old_data = self._data
        self._data = [None]*new_len
        step = self._front
        for i in range(len(self._data)):
            self._data[i] = old_data[step]
            step = (step+1)%len(old_data)
        self._front = 0

    def resize(self, new_len):
        old_data = self._data
        self._data = [None]*new_len
        step = self._front
        for i in range(len(old_data)):
            self._data[i] = old_data[step]
            step = (step+1)%len(old_data)
        self._front = 0

    def to_string(self):
        print(self._data)
        

class Node:
    __slots__ = '_item', '_next'

    def __init__(self, item, next=None):
        self._item = item
        self._next = next
    
    def to_string(self):
        print(self._item)


class SinglyLinked:
    def __init__(self, head_item):
        self._head = Node(head_item)

    # O(n) time to insert at tail of list
    def insert_back(self, item):
        cur_node = self._head
        while cur_node._next != None:
            cur_node = cur_node._next
        new_tail = Node(item, None)
        cur_node._next = new_tail
        return

    # O(1) time to insert at head of list
    def insert_front(self, item):
        new_head = Node(item, self._head)
        self._head = new_head
        return

    def insert_sorted(self, item):
        new_node = Node(item, self._head)
        cur_node = new_node
        while cur_node._next != None and cur_node._next._item < new_node._item:
            cur_node = cur_node._next
        new_node._next = cur_node._next
        cur_node._next = new_node if cur_node is not new_node else cur_node._next
        self._head = new_node if new_node._next is self._head else self._head
        return

    def reverse_list(self, prev, cur:Node):
        if cur._next is not None:
            self.reverse_list(cur, cur._next)
        if cur._next is None:
            self._head = cur
        cur._next = prev

    def to_string(self):
        cur_node = self._head
        out = ""
        while cur_node is not None:
            out+=str(cur_node._item)+'-->'
            cur_node = cur_node._next
        out+='None'
        print(out)
        return


class LinkedStack:
    def __init__(self, top=None):
        self._top = top
        self._size = 0 if top is None else 1
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def peek(self):
        if self.is_empty():
            raise('Empty Stack')
        return self._top._item
    
    def push(self, elem):
        if self.is_empty():
            self._top = Node(elem, None)
            self._size=1
        else:
            new_top = Node(elem, self._top)
            self._top = new_top
        return
    
    def pop(self):
        if self.is_empty():
            raise('Empty Stack')
        old_top = self._top
        self._top = self._top._next
        data = old_top._item
        del old_top
        return data

    def to_string(self):
        cur_node = self._top
        out = ""
        while cur_node is not None:
            out+=str(cur_node._item)+'-->'
            cur_node = cur_node._next
        out+='None'
        print(out)
        return


def matching_brackets(delims):
    opens = "({["
    closes = ")}]"
    track = ArrayStack()
    for b in delims:
        if b in opens:
            track.push(b)
            track.to_string()
        elif b in closes:
            if track.is_empty():
                return False
            if track.peek() in opens and opens.index(track.peek()) != closes.index(b):
                return False
            if track.peek() in opens and opens.index(track.peek()) == closes.index(b):
                track.pop()
                track.to_string()
    track.to_string()
    return track.is_empty()


def pret_a_mange_coffee_queue(people):
    # add people to queue:
    coffee_queue = ArrayQueue()
    for person in people:
        coffee_queue.enqueue(person)
        coffee_queue.to_string()
    while not coffee_queue.is_empty():
        print(coffee_queue.first(), " has ordered their latte, and exited the queue!-----")
        coffee_queue.dequeue()
        coffee_queue.to_string()


def main():
    # pret_a_mange_coffee_queue(['Aaran', 'Aaren', 'Aarez', 'Aarman', 'Aaron', 'Aaron-James', 'Aarron', 'Aaryan', 'Aaryn', 'Aayan'])
    # res_list = ['Aaron', 'Aaran', 'Aaren', 'Aarez', 'Aarman', 'Aaron-James', 'Aarron', 'Aaryan', 'Aaryn', 'Aayan']

    # rising_ballers = SinglyLinked(res_list[0])
    # cur_node = rising_ballers._head
    # for baller in res_list[1:]:
    #     cur_node._next = Node(baller)
    #     cur_node = cur_node._next
    # rising_ballers.to_string()

    rand_ints = random.sample(range(0,100),20)
    print(rand_ints)

    # linked_nums = SinglyLinked(rand_ints[0])
    # print('init head: ', linked_nums._head._item)

    # for x in rand_ints[1:]:
    #     linked_nums.insert_sorted(x)
    # linked_nums.to_string()
    # linked_nums.reverse_list(None, linked_nums._head)
    # linked_nums.to_string()

    linked_num_stack = LinkedStack()
    for num in rand_ints:
        linked_num_stack.push(num)
        linked_num_stack.to_string()

    
    return

if __name__ == "__main__":
    main()