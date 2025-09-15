# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, name):
        current = self.head
        prev = None
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return f"{name} has been removed from the waitlist."
            prev = current
            current = current.next
        return f"{name} not found in the waitlist."

    def print_list(self):
        if not self.head:
            print("The waitlist is currently empty.")
            return
        current = self.head
        while current:
            print(current.name, end=" -> " if current.next else "\n")
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program

waitlist_generator()

'''
Design Memo:
This program uses a single linked list to store a waitlist of customers. All customers are stored as a Node,
whose parameters are his name and the next Node reference. LinkedList class manages these
nodes by having the head, which is the starting node of the list. Class methods allow adding a
customer to front, add to end, remove by name, and display full list.

Head is a crucial part because it is the entrance to the list. If the head is destroyed, the entire list is out of reach. Adding to front is achieved by creating a new Node and pointing it
to the current head, then updating head to the new Node. Inserting at the end involves moving
through the list from the head until the last Node is found, then attaching the new Node there. Deletion
involves scanning names one by one and redirecting pointers to skip the Node to be removed.

When I was pondering where a real engineer would put something like that, the first thing that came
something to recall was a doctor's office or a restaurant. There are always people being added to the list as they enter, and sometimes someone has to be pushed up if they have a reservation or an urgent appointment. 
Other times, someone will leave before they are called, so they'd have to be removed
the list. A custom linked list would be a good selection for that kind of situation because it's easy, simple, and lets you handle changes along the way.
'''
