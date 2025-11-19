def transpose_matrix(matrix): 
    # Use list comprehension to transpose 
    return[[row[i] for row in matrix] for i in range(len(matrix[0]))] 
 
# Example 
matrix = [[1, 2], [3, 4], [5, 6]] 
output= transpose_matrix(matrix) 
print(output) 