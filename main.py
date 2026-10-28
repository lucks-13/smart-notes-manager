from note import Note
from storage import save_notes, load_notes

notes = load_notes

while True:
    print("====== Smart Notes Manager ======\n")
    print("1. Create a note")
    print("2. View all notes")
    print("3. Update a note")
    print("4. Delete a note")
    print("5. Search notes")
    print("6. Exit.")

    try:
        x = int(input("Choose an option :"))
    except ValueError:
        print("Please enter te valid number.")
        continue

    if x==1:
        print("option 1")
    elif x==2:
        print("option 2")
    elif x==3:
        print("option 3")
    elif x==4:
        print("option 4")
    elif x==5:
        print("option 5")
    elif x==6:
        print("Good Bye.")
        break
    else:
        print("Invalid option.")