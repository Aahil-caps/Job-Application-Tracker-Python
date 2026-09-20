jobs = []

while True:

    print("\n===== Job Application Tracker =====")
    print("1. Add Job")
    print("2. View Jobs")
    print("3. Search Job")
    print("4. Exit")

    choice = int(input("Enter choice from 1-4: "))

    if choice == 1:

        a = input("Enter Company Name: ")
        b = input("Enter Job Role: ")
        c = input("Enter Location: ")
        d = input("Enter Status: ")

        user = (a, b, c, d)
        jobs.append(user)

        print("Job Added Successfully!")

    elif choice == 2:

        for job in jobs:
            print(job)

    elif choice == 3:

        print("Search Job selected")

    elif choice == 4:

        print("Goodbye!")
        break

    else:

        print("Invalid choice")