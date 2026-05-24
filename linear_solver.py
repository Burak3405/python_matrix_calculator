import numpy as np

def add_matrices(matrix_a, matrix_b):
    return np.add(matrix_a, matrix_b)

def multiply_matrices(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def find_transpose(matrix):
    return np.transpose(matrix)

def find_inverse(matrix):
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "Singular matrix, inverse does not exist."

def get_matrix_size():
    while True:
        try:
            size = int(input("\nEnter the size N for the NxN square matrices: "))
            if size <= 0:
                print("Size must be positive integer greater than 0.")
                continue
            return size
        except ValueError:
            print("Invalid input. Please enter an integer")

def get_matrix_input(matrix_name, size):
    # Gets an NxN matrix input
    print(f"\nEntering values for {matrix_name} ({size}x{size} Matrix)")
    matrix = []
    
    for i in range(size):
        while True:
            try:
                row_input = input(f"Enter {size} numbers for row {i+1} (separated by space): ")
                
                row = [float(val) for val in row_input.split()]
                
                if len(row) != size:
                    print(f"Please enter exactly {size} numbers.")
                    continue
                
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                
    return np.array(matrix)

def main():
    while True:
        print("**** Linear Algebra Solver ****")
    
        matrix_size = get_matrix_size()
        matrix_x = get_matrix_input("Matrix X", matrix_size)
        matrix_y = get_matrix_input("Matrix Y", matrix_size)

        print("\nMatrix X:")
        print(matrix_x)
        print("\nMatrix Y:")
        print(matrix_y)

        print("\n1. Addition (X + Y):")
        print(add_matrices(matrix_x, matrix_y))

        print("\n2. Multiplication (X * Y):")
        print(multiply_matrices(matrix_x, matrix_y))

        print("\n3. Determinant of Matrix X:")
        print(calculate_determinant(matrix_x))

        print("\n4. Transpose of Matrix Y:")
        print(find_transpose(matrix_y))
    
        print("\n5. Inverse of Matrix X:")
        print(find_inverse(matrix_x))

        repeat = input("\nWould you like to try another operation? (y/n): ").strip().lower()
        if repeat != 'y':
            print("\n ****See you next time****")
            break 

if __name__ == "__main__":
    main()