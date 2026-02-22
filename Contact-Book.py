import csv
import os

FILENAME = "contacts.csv"


class ContactBook:

    def __init__(self):
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone"])  # Header




    def add_contact(self):
        try:
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            if not name or not phone:
                raise ValueError("All fields are required!")

            # ✅ 10 digit phone validation
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Phone number must be exactly 10 digits!")

            with open(FILENAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, phone])

            print("✅ Contact added successfully!")

        except ValueError as e:
            print("❌ Error:", e)


    def view_contacts(self):
        try:
            with open(FILENAME, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header

                print("\n📒 Contact List")
                print("-" * 40)

                for row in reader:
                    if row:
                        name, phone = row
                        print(f"Name : {name}")
                        print(f"Phone: {phone}")
                        print("-" * 40)

        except Exception as e:
            print("Error reading contacts:", e)

    def search_contact(self):
        search_name = input("Enter name to search: ").strip().lower()
        found = False

        try:
            with open(FILENAME, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    name, phone = row
                    if search_name in name.lower():
                        print("\n🔎 Contact Found")
                        print(f"Name : {name}")
                        print(f"Phone: {phone}")
                        found = True

            if not found:
                print("❌ Contact not found.")

        except Exception as e:
            print("Error searching contact:", e)

    def delete_contact(self):
        delete_name = input("Enter name to delete: ").strip().lower()
        updated_contacts = []
        deleted = False

        try:
            with open(FILENAME, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

                for row in reader:
                    name, phone = row
                    if delete_name != name.lower():
                        updated_contacts.append(row)
                    else:
                        deleted = True

            with open(FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(updated_contacts)

            if deleted:
                print("✅ Contact deleted successfully!")
            else:
                print("❌ Contact not found.")

        except Exception as e:
            print("Error deleting contact:", e)


def main():
    contact_book = ContactBook()

    while True:
        print("\n📌 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.delete_contact()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
