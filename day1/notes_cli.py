print("===== Notes App =====")

notes = []

try:
    with open("day1/notes.txt", "r")as file:
        for line in file:
            notes.append(line.strip())

except FileNotFoundError:
    pass


while True:

    print("\n1. add note")
    print("2. view notes")
    print("3. exit")

    choice = input("choose an option: ")
    
    print(f"you chose: {choice}")

    if choice == "1":
        note = input("enter your note:")
        notes.append(note)
        with open("day1/notes.txt", "a")as file:
            file.write(note + "\n")
        print("note added!")

    if choice == "2":
        if len(notes) == 0:
            print("no notes found")

        else:
            print("\nyour notes:")

            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note}")

    if choice == "3":
        print("goodbye!")
        break