def create_initial_matrix(columns, rows):
  matrix = []
  for _ in range(rows):
    row_arr = []

    for _ in range(columns):
      row_arr.append(0)

    matrix.append(row_arr)  
  return matrix

def next_generation_cell(cell, matrix, row, column):
  counter = 0

  counter += matrix[row - 1][column - 1]
  counter += matrix[row - 1][column]
  counter += matrix[row - 1][(column + 1) % len(matrix[0])]

  counter += matrix[row][column - 1]
  counter += matrix[row][(column + 1) % len(matrix[0])]

  counter += matrix[(row + 1) % len(matrix)][column - 1]
  counter += matrix[(row + 1) % len(matrix)][column]
  counter += matrix[(row + 1) % len(matrix)][(column + 1) % len(matrix[0])]

  if (cell == 0 and counter == 3):
    return 1
  elif (cell == 1 and (counter == 2 or counter == 3)):
    return 1
  else:
    return 0

def generate_next_generation(matrix):
  generation_matrix = create_initial_matrix(len(matrix[0]), len(matrix)) 

  for row in range(len(matrix)):
    for column in range(len(matrix[0])):
      cell = matrix[row][column]
      generation_matrix[row][column] = next_generation_cell(cell, matrix, row, column)

  return generation_matrix

def run_simulation(matrix, generation_counter, file_name):
  generation_matrix = generate_next_generation(matrix)

  generation_counter -= 1

  if (generation_counter == 0):
    with open(file_name, 'w+') as result_file:
      for row in generation_matrix:
        result_file.write(''.join([str(i) for i in row]).replace('0', '.').replace('1', 'x') + '\n')
    return generation_matrix

  run_simulation(generation_matrix, generation_counter, file_name)