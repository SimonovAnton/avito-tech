import asyncio
import aiohttp
from typing import List


# Фнкция считывает txt файл по URL
async def matrix_from_url(url: str) -> List[str]:
    async with aiohttp.ClientSession() as session:
        for _ in range(10):    # В случае неудачи запрос повторяется 10 раз с интервалом 0.2 секунды
            try:
                async with session.get(url) as resp:
                    assert resp.status == 200
                    matrix_initial = await resp.text()
                    matrix_initial = matrix_initial.split('\n')
                    return matrix_initial
            except AssertionError:   # Вызывается исключение, если код ответа HTTP не равен 200
                print('{url} finished with status: {status}'.format(url=url, status=resp.status))
                await asyncio.sleep(0.2)
            except aiohttp.ClientError as e:    # Ошибка подключения
                print('{url}: Connection error: {e}'.format(url=url, e=e))
                await asyncio.sleep(0.2)


# Преобразует исходную матрицу в матрицу INT
def matrix_prepare(matrix_initial: List, sep: str = '|') -> List[List[int]]:
    matrix = []
    for row in matrix_initial:
        if not row:
            continue
        if row[0] == sep:
            numbers = [int(i) for i in row.replace(sep, '').split()]
            matrix.append(numbers)
    return matrix


# Функция возвращает список элементов матрицы против часовой стрелки
def matrix_spiral_l(matrix_initial: List) -> List[int]:
    result = []
    matrix = matrix_prepare(matrix_initial)
    n = len(matrix)  # Размерность матрицы
    for lvl in range(n // 2):  # Контуры обхода
        for i in range(lvl, n - lvl):  # Левая граница
            result.append(matrix[i][lvl])
        for i in range(1 + lvl, n - 1 - lvl):  # Нижняя граница
            result.append(matrix[n - lvl - 1][i])
        for i in range(lvl, n - lvl):  # Правая граница
            result.append(matrix[n - 1 - i][n - 1 - lvl])
        for i in range(1 + lvl, n - 1 - lvl):  # Верхняя граница
            result.append(matrix[lvl][n - 1 - i])
    if n % 2 == 1:  # Добавление центрального элемента
        result.append(matrix[n // 2][n // 2])
    return result


# Функция единственным аргументом получает URL для загрузки матрицы с сервера по протоколу HTTP(S).
# Функция возвращает список, содержащий результат обхода полученной матрицы по спирали: против часовой стрелки,
# начиная с левого верхнего угла.
async def get_matrix(url: str) -> List[int]:
    try:
        matrix = matrix_spiral_l(await matrix_from_url(url))
        return matrix
    except Exception as error:
        print(Exception('{url} finished with error: {error}'.format(url=url, error=error)))


if __name__ == '__main__':
    URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    loop = asyncio.get_event_loop()
