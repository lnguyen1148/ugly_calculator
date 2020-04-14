
import textwrap
import math

def clear_display() -> None:
    """Clears the display"""
    set_display_write_enable()
    num_display.delete(1.0, END)
    set_display_write_enable()


def set_display_read_only():
    """Sets the display to ready only"""
    num_display["state"] = "disabled"


def set_display_write_enable():
    """Sets the display to write enable"""
    num_display["state"] = "normal"


def update_display() -> None:
    """
    Refreshes the display to show the current
    equation working equation and current
    entered number.
    """
    global current_num
    set_display_write_enable()
    clear_display()
    # sets the current display number to a maximum of 15 charaters
    current_num = textwrap.shorten(current_num, width=15, placeholder="")
    # Refreshes the equation display
    num_display.insert(END, f"{equation}{operator_queue}", "EQUATION")
    # Refreshes the current working entered number
    num_display.insert(END, f"\n{current_num}", "NUMBER")
    set_display_read_only()


def current_num_format() -> None:
    """
    Set the current number to an integer
    format if the number is a whole number. 
    """
    global current_num
    # converst the current_num from a string to a float
    number = float(current_num)
    # If the number is a whole number, parse it to an int
    if number % 1 == 0:
        number = int(number)
    # Assigns the formatted number to the current number string
    current_num = str(number)


def sqrt_click() -> None:
    """
    Takes the root of the working number and
    assigns the root value to the current working
    number.    
    """
    global equation
    global current_num
    # Parses the current number to a float variable
    number = float(current_num)
    # assigns the root of the float to current_num
    current_num = str(math.sqrt(number))
    # removes the decimal place if current_num is a whole number
    current_num_format()
    update_display()


def numbers_button_press(number: str) -> None:
    """
    Updates the number being entered into the
    calculator and refreshes the display with
    new value. If an operator has been pressed
    before the first digit is entered, the operator
    will be moved from the operator_queue and into
    the equation.
    """
    global new_number
    global equation
    global operator_queue
    global current_num
    # If the number pressed is zero and a new number is
    # being formed, set the current number to "0".
    # Leave new number variable to True, this will
    # eliminate the leading zeros if entered.
    if number == "0" and new_number:
        current_num = "0"
    # If a new number is being formed and the first
    # digit is not a zero.
    elif new_number:
        # Indicate that this we are now working with a
        # current_num that is in process
        new_number = False
        # Assign number to current_num
        current_num = number
        # If an operator is in the Q, insert it into the equation
        equation += f"{operator_queue}"
        # Remove the last used operator
        operator_queue = ""
    # Else, just append the given number to the current_num
    else:
        current_num += number
    update_display()


def decimal_button_click() -> None:
    """
    Inserts a decimal place into the current_num.
    If a decimal has already been entered, the 
    entered decimal will not be entered.
    """
    global new_number
    global equation
    global operator_queue
    global current_num
    # If the current_num is considered new,
    # Set current_num to equal "0."
    if new_number:
        new_number = False
        current_num = "0."
        equation += f"{operator_queue}"
        operator_queue = ""
    # If current_num is in process and a decimal
    # has not already been entered, append a decimal
    # to the end of the current_num.
    else:
        if "." not in current_num:
            current_num += "."
    update_display()


def operator_button_click(operator: str) -> None:
    """
    Updates the operator_queue with by the
    operator chosen by the user.
    """
    global new_number
    global equation
    global operator_queue
    # If the calculator already has an equation entered
    # or if the current_num has already been entered,
    # assign the operator to the operator_queue variable.
    if len(equation) > 0 or new_number == False:
        # If a current_num has been entered, append the
        # value of current_num to the end of the working equation.
        if new_number == False:
            equation += f" {current_num}"
        operator_queue = f" {operator}"
    # If no equation has been entered yet, and the current_num
    # does not equal zero, move the value of the current_num to
    # the equation and assign the operator to the operator_queue.
    # This will take place after equals has been pressed and the value
    # in the display will be the first value in the equation.
    elif len(equation) == 0 and current_num != "0":
        equation = current_num
        operator_queue = f" {operator}"
    new_number = True
    update_display()


def equal_button_click() -> None:
    """
    Performs the equals operation. 
    Calculates the results of the entered equation
    and displays the results in the main display.
    """
    global new_number
    global equation
    global operator_queue
    global current_num
    # If an equation has been entered and a new current_number
    # has been entered, perform the equals operation.
    if len(equation) > 0 and new_number == False:
        # Append the value of the current_num to the equation
        equation += f" {current_num}"
        # Evaluate the equation and assign the result to current_num
        current_num = str(eval(equation))
        # Removes the decimal place if the result is a whole number
        current_num_format()
        # updates the display
        update_display()
        # resets the global variables for a new equation
        equation = ""
        new_number = True
        operator_queue = ""


def clr_button_click() -> None:
    """
    Resets the calculator to its default state.
    """
    global new_number
    global current_num
    global equation
    global operator_queue
    # Assigns all global variables to their initial state
    new_number = True
    current_num = "0"
    equation = ""
    operator_queue = ""
    update_display()
