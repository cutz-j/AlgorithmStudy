class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True

            elif target < matrix[row][col]:
                col -= 1

            else:
                row += 1

        return False

    def searchMatrix2(self, matrix, target) -> bool:
        return any(target in row for row in matrix)