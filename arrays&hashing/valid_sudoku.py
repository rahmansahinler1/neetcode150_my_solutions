class Solution(object):
    def isValidSudoku(self, board):
        numbers = ['0', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9', 
                   '.']
        for i in range(9):
            row_holder = []  
            for j in range(9):
                cell_value = board[i][j]
                if cell_value == '.':
                    continue
                elif (cell_value in numbers) and (cell_value not in row_holder):  
                    row_holder.append(cell_value)
                else:
                    return False

        for j in range(9):
            column_holder = []  # empty list for each row before checking
            for i in range(9):
                cell_value = board[i][j]
                if cell_value == '.':
                    continue
                if (cell_value in numbers) and (cell_value not in column_holder): 
                    column_holder.append(cell_value)
                else:
                    return False
        
        row_start_value = 0
        column_start_value = 0
        for _ in range(3):
            for _ in range(3):
                square_holder = []
                for i in range(row_start_value, row_start_value + 3):
                    for j in range(column_start_value, column_start_value + 3):
                        cell_value = board[i][j]
                        if cell_value == '.':
                            continue
                        elif (cell_value in numbers) and (cell_value not in square_holder):
                            square_holder.append(cell_value)
                        else:
                            return False
                column_start_value += 3
            row_start_value += 3
            column_start_value = 0 
        
        return True
        