# Welcome message
print("Welcome to Bus Ticket Reservation System\n")

# Dictionary of available routes and their fixed prices
routes = {
    "Mumbai to Pune": 500,
    "Delhi to Jaipur": 600,
    "Ahmedabad to Surat": 400
}

# Dictionary to store all booked tickets using ticket ID as key
tickets = {}

# Counter to generate unique ticket IDs
ticket_id_counter = 1

# Start a loop to show menu until user chooses to exit
while True:
    print("\nMenu:")
    print("1. Show Available Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    # Take user choice
    choice = input("Enter your choice (1-5): ")

    # Option 1: Show all available routes and their prices
    if choice == "1":
        print("\nAvailable Routes and Prices:")
        for route, price in routes.items():
            print(f"{route} - ₹{price}")

    # Option 2: Book a ticket
    elif choice == "2":
        print("\n--- Book Ticket ---")
        name = input("Enter passenger name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")

        # Display available routes for selection
        print("\nChoose route:")
        for i, route in enumerate(routes):
            print(f"{i+1}. {route} - ₹{routes[route]}")

        # User selects route number
        route_choice = int(input("Enter route number: ")) - 1

        # Convert route dictionary keys to list to select by index
        route_list = list(routes.keys())

        # Check if route number is valid
        if route_choice >= 0 and route_choice < len(route_list):
            route_selected = route_list[route_choice]

            # Count how many tickets are already booked on this route
            seat_count = 0
            for t in tickets.values():
                if t['route'] == route_selected:
                    seat_count += 1

            # Check seat availability (maximum 40 seats)
            if seat_count < 40:
                # Create unique ticket ID like T1, T2, T3...
                ticket_id = "T" + str(ticket_id_counter)
                ticket_id_counter += 1

                # Store ticket info in dictionary
                tickets[ticket_id] = {
                    'name': name,
                    'age': age,
                    'mobile': mobile,
                    'route': route_selected,
                    'seat_no': seat_count + 1
                }

                print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
            else:
                print("Sorry, bus is full for this route.")
        else:
            print("Invalid route selection.")

    # Option 3: View ticket details using ticket ID
    elif choice == "3":
        print("\n--- View Ticket ---")
        tid = input("Enter Ticket ID: ")
        if tid in tickets:
            t = tickets[tid]
            print(f"Passenger Name: {t['name']}")
            print(f"Age: {t['age']}")
            print(f"Mobile: {t['mobile']}")
            print(f"Route: {t['route']}")
            print(f"Seat No: {t['seat_no']}")
        else:
            print("Ticket not found.")

    # Option 4: Cancel ticket by ID
    elif choice == "4":
        print("\n--- Cancel Ticket ---")
        tid = input("Enter Ticket ID to cancel: ")
        if tid in tickets:
            del tickets[tid]  # Remove ticket from dictionary
            print("Ticket cancelled successfully.")
        else:
            print("Ticket ID not found.")

    # Option 5: Exit the system
    elif choice == "5":
        print("Exiting the system. Thank you!")
        break  # Break the while loop to exit program

    # If user enters invalid choice
    else:
        print("Invalid choice. Please enter between 1 to 5.")
