"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    LETTERS = ["A", "B", "C", "D"]
    result_dict = {}

    for n in range(number):
        result_dict.update([(n, LETTERS.pop(0))])
        if not LETTERS:
            LETTERS = ["A", "B", "C", "D"]
        yield result_dict[n]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    LETTERS = ["A", "B", "C", "D"]
    result_dict = {}

    row = 1
    for n in range(number):
        result_dict.update([(n, (str(row) + LETTERS.pop(0)))])
        if not LETTERS:
            row += 1
            if row == 13:
                row = 14
            LETTERS = ["A", "B", "C", "D"]
        yield result_dict[n]


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names
        of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers
        as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned_seats = {}

    seats = generate_seats(len(passengers))
    for passenger in passengers:
        assigned_seats.update([(passenger, next(seats))])
    return assigned_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        sn_fid = f'{seat_number}{flight_id}'
        zeroes = str(0)*(12-len(sn_fid))
        yield sn_fid+zeroes
