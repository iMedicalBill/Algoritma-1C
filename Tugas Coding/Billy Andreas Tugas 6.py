#A. Beberapa contoh tipe data object 
#1. dict (dictionary)
#contoh
person = {
    "name": "Billy",
    "age": 20,
    "is_student": False
}
print(person["name"])  # Output: gabril

#2. Tipe data list
#contoh
fruits = ["apel", "pisang", "nanas"]
print(fruits[1])  # Output: Pisang

#3. tuple
#contoh
coordinates = (10, 20, 30)
print(coordinates[0])  # Output: 10

#4.set
#contoh
angka_unik = {1, 2, 3, 4, 4, 5}
print(angka_unik)  # Output: {1, 2, 3, 4, 5}

#5. string
#contoh
message = "Hello, Python!"
print(message.upper())  # Output: HELLO, PYTHON!



#B. Beberapa contoh tipe data Stack
#1. Menggunakan List
#Contoh
stack = []  # Inisialisasi stack kosong

# Push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)  # Output: [10, 20, 30]

# Pop elemen dari stack
print(stack.pop())  # Output: 30
print(stack)        # Output: [10, 20]

#2. Menggunakan collections.deque
#contoh
from collections import deque

stack = deque()  # Inisialisasi stack kosong

# Push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)  # Output: deque([10, 20, 30])

# Pop elemen dari stack
print(stack.pop())  # Output: 30
print(stack)        # Output: deque([10, 20])

#3. Menggunakan Modul queue.LifoQueue
#Contoh
from queue import LifoQueue

stack = LifoQueue()  # Inisialisasi stack kosong

# Push elemen ke stack
stack.put(10)
stack.put(20)
stack.put(30)

print(stack.qsize())  # Output: 3

# Pop elemen dari stack
print(stack.get())  # Output: 30
print(stack.qsize())  # Output: 2


#C. Beberapa contoh tipe data queue
#1. Menggunakan List
#Contoh
queue = []  # Inisialisasi queue kosong

# Menambahkan elemen ke queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: [1, 2, 3]

# Menghapus elemen dari queue (FIFO)
print(queue.pop(0))  # Output: 1
print(queue)         # Output: [2, 3]

#2. Priority Queue (queue.PriorityQueue)
#Contoh
from queue import PriorityQueue

pq = PriorityQueue()  # Inisialisasi Priority Queue

# Menambahkan elemen dengan prioritas (angka lebih kecil = prioritas lebih tinggi)
pq.put((2, "task2"))
pq.put((1, "task1"))
pq.put((3, "task3"))

# Menghapus elemen berdasarkan prioritas
print(pq.get())  # Output: (1, 'task1')
print(pq.get())  # Output: (2, 'task2')
print(pq.get())  # Output: (3, 'task3')

#3 Implementasi manual dengan kelas
#contoh
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Penggunaan
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.size())     # Output: 2



#D. Beberapa contoh tipe data Linked List
#1. Singly Linked List
#Contoh
class Node:
    def __init__(self, data):
        self.data = data  # Data dalam node
        self.next = None  # Referensi ke node berikutnya

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Node pertama (head)

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Jika linked list kosong
            self.head = new_node
            return
        current = self.head
        while current.next:  # Mencari node terakhir
            current = current.next
        current.next = new_node  # Menambahkan node baru di akhir

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Penggunaan
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.display()  # Output: 10 -> 20 -> 30 -> None

#2. Doubly Linked List
#Contoh
class Node:
    def __init__(self, data):
        self.data = data  # Data dalam node
        self.next = None  # Referensi ke node berikutnya
        self.prev = None  # Referensi ke node sebelumnya

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Node pertama (head)

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Jika linked list kosong
            self.head = new_node
            return
        current = self.head
        while current.next:  # Mencari node terakhir
            current = current.next
        current.next = new_node  # Menambahkan node baru di akhir
        new_node.prev = current  # Mengatur referensi ke node sebelumnya

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Penggunaan
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()  # Output: 10 <-> 20 <-> 30 <-> None

#3. Circular Linked List
#Contoh
class Node:
    def __init__(self, data):
        self.data = data  # Data dalam node
        self.next = None  # Referensi ke node berikutnya

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Node pertama (head)

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Jika linked list kosong
            self.head = new_node
            new_node.next = self.head  # Mengatur agar circular
            return
        current = self.head
        while current.next != self.head:  # Mencari node terakhir
            current = current.next
        current.next = new_node  # Menambahkan node baru di akhir
        new_node.next = self.head  # Menjadikan circular

    def display(self):
        current = self.head
        if not self.head:
            return
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# Penggunaan
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()  # Output: 10 -> 20 -> 30 -> (back to head)
