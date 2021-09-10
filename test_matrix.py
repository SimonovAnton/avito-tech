import matrix
import asyncio

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
OUTPUT = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70
]


def test_get_matrix() -> None:
    loop = asyncio.get_event_loop()
    assert loop.run_until_complete(matrix.get_matrix(SOURCE_URL)) == OUTPUT


SOURCE_URL_BROKEN = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/ilovedogs'


def test_get_matrix_broken_url() -> None:
    loop = asyncio.get_event_loop()
    assert loop.run_until_complete(matrix.get_matrix(SOURCE_URL_BROKEN)) is None


def test_matrix_spiral_l_0element() -> None:
    assert matrix.matrix_spiral_l([]) == []


INPUT1 = [
    '+---+',
    '| 0 |',
    '+---+'
]


def test_matrix_spiral_l_1element() -> None:
    assert matrix.matrix_spiral_l(INPUT1) == [0]


INPUT2 = [
    '+---+---+',
    '| 1 | 2 |',
    '+---+---+',
    '| 3 | 4 |',
    '+---+---+'
]
OUTPUT2 = [1, 3, 4, 2]


def test_matrix_spiral_l_2element() -> None:
    assert matrix.matrix_spiral_l(INPUT2) == OUTPUT2


INPUT3 = [
    '+---+---+---+',
    '| 1 | 2 | 3 |',
    '+---+---+---+',
    '| 4 | 5 | 6 |',
    '+---+---+---+',
    '| 7 | 8 | 9 |',
    '+---+---+---+'
]
OUTPUT3 = [1, 4, 7, 8, 9, 6, 3, 2, 5]


def test_matrix_spiral_l_3element() -> None:
    assert matrix.matrix_spiral_l(INPUT3) == OUTPUT3


INPUT_EMPTY = []


def test_matrix_spiral_l_empty() -> None:
    assert matrix.matrix_spiral_l(INPUT_EMPTY) == []


SEP = '!'
INPUT_SEP = [
    '*...*...*',
    '! 1 ! 2 !',
    '*...*...*',
    '! 3 ! 4 !',
    '*...*...*'
]


def test_matrix_prepare_sep() -> None:
    assert matrix.matrix_prepare(INPUT_SEP, sep=SEP) == [[1, 2], [3, 4]]


INPUT_WITHOUT_NUMBERS = [
    'aaaaa',
    'bbbbb',
    'ccccc',
    'ddddd',
    'eeeee'
]


def test_matrix_spiral_l_without_numbers() -> None:
    assert matrix.matrix_spiral_l(INPUT_WITHOUT_NUMBERS) == []
