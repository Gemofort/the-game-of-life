import pytest

from helpers import create_initial_matrix, next_generation_cell, generate_next_generation, run_simulation

input_file = open('test_input.txt', 'r')
lines = input_file.readlines()
input_file.close()

generations = int(lines[0])
columns, rows = [int(i) for i in lines[1].split(' ')]
input_matrix = [[int(i) for i in list(line.replace('\n', '').replace('.', '0').replace('x', '1'))] for line in lines[2:]]

initial_matrix = create_initial_matrix(columns, rows)

for i in range(len(initial_matrix)):
  for j in range(len(initial_matrix[i])):
    try:
      initial_matrix[i][j] = input_matrix[i][j]
    except (IndexError):
      pass

def test_initial_matrix():
  matrix = create_initial_matrix(columns, rows)
  assert len(matrix) == rows and len(matrix[0]) == columns

def test_initial_matrix_wrong():
  matrix = create_initial_matrix(columns, rows)
  assert len(matrix) != rows + 1 and len(matrix[0]) != columns + 1

def test_next_generation_cell():
  result = 0
  row = 0
  column = 0
  matrix = input_matrix
  cell = input_matrix[row][column]

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
    result = 1
  elif (cell == 1 and (counter == 2 or counter == 3)):
    result = 1
  else:
    result = 0

  assert result == next_generation_cell(0, input_matrix, 0, 0)

def test_next_generation_cell_becomes_one():
  assert 1 == next_generation_cell(input_matrix[2][1] , input_matrix, 2, 1)

def test_next_generation_cell_becomes_zero():
  assert 0 == next_generation_cell(input_matrix[1][2] , input_matrix, 1, 2)

def test_next_generation_cell_remains_zero():
  assert 0 == next_generation_cell(input_matrix[0][0] , input_matrix, 0, 0)

def test_next_generation_cell_remains_one():
  assert 1 == next_generation_cell(input_matrix[2][2] , input_matrix, 2, 2)

# test wrong next_generation_cell_results
def test_next_generation_cell_becomes_one_wrong():
  assert 0 != next_generation_cell(input_matrix[2][1] , input_matrix, 2, 1)

def test_next_generation_cell_becomes_zero_wrong():
  assert 1 != next_generation_cell(input_matrix[1][2] , input_matrix, 1, 2)

def test_next_generation_cell_remains_zero_wrong():
  assert 1 != next_generation_cell(input_matrix[0][0] , input_matrix, 0, 0)

def test_next_generation_cell_remains_one_wrong():
  assert 0 != next_generation_cell(input_matrix[2][2] , input_matrix, 2, 2)

def test_generate_next_generation():
  next_matrix = generate_next_generation(input_matrix)

  for row in range(len(next_matrix)):
    for column in range(len(next_matrix[0])):
      cell = input_matrix[row][column]
      assert next_matrix[row][column] == next_generation_cell(cell, input_matrix, row, column)

def test_run_simulation():
  run_simulation(input_matrix, generations, 'test_result.txt')
  run_simulation(input_matrix, generations, 'test_result_v2.txt')

  with open('test_result.txt') as f1, open('test_result_v2.txt') as f2:
    line_file1 = f1.readlines()
    line_file2 = f2.readlines()
  
    for index in range(len(line_file1)):
      assert line_file1[index] == line_file2[index]
