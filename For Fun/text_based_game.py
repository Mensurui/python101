# Start from Monday and go through to the 7 days of the week
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

def date():
    Mornings = 0
    Nights = 0
    print("Welcome to your weekly routine tracker!")
    for i in range(7):
        print(f"\n{days[i]}'s Routine:")
        valueGym = input("Did you go to the gym in the morning? (Y/N): ").upper()
        valueBooks = input("Did you read books at night? (Y/N): ").upper()

        if valueGym == "Y":
            Mornings += 1
        if valueBooks == "Y":
            Nights += 1

    print("\nWeekly Routine Summary:")
    print(f"Total mornings at the gym: {Mornings} days")
    print(f"Total nights reading books: {Nights} days")

    if Mornings > 3 and Nights > 3:
        print("You are on the right path to a healthy and knowledgeable life!")
    elif Mornings < 3 and Nights > 3:
        print("Reading books is great, but consider adding some physical activity to your routine.")
    elif Mornings > 3 and Nights < 3:
        print("Keep up the gym routine, but don't forget to nourish your mind with books.")
    else:
        print("Don't worry; everyone has their own routine. Keep improving!")

date()
