from datetime import date


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} (ID: {self.student_id})"


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.city}, {self.street}, {self.zip_code} | "
            f"Godziny: {self.open_hours}, Tel: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name} (Data zatrudnienia: {self.hire_date}, "
            f"Miasto: {self.city})"
        )


class Book:
    def __init__(
        self, library, publication_date, author_name, author_surname, number_of_pages
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        library_desc = self.library.city
        return (
            f"Book: {self.author_name} {self.author_surname} ({self.publication_date}), "
            f"{self.number_of_pages} stron. Dostępna w: {library_desc}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_titles = [str(book) for book in self.books]
        books_list_str = "\n    * ".join(book_titles)

        return (
            f"\n--- ORDER #{self.order_date.strftime('%Y%m%d')} ---"
            f"\nData zamówienia: {self.order_date}"
            f"\nObsługujący: {self.employee.first_name} {self.employee.last_name}"
            f"\nKlient: {self.student.first_name} {self.student.last_name}"
            f"\nKsiążki w zamówieniu ({len(self.books)}):"
            f"\n    * {books_list_str}"
        )


# TWÓRZENIE INSTANCJI
library_wroclaw = Library(
    "Wrocław", "ul. Czytelnicza 10", "50-001", "8:00-18:00", "71 111 22 33"
)
library_krakow = Library(
    "Kraków", "ul. Książkowa 5", "30-001", "9:00-17:00", "12 999 88 77"
)

book1 = Book(library_wroclaw, date(2021, 5, 10), "Jan", "Kowalski", 300)
book2 = Book(library_wroclaw, date(2018, 1, 1), "Anna", "Nowak", 150)
book3 = Book(library_wroclaw, date(2023, 11, 20), "Piotr", "Zacny", 450)
book4 = Book(library_krakow, date(2005, 3, 30), "Ewa", "Młynarz", 220)
book5 = Book(library_krakow, date(2022, 7, 7), "Robert", "Leśny", 500)

employee1 = Employee(
    "Marta",
    "Zielińska",
    date(2020, 10, 1),
    date(1990, 5, 15),
    "Wrocław",
    "Słoneczna 1",
    "50-100",
    "71 555 66 77",
)
employee2 = Employee(
    "Tomasz",
    "Wójcik",
    date(2019, 3, 15),
    date(1985, 11, 22),
    "Kraków",
    "Gwiezdna 2",
    "30-200",
    "12 111 22 33",
)
employee3 = Employee(
    "Kasia",
    "Dąbrowska",
    date(2022, 7, 1),
    date(1995, 8, 8),
    "Wrocław",
    "Leśna 3",
    "50-300",
    "71 444 55 66",
)

student1 = Student("Agnieszka", "Krupa", "S001")
student2 = Student("Bartosz", "Lis", "S002")
student3 = Student("Celina", "Bóbr", "S003")

order1 = Order(
    employee=employee1,
    student=student1,
    books=[book1, book2],
    order_date=date(2025, 12, 10),
)

order2 = Order(
    employee=employee2,
    student=student2,
    books=[book3, book4, book5],
    order_date=date(2025, 12, 12),
)

# WYŚWIETLANIE ZAMÓWIEŃ
print(order1)
print(order2)
