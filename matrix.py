class Matrix:
    _rows: int = None
    _cols: int = None
    _matrix: list[list[int, float]] = None

    def __init__(self, matrix: list[list[int, float]]) -> None:        
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._matrix = matrix

    def __add__(self, other) -> 'Matrix':       
        if not isinstance(other, self.__class__):
            print("Не является матрицей.")
            return
        if self._rows != other._rows or self._cols != other._cols:
            print("Операция невыполнима для матриц разного размера.")
            return
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._matrix[j][i] + other._matrix[j][i]
        return Matrix(new_matrix)

    def __mul__(self, other) -> 'Matrix':        
        if isinstance(other, self.__class__):
            return self.__rmul__(other)
        elif isinstance(other, int) or isinstance(other, float):
            new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
            for i in range(self._rows):
                for j in range(self._cols):
                    new_matrix[i][j] = self._matrix[i][j] * other
            return Matrix(new_matrix)
        else:
            print("Неподдерживаемая операция")
            return

    def __rmul__(self, other) -> 'Matrix':        
        if not isinstance(other, self.__class__):
           print("Не является матрицей.")
           return
        if self._cols != other._rows:
            print("Операция невыполнима если кол-во рядов первой матрицы не соответствует кол-ву столбцов второй матрицы.")
            return
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._rows):
                new_matrix[i][j] = self._matrix[i][j] * other._matrix[j][i]
        return Matrix(new_matrix)

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, self.__class__):
            print("Не является матрицей.")
            return
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for j in range(self._rows):
            for i in range(self._cols):
                if self._matrix[j][i] != other._matrix[j][i]:
                    return False
        return True

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix]) + '\n'

    def __repr__(self):
        return f'Матрица: {self._matrix}'