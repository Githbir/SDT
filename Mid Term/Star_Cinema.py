class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)
        self.__seats = {}  # Dictionary
        self.__show_list = []  # tuple
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        make_tuple = (id, movie_name, time)
        self.__show_list.append(make_tuple)

        seats_layout = [['free' for _ in range(
            self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats_layout

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print(f"Show with ID {id} does not exist.")
            return

        for row, col in seat_list:
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                print(f"Invalid seat position: ({row}, {col})")
                continue

            elif self.__seats[id][row][col] == 'booked':
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                self.__seats[id][row][col] = 'booked'
                print(f'Booked the seat of ({row},{col})')
                hall_1.view_available_seats(id)

    def view_show_list(self):
        print("\nShow List:")
        for show in self.__show_list:
            show_id, movie_name, time = show
            print(f"ID: {show_id}, Movie: {movie_name}, Time: {time}")
        print()

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"Show with ID {id} does not exist.\n")
            return

        print(f"\nAvailable seats for show {id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[id][row][col] == 'free':
                    # print(f"({row},{col})", end='=0 ')
                    print(end=' 0 ')
                else:
                    print(end='(1)')
            print()
        print()


# row, col, hall_no
hall_1 = Hall(6, 6, 1)

# Adding shows
hall_1.entry_show("A11", "Movie 12 Fail", "03:00 PM")
hall_1.entry_show("A22", "Movie Doom-3 ", "07:00 PM")


while True:
    print("\n**Welcome!**")
    print("1. View all show list")
    print("2. View available seats, For Target Show")
    print("3. Book Ticket")
    print("4. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        hall_1.view_show_list()

    elif choice == 2:
        show_id = (input('Target show id : '))
        hall_1.view_available_seats(show_id)

    elif choice == 3:
        show_id = (input('Target show id : '))
        row = int(input('Row No : '))
        col = int(input('Col No : '))
        hall_1.book_seats(show_id, [(row, col)])

    elif choice == 4:
        break
    else:
        print("Invalid Input!!X!!")


# Simple Input & Output

"""

**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 1

Show List:
ID: A11, Movie: Movie 12 Fail, Time: 03:00 PM
ID: A22, Movie: Movie Doom-3 , Time: 07:00 PM


**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 2
Target show id : A11

Available seats for show A11:
 0  0  0  0  0  0 
 0  0  0  0  0  0 
 0  0  0  0  0  0 
 0  0  0  0  0  0 
 0  0  0  0  0  0 
 0  0  0  0  0  0 


**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 3
Target show id : A11
Row No : 0  
Col No : 0
Booked the seat of (0,0)

Available seats for show A11:
(1) 0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0
 0  0  0  0  0  0


**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 3
Target show id : A11
Row No : 0
Col No : 0
Seat (0, 0) is already booked.

**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 3
Target show id : A11
Row No : 0  
Col No : 9
Invalid seat position: (0, 9)

**Welcome!**
1. View all show list
2. View available seats, For Target Show
3. Book Ticket
4. Exit
Enter your choice : 4

"""
