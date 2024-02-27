# Import the libraries
import tkinter
import math

# To provide functionalities
def click(val):
    e = entry.get()  # getting the value
    ans = " "

    try:
        # ln
        if val == "ln":
            ans = math.log(eval(e))

        # degree
        elif val == "1/x":
            if eval(e) == 0:
                entry.delete(0, "end")
                entry.insert(0, "Math error")
                return
            else:
                ans = 1/eval(e)
       
        # abselute
        elif val == "|x|":
            if eval(e) >= 0:
                ans =eval(e)
            else:
                ans =eval(e) * -1

        # Functions
        elif val == "Fn":
            tkobj.withdraw()  # Hide tkobj
            tkobj2.deiconify()  # Show tkobj2
            return
        
        # Matrix
        elif val == "Mx":
            tkobj.withdraw()  # Hide tkobj
            tkobj3.deiconify()  # Show tkobj2
            return

        # degree
        elif val == "deg":
            ans = math.degrees(eval(e))

        # radian
        elif val == "rad":
            ans = math.radians(eval(e))

        # exponential
        elif val == "e":
            ans = math.e
            
        # log2
        elif val == "log2":
            ans = math.log2(eval(e))

        # log10
        elif val == "log10":
            ans = math.log10(eval(e))

        # cos
        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))

        # tan
        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))

        # sin
        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))

        # Square root
        elif val == "√":
            ans = math.sqrt(eval(e))

        # cubic root
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)

        # cosh
        elif val == "cosh":
            ans = math.cosh(eval(e))

        # tanh
        elif val == "tanh":
            ans = math.tanh(eval(e))
            
        # sinh
        elif val == "sinh":
            ans = math.sinh(eval(e))

        # To delete the last char
        elif val == "C":
            e = e[0:len(e) - 1]  # deleting the last char
            entry.delete(0, "end")#clear the field
            entry.insert(0, e)#add the new value
            return

        # To clear the field
        elif val == "CE":
            entry.delete(0, "end")

        # x to the power y
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return

        # cube
        elif val == "x\u00B3":
            ans = eval(e) ** 3

        # square
        elif val == "x\u00B2":
            ans = eval(e) ** 2
   
        # factorial
        elif val == "x!":
            ans = math.factorial(eval(e))
        
        # percentage
        elif val == "%":
            ans = eval(e) /100

        # pi
        elif val == "π":
            ans = math.pi

        # 2π
        elif val == "2π":
            ans = 2 * math.pi

        #division operator
        elif val == "÷":
            entry.insert("end", "/")
            return
        #equal operator
        elif val == "=":
            ans = eval(e)

        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except SyntaxError:
        pass



    tkobj3.withdraw()
    tkobj.deiconify()  
    return

# Create the Window Object
tkobj = tkinter.Tk()
# Set the Windows title
tkobj.title("Scientific Calculator")
#Set the Windows size (W x L)
tkobj.geometry("440x740")
# Set the Windows background color
tkobj.config(bg="light blue")



#The Scientific Calculator Window

# Entry field
entry = tkinter.Entry(tkobj, font=("arial", 20, "bold"), bg="white", fg="Black", bd=10, width=28)
entry.grid(row=0, column=0, columnspan=5)

# Buttons text list
button_list =[ "ln","1/x","|x|","Fn","Mx",
               "deg","rad", "e","log2","log10",
               "cosθ","tanθ","sinθ","√",chr(8731),
               "cosh","tanh","sinh","(", ")",
               "C","CE","x\u02b8","x\u00B3","x\u00B2",
               "7","8","9","x!","%",
               "4","5","6","π","2π",
               "1","2","3","*",chr(247),
               "0",".","=","+","-"]

# Loop to get the buttons on the Window
r = 1
c = 0
for i in button_list:
    # Buttons
    button = tkinter.Button(tkobj, width=5, height=2, bd=2, text=i,  bg="light blue", fg="Black",
                            font=("arial", 17, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 4:
       r += 1
       c = 0
                        ####################################################
#The Function Calculator Window
tkobj2 = tkinter.Tk()
tkobj2.withdraw()
tkobj2.title("Function Calculator")
tkobj2.geometry("440x420")
tkobj2.config(bg="light blue")

def solve_linear_equation(a, b):
    # Check if the equation is linear (a cannot be 0)
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")

    # Solve for x: x = -b/a
    x = -b / a
    return x
def solve_linear_system(a1, b1, c1, a2, b2, c2):
    # Calculate the determinant
    determinant = a1 * b2 - a2 * b1

    # Check if the system has a unique solution
    if determinant == 0:
        return ValueError("The system does not have a unique solution.")

    # Solve for x and y
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return [x, y]
def solve_quadratic_equation(a, b, c):

        discriminant = b ** 2 - 4 * a * c
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
def solve_cubic_equation(a, b, c, d):
    # Calculate the discriminant
    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = ((delta1 + (delta1**2 - 4*delta0**3)**0.5) / 2)**(1/3)
    if C == 0:
        z1 = -b / (3*a)
    else:
        z1 = -1/(3*a) * (b + C + delta0/C)
    
    # Calculate the remaining roots using the known root z1
    A = a
    B = b + a*z1
    C = c + b*z1 + a*z1**2
    delta = B**2 - 4*A*C
    if delta.real > 0:
        z2 = (-B + delta**0.5) / (2*A)
        z3 = (-B - delta**0.5) / (2*A)
    elif delta.real == 0:
        z2 = -B / (2*A)
        z3 = -B / (2*A)
    else:
        real_part = -B / (2*A)
        imaginary_part = (-delta)**0.5 / (2*A)
        z2 = complex(real_part, imaginary_part)
        z3 = complex(real_part, -imaginary_part)

    return [z1, z2, z3]
def Back2():
    tkobj2.withdraw()
    tkobj.deiconify()  
    return
# To provide functionalities
def click2(val):
    e = entry2.get()  # getting the value
    ans = " "
    try:
        if val == "linear'\na,b":
            # Parse the input string to extract coefficients a and b
            a, b = map(float, e.split(","))
            ans = solve_linear_equation(a, b)
        elif val == "quad'\nequ":
            a, b, c = map(float, e.split(","))
            ans = solve_quadratic_equation(a, b, c)
        elif val == "Cubic'\nequ":
            a, b, c, d = map(float, e.split(","))
            ans = solve_cubic_equation(a, b, c, d)
        elif val == "2 eq":
            entry6.grid(row=1, column=0, columnspan=5)
            entry2.delete()
        elif val == "Clear":
            entry6.grid_remove()
            entry2.clipboard_clear()
        elif val == "linear'\nSystem":
            b= entry6.get()
            a1, b1, c1= map(float, e.split(","))
            a2, b2, c2= map(float, b.split(","))
            ans = solve_linear_system(a1, b1, c1, a2, b2, c2)
        elif val == "Back":
            Back2()
        else:
            entry2.insert("end", val)
            return


        entry2.delete(0, "end")
        entry6.delete(0, "end")
        entry2.insert(0, ans)
    except (ValueError, ZeroDivisionError) as e:
        entry2.delete(0, "end")
        entry2.insert(0, "Error: " + str(e))

# Entry field
entry6 = tkinter.Entry(tkobj2, font=("arial", 20, "bold"), bg="white", fg="Black", bd=10, width=28)
entry2 = tkinter.Entry(tkobj2, font=("arial", 20, "bold"), bg="white", fg="Black", bd=10, width=28)
entry2.grid(row=0, column=0, columnspan=5)

# Buttons text list
button_list2 =["7","8","9",",","Back",
               "4","5","6","2 eq","Clear",
               "1","2","3","quad'\nequ","Cubic'\nequ",
               "0",".","","linear'\na,b","linear'\nSystem"]

# Loop to get the buttons on the Function Window
r = 5
c = 0
for i in button_list2:
    # Buttons
    button2 = tkinter.Button(tkobj2, width=5, height=2, bd=2, text=i, bg="light blue", fg="black",
                            font=("arial", 17, "bold"), command=lambda button=i: click2(button))
    button2.grid(row=r, column=c, pady=1)
    c += 1
    if c > 4:
       r += 1
       c = 0

                        ####################################################

                        ####################################################
#The Matrix Calculator Window
tkobj3 = tkinter.Tk()
tkobj3.withdraw()
tkobj3.title("Matrix Calculator")
tkobj3.geometry("440x420")
tkobj3.config(bg="light blue")

def parse_matrices(matrices_str):
    if matrices_str == ''or matrices_str == ' ' :
        return
    matrices_str = matrices_str.strip()
    matrix_strings = matrices_str.split(']],[[')
    matrices = []
    for matrix_str in matrix_strings:
        matrix_str = matrix_str.strip('[]')
        rows = matrix_str.split('],[')
        matrix = []
        for row in rows:
            elements = row.split(',')
            row_values = [float(element) for element in elements]
            matrix.append(row_values)
        matrices.append(matrix)
    return matrices
def parse_matrices1(matrices_str):
    if not matrices_str.strip():
        return []

    matrices = []
    for row in matrices_str.split("],["):
        matrix = []
        for value in row.replace("[", "").replace("]", "").split(","):
            matrix.append(float(value))
        matrices.append(matrix)
    
    return matrices
def add_matrices(matrices):
    if not matrices:
        return None
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrices[0][0]))] for _ in range(len(matrices[0]))]
    for matrix in matrices:
        if len(matrix) != len(result) or len(matrix[0]) != len(result[0]):
            return ValueError("Matrices must be of the same size.")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # Accumulate the values directly without conversion
                result[i][j] += matrix[i][j]
    return result
def subtract_matrices(matrices):
    if not matrices:
        return None
    # Initialize the result matrix as a copy of the first matrix
    result = [row.copy() for row in matrices[0]]
    for matrix in matrices[1:]:
        if len(matrix) != len(result) or len(matrix[0]) != len(result[0]):
            raise ValueError("Matrices must be of the same size.")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # Subtract the corresponding elements
                result[i][j] -= matrix[i][j]
    return result
def multiply_matrices(matrices):
    if not matrices:
        return None
    result = matrices[0]
    for matrix in matrices[1:]:
        if len(result[0]) != len(matrix):
            return ValueError("Matrices are not compatible for multiplication.")
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in result]
    return result
def scalar_multiply_matrices(scalar_str, matrices):
    scalar = int(scalar_str)  # Convert string to integer
    if not matrices:
        return None
    result = []
    # Wrap the single matrix in a list
    if not isinstance(matrices[0][0], list):
        matrices = [matrices]
    for matrix in matrices:
        result.append([[scalar * element for element in row] for row in matrix])
    return result
def get_matrix_inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square.")

    n = len(matrix)
    # Augmenting the matrix with an identity matrix of the same size
    augmented_matrix = [row + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]

    # Applying Gauss-Jordan elimination
    for i in range(n):
        # Normalize the current row
        factor = augmented_matrix[i][i]
        for j in range(n * 2):
            augmented_matrix[i][j] /= factor
        # Make all other rows 0 in the current column
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(n * 2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extracting the inverse matrix
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix
def get_matrix_transpose(matrix):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    
    # Create a new matrix to store the transposed matrix
    transposed_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    
    # Fill the transposed matrix with the values from the original matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

def Back3():
    tkobj3.withdraw()
    tkobj.deiconify()  
    return

# To provide functionalities
def click3(val):
    try:
        e_str = entry3.get()  # getting the string value
        ans = " "
        # ADD
        if val == "ADD":
           e = parse_matrices(e_str)# convert the string to a matrix
           ans=add_matrices(e)
        # SUB
        elif val == "SUB":
            e = parse_matrices(e_str)
            ans=subtract_matrices(e)
        # Mul
        elif val == "MUL":
            e = parse_matrices(e_str)
            ans=multiply_matrices(e)
        # Scalar MUL
        elif val == "Scalar'\n MUL":
            scal  = entry4.get()
            e = parse_matrices(e_str)
            ans=scalar_multiply_matrices(scal, e)
        # INV
        elif val == "INV":
            e = parse_matrices1(e_str)
            ans=get_matrix_inverse(e)
        # TRAN
        elif val == "TRAN":
            e = parse_matrices1(e_str)
            ans=get_matrix_transpose(e)
        # Back
        elif val == "Back":
            entry3.delete(0, "end")
            Back3()
        # Clear
        elif val == "Clear":
            entry3.delete(0, "end")
            entry4.delete(0, "end")
        else:
            entry3.insert("end", val)
            return
        entry3.delete(0, "end")
        entry4.delete(0, "end")
        entry3.insert(0, ans)
    except (ValueError, ZeroDivisionError) as e:
        entry2.delete(0, "end")
        entry2.insert(0, "Error: " + str(e))
        
# Entry field
entry3 = tkinter.Entry(tkobj3, font=("arial", 20, "bold"), bg="white", fg="Black", bd=10, width=28)
entry3.grid(row=0, column=0, columnspan=5)
entry4 = tkinter.Entry(tkobj3, font=("arial", 20, "bold"), bg="white", fg="Black", bd=10, width=5)
entry4.grid(row=1, column=0, columnspan=2)

# Buttons text list
button_list3 =["7","8","9",",","Back",
               "4","5","6","INV","TRAN",
               "1","2","3","MUL","Scalar'\n MUL",
               "0","[","]","ADD","SUB"]

# Loop to get the buttons on the Matrix Window
r = 2
c = 0
for i in button_list3:
    # Buttons
    button3 = tkinter.Button(tkobj3, width=5, height=2, bd=2, text=i, bg="light blue", fg="black",
                            font=("arial", 17, "bold"), command=lambda button=i: click3(button))
    button3.grid(row=r, column=c, pady=1)
    c += 1
    if c > 4:
       r += 1
       c = 0
button4 = tkinter.Button(tkobj3, width=5, height=1, bd=1, text="Clear", bg="light blue", fg="black",
                            font=("arial", 17, "bold"), command=lambda button="Clear": click3(button))
button4.grid(row=1, column=4, pady=1)


# Makes the main window on loop
tkobj.mainloop()