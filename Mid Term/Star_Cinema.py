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

            if self.__seats[id][row][col] == 'booked':
                print(f"Seat ({row}, {col}) is already booked.")
            self.__seats[id][row][col] = 'booked'

    def view_show_list(self):
        print("Show List:\n")
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
                    print(f"({row},{col})", end='=0 ')
                else:
                    print(end=' Booked ')
            print()
        print()


# row, col, hall_no
hall_1 = Hall(6, 6, 1)

# Adding shows
hall_1.entry_show("S1", "Movie A", "03:00 PM")
hall_1.entry_show("S2", "Movie B", "07:00 PM")

# View show list
hall_1.view_show_list()

# View available seats, if someone gives awrong id of a show
hall_1.view_available_seats("S3")

# View available seats when all seats are available
hall_1.view_available_seats("S1")

# Book some seats, if someone tries to book a seat that is invalid
hall_1.book_seats("S1", [(0, 5), (8, 2)])

# Book some seats for a show
hall_1.book_seats("S1", [(0, 1), (0, 2)])

# if someone tries to book a seat that is already booked
print()
hall_1.book_seats("S1", [(0, 1), (0, 2)])

# View available seats after some seat booked
hall_1.view_available_seats("S1")


# output :::::::::
"""
Show List:

ID: S1, Movie: Movie A, Time: 03:00 PM
ID: S2, Movie: Movie B, Time: 07:00 PM

Show with ID S3 does not exist.


Available seats for show S1:
(0,0)=0 (0,1)=0 (0,2)=0 (0,3)=0 (0,4)=0 (0,5)=0 
(1,0)=0 (1,1)=0 (1,2)=0 (1,3)=0 (1,4)=0 (1,5)=0 
(2,0)=0 (2,1)=0 (2,2)=0 (2,3)=0 (2,4)=0 (2,5)=0 
(3,0)=0 (3,1)=0 (3,2)=0 (3,3)=0 (3,4)=0 (3,5)=0 
(4,0)=0 (4,1)=0 (4,2)=0 (4,3)=0 (4,4)=0 (4,5)=0 
(5,0)=0 (5,1)=0 (5,2)=0 (5,3)=0 (5,4)=0 (5,5)=0 

Invalid seat position: (8, 2)

Seat (0, 1) is already booked.
Seat (0, 2) is already booked.

Available seats for show S1:
(0,0)=0  Booked  Booked (0,3)=0 (0,4)=0  Booked 
(1,0)=0 (1,1)=0 (1,2)=0 (1,3)=0 (1,4)=0 (1,5)=0 
(2,0)=0 (2,1)=0 (2,2)=0 (2,3)=0 (2,4)=0 (2,5)=0 
(3,0)=0 (3,1)=0 (3,2)=0 (3,3)=0 (3,4)=0 (3,5)=0 
(4,0)=0 (4,1)=0 (4,2)=0 (4,3)=0 (4,4)=0 (4,5)=0 
(5,0)=0 (5,1)=0 (5,2)=0 (5,3)=0 (5,4)=0 (5,5)=0 


"""
