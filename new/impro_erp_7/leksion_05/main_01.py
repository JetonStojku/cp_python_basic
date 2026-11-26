def hello_world(name="", surname=""):
    print(f"Hello {name} {surname}!")
    print("Welcome to my world!")
    print("-" * 28)


lastname = input("Enter you name: ")
hello_world(surname=lastname)
hello_world(surname="Ben", name="Prifti")
hello_world("Din", "Hoxha")
hello_world()
