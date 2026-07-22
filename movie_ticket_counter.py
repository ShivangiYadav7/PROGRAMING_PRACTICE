
    # Movie Ticket Counter

tickets = 30

while tickets > 0:
    print("\n=== WELCOME TO MOVIE TICKET COUNTER ===")
    print(f"Available Tickets: {tickets}")

    customer = int(input("How many tickets do you want? "))

    if customer <= tickets:
        tickets -= customer
        print(f"\n🎉 {customer} ticket(s) booked successfully.")
        print(f"Remaining tickets: {tickets}")

        if tickets == 0:
            print("\n🎬 House Full!")
            break

    else:
        print("\n❌ Sorry! Not enough tickets available.")