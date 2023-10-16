# Start from Monday and go through the 7 days of the week
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

    print("\nYour Weekly Routine:")
    for i in range(7):
        gym_indicator = "X" if i < Mornings else " "
        books_indicator = "X" if i < Nights else " "
        print(f"{days[i]}: Gym [{gym_indicator}] Books [{books_indicator}]")

    print("\nMotivational Feedback:")
    if Mornings > 3 and Nights > 3:
        print("Congratulations! You're on a fantastic path to a healthy and knowledgeable life.")
    elif Mornings < 3 and Nights > 3:
        print("Reading books is great, but consider adding some physical activity to your routine.")
    elif Mornings > 3 and Nights < 3:
        print("Keep up the gym routine, but don't forget to nourish your mind with books.")
    else:
        print("Don't worry; everyone has their own routine. Keep improving!")

date()
