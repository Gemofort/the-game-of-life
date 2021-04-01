from helpers import run_simulation, create_initial_matrix

input_file = open('input.txt', 'r')
lines = input_file.readlines()
input_file.close()

generations = int(lines[0])
columns, rows = [int(i) for i in lines[1].split(' ')]
input_matrix = [[int(i) for i in list(line.replace('\n', '').replace('.', '0').replace('x', '1'))] for line in lines[2:]]
print(f'Generations: {generations}')
print(f'Columns: {columns}, Rows: {rows}')

initial_matrix = create_initial_matrix(columns, rows)

for i in range(len(initial_matrix)):
  for j in range(len(initial_matrix[i])):
    try:
      initial_matrix[i][j] = input_matrix[i][j]
    except (IndexError):
      pass

run_simulation(initial_matrix, generations, 'result.txt')