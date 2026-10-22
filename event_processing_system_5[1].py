from collections import deque
queue = deque()
while True:
    print("\n-- Event Processing System---")
    print("1.Add Event")
    print("2.Process Next Events")
    print("3.Display Pending Events")
    print("4.Cancle Event")
    print("5.Exit")
    choice=int(input("Enter your choices:"))
    if choice==1:
        event=input("Enter event:")
        queue.append(event)
        print("Enter added:",event)
    elif choice==2:
        if queue:
            event=queue.popleft()
            print("event processed:",event)
        else:
            print("Queue is empty.")
    elif choice==3:
        if queue:
            print("Pending Events:",list(queue))
        else:
            print("No pending events.")
    elif choice==4:
        event=input("Enter event to cancle:")
        if event in queue:
            queue.remove(event)
            print("Event cancelled:",event)
        else:
            print("Event not found.")
    elif choice==5:
        print("program ended.")
        break
    else:
        print("Invalid choice.")

               