matrix = eval(input())
row_sum = [sum(row) for row in matrix]
col_sum =  [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
resul = row_sum + col_sum
print(resul)