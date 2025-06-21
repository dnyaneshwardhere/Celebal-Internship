# Node class to represent a single element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the end
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to print the entire list
    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to delete the nth node (1-based index)
    def delete_nth_node(self, n):
        try:
            if n <= 0:
                raise ValueError("Index should be a positive integer.")

            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n == 1:
                self.head = self.head.next
                return

            current = self.head
            count = 1
            prev = None

            while current and count < n:
                prev = current
                current = current.next
                count += 1

            if not current:
                raise IndexError("Index out of range.")

            prev.next = current.next

        except (ValueError, IndexError) as e:
            print("Error:", e)


# Sample usage for testing
if __name__ == "__main__":
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)

    print("Initial linked list:")
    ll.print_list()

    print("\nDeleting 3rd node:")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nAttempting to delete 10th node (out of range):")
    ll.delete_nth_node(10)

    print("\nDeleting 1st node:")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDeleting remaining nodes:")
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete from empty list:")
    ll.delete_nth_node(1)
