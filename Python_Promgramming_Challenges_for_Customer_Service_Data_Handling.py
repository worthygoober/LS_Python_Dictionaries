



def open_new_ticket(tickets, ticket_id, customer, issue):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"Customer" : customer, "Issue" : issue, "Status" : "open"}
        print(f"Service Ticket {ticket_id} has been added by {customer}.")
    else:
        print(f"Service Ticket {ticket_id} already exists.")

def update_ticket_status(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"Service Ticket {ticket_id} status updated to {status}.")
    else:
        print(f"Service Ticket {ticket_id} not found.")

def display_tickets(tickets):
    for tid, details in tickets.items():
        print(f"{tid}, Customer: {details["Customer"]}, Issue: {details["Issue"]}, Status: {details["Status"]}.")

service_tickets = {}

while True:
    print("\nCustomer Service Ticket Tracker")
    print("1: Open New Service Ticket\n2: Update Ticket Status\n3: Display Service Tickets\n4: Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        tid = input("Enter service ticket ID: ")
        cust = input("Enter the customer's name: ")
        reported_issue = input("Enter the customer's issue: ")
        open_new_ticket(service_tickets, tid, cust, reported_issue)
    elif choice == "2":
        tid = input("Enter service ticket ID: ")
        status = input("Enter status (open/closed): ")
        update_ticket_status(service_tickets, tid, status)
    elif choice == "3":
        display_tickets(service_tickets)
    elif choice == "4":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")