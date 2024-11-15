from node import Node


def display(head):
    temp = head
    while temp != None:
        print(f"{temp.data}->", end="")
        temp = temp.next
    print()


def displayRecursive():
    pass


def sumList(head):
    temp = head
    total = 0
    while temp != None:
        total += temp.data
        temp = temp.next
    return total


def countList(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    return count


def maxElement():
    pass


def insertAtHead(head, data):
    newNode = Node(data=data)
    newNode.next = head
    head = newNode
    return head


def insertAtTail():
    pass


def insertAfterElement(head, element, data):
    temp = head
    while temp != None:
        if temp.data == element:
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
            break
        temp = temp.next
    return head


def deleteAtHead(head):
    head = head.next
    return head


def deleteAtPosition(head, position):
    if position == 1:
        return deleteAtHead(head)
    prev = None
    curr = head
    currPos = 1
    while curr != None:
        if currPos == position:
            prev.next = curr.next
            curr.next = None
            break
        prev = curr
        curr = curr.next
        currPos += 1
    return head


def main():
    head = Node(10)
    head = insertAtHead(head=head, data=20)
    head = insertAtHead(head=head, data=80)
    head = insertAtHead(head=head, data=200)
    head = insertAfterElement(head, 20, 33)
    head = insertAfterElement(head, 10, 433)
    head = insertAfterElement(head, 200, 1433)
    display(head)
    total = sumList(head)
    print("total is", total)
    count = countList(head)
    print("count is", count)
    head = deleteAtHead(head)
    display(head)
    head = deleteAtPosition(head, 2)
    display(head)


if __name__ == "__main__":
    main()
