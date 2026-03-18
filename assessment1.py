# HEALTHCARE MANAGEMENT SYSTEM----------------
class ClinicAppointment:
    def __init__(self):
        self.doctors = ["Dr. Sharma", "Dr. Patel", "Dr. Mehta"]
        self.slots = ["10AM", "11AM", "12PM", "2PM", "3PM"]
        self.appointments = []   # list of dictionaries

    # Show doctors
    def show_doctors(self):
        print("\nAvailable Doctors:")
        for i, doc in enumerate(self.doctors, 1):
            print(i, doc)

    # Show slots
    def show_slots(self):
        print("\nAvailable Time Slots:")
        for i, slot in enumerate(self.slots, 1):
            print(i, slot)

    # Check slot availability (max 3 per doctor per slot)
    def check_availability(self, doctor, slot):
        count = 0
        for appt in self.appointments:
            if appt["doctor"] == doctor and appt["slot"] == slot:
                count += 1
        return count < 3

    # Book appointment
    def book_appointment(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")

        self.show_doctors()
        d_choice = int(input("Select doctor: ")) - 1

        self.show_slots()
        s_choice = int(input("Select time slot: ")) - 1

        doctor = self.doctors[d_choice]
        slot = self.slots[s_choice]

        if self.check_availability(doctor, slot):
            appointment = {
                "name": name,
                "age": age,
                "mobile": mobile,
                "doctor": doctor,
                "slot": slot
            }
            self.appointments.append(appointment)
            print("\n✅ Appointment Booked Successfully!")
        else:
            print("\n❌ Slot Full! Try another time.")

    # View appointment
    def view_appointment(self):
        mobile = input("Enter mobile number: ")
        found = False

        for appt in self.appointments:
            if appt["mobile"] == mobile:
                print("\n📋 Appointment Details:")
                for key, value in appt.items():
                    print(key.capitalize(), ":", value)
                found = True

        if not found:
            print("No appointment found!")

    # Cancel appointment
    def cancel_appointment(self):
        mobile = input("Enter mobile number: ")
        for appt in self.appointments:
            if appt["mobile"] == mobile:
                self.appointments.remove(appt)
                print("❌ Appointment Cancelled!")
                return
        print("No appointment found!")

    # Menu
    def run(self):
        while True:
            print("\n===== Clinic Appointment System =====")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointment()
            elif choice == "3":
                self.cancel_appointment()
            elif choice == "4":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    system = ClinicAppointment()
    system.run()



    
# SCHOOL MANAGEMENT SYSTEM-------------
class SchoolManagement:

    def __init__(self):
        self.students = {}
        self.student_id = 1

    def new_admission(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        student_class = int(input("Enter class (1-12): "))
        mobile = input("Enter mobile: ")

        if age < 5 or age > 18:
            print("Invalid age")
            return

        if len(mobile) != 10:
            print("Invalid mobile")
            return

        sid = self.student_id

        self.students[sid] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print("Student ID:", sid)
        self.student_id += 1


    def view_student(self):
        sid = int(input("Enter student ID: "))
        if sid in self.students:
            print(self.students[sid])
        else:
            print("Student not found")

            
obj = SchoolManagement()
while True:

    print("\n1. New Admission")
    print("2. View Student")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        obj.new_admission()

    elif choice == 2:
        obj.view_student()

    elif choice == 3:
        break

    else:
        print("Invalid choice")


# TRANSPORT RESERVATION SYSTEM----------------
import random

class BusReservation:
    def __init__(self):
        self.routes = {
            1: {"route": "Mumbai to Pune", "price": 500, "seats": 40, "booked": []},
            2: {"route": "Delhi to Jaipur", "price": 600, "seats": 40, "booked": []},
            3: {"route": "Ahmedabad to Surat", "price": 300, "seats": 40, "booked": []},
            4: {"route": "Bangalore to Chennai", "price": 700, "seats": 40, "booked": []}
        }
        
        self.tickets = {}  # ticket_id → ticket details

    # Show available routes
    def show_routes(self):
        print("\nAvailable Routes:")
        for key, value in self.routes.items():
            available_seats = value["seats"] - len(value["booked"])
            print(f"{key}. {value['route']} - ₹{value['price']} | Available Seats: {available_seats}")

    # Generate unique ticket ID
    def generate_ticket_id(self):
        return "T" + str(random.randint(10000, 99999))

    # Book ticket
    def book_ticket(self):
        self.show_routes()
        choice = int(input("\nEnter route number: "))

        if choice not in self.routes:
            print("Invalid route selection!")
            return

        route = self.routes[choice]

        if len(route["booked"]) >= route["seats"]:
            print("No seats available!")
            return

        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        mobile = input("Enter mobile number: ")

        seat_number = len(route["booked"]) + 1
        ticket_id = self.generate_ticket_id()

        ticket = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route["route"],
            "price": route["price"],
            "seat": seat_number
        }

        self.tickets[ticket_id] = ticket
        route["booked"].append(seat_number)

        print("\n✅ Ticket Booked Successfully!")
        print(f"Ticket ID: {ticket_id}")
        print(f"Seat Number: {seat_number}")

    # View ticket
    def view_ticket(self):
        ticket_id = input("Enter Ticket ID: ")

        if ticket_id in self.tickets:
            t = self.tickets[ticket_id]
            print("\n🎫 Ticket Details:")
            for key, value in t.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Ticket not found!")

    # Cancel ticket
    def cancel_ticket(self):
        ticket_id = input("Enter Ticket ID to cancel: ")

        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]

            # Find route and free seat
            for r in self.routes.values():
                if r["route"] == ticket["route"]:
                    r["booked"].remove(ticket["seat"])
                    break

            del self.tickets[ticket_id]
            print("❌ Ticket Cancelled Successfully!")
        else:
            print("Ticket not found!")

    # Main menu
    def run(self):
        while True:
            print("\n===== Bus Reservation System =====")
            print("1. Show Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_routes()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_ticket()
            elif choice == "4":
                self.cancel_ticket()
            elif choice == "5":
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice, try again!")

if __name__ == "__main__":
    system = BusReservation()
    system.run()

