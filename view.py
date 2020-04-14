from tkinter import *
import textwrap

# Main Calculator Window
root = Tk()
# Window Header
root.title("Standard Calculator")
# Window Icon
root.iconbitmap("PyCrust.ico")
# window size set and fixed to un-sizeable
root.geometry("323x443")
root.resizable(0, 0)

# Content Frame to hold all widgets
content = Frame(root, bg="#f03b20", padx=10, pady=10)
content.grid(column=0, row=0, sticky=(N, S, E, W))

# Main Calculator Display
num_display = Text(
    content,
    width=10,
    height=2,
    font=("Helvetica", 30),
    state="disabled",
    bg="#feb24c",
    padx=10,
)
# Two configured formatting styles for the main display
# EQUATION: Right justified with font size 11
# NUMBER: Right justified with font size 25
num_display.tag_configure("EQUATION", justify="right", font=("Helvetica", 11))
num_display.tag_configure("NUMBER", justify="right", font=("Helvetica", 25))

# All initialized GUI buttons
sqrt_button = Button(
    content,
    text="sqrt",
    font=("Helvetica", 20),
    padx=4,
    bg="#ffeda0",
    command=sqrt_click,
)
clr_button = Button(
    content,
    text="C",
    font=("Helvetica", 20),
    padx=17,
    bg="#ffeda0",
    command=clr_button_click,
)
div_button = Button(
    content,
    text="/",
    font=("Helvetica", 20),
    padx=22,
    bg="#ffeda0",
    command=lambda: operator_button_click("/"),
)
multi_button = Button(
    content,
    text="X",
    font=("Helvetica", 20),
    padx=11,
    bg="#ffeda0",
    command=lambda: operator_button_click("*"),
)
minus_button = Button(
    content,
    text="-",
    font=("Helvetica", 20),
    padx=14,
    bg="#ffeda0",
    command=lambda: operator_button_click("-"),
)
add_button = Button(
    content,
    text="+",
    font=("Helvetica", 20),
    padx=11,
    bg="#ffeda0",
    command=lambda: operator_button_click("+"),
)
equal_button = Button(
    content,
    text="=",
    font=("Helvetica", 20),
    padx=11,
    pady=31,
    bg="#ffeda0",
    command=equal_button_click,
)
one_button = Button(
    content,
    text="1",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("1"),
)
two_button = Button(
    content,
    text="2",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("2"),
)
three_button = Button(
    content,
    text="3",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("3"),
)
four_button = Button(
    content,
    text="4",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("4"),
)
five_button = Button(
    content,
    text="5",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("5"),
)
six_button = Button(
    content,
    text="6",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("6"),
)
seven_button = Button(
    content,
    text="7",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("7"),
)
eight_button = Button(
    content,
    text="8",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("8"),
)
nine_button = Button(
    content,
    text="9",
    font=("Helvetica", 20),
    padx=19,
    bg="#ffeda0",
    command=lambda: numbers_button_press("9"),
)
zero_button = Button(
    content,
    text="0",
    font=("Helvetica", 20),
    padx=58,
    bg="#ffeda0",
    command=lambda: numbers_button_press("0"),
)
decimal_button = Button(
    content,
    text=".",
    font=("Helvetica", 20),
    padx=22,
    bg="#ffeda0",
    command=decimal_button_click,
)

# All widget placement into the GUI
num_display.grid(column=0, row=0, columnspan=4, sticky=(N, E, W), padx=2, pady=15)
one_button.grid(column=0, row=4, padx=2, pady=2)
two_button.grid(column=1, row=4, padx=2, pady=2)
three_button.grid(column=2, row=4, padx=2, pady=2)
four_button.grid(column=0, row=3, padx=2, pady=2)
five_button.grid(column=1, row=3, padx=2, pady=2)
six_button.grid(column=2, row=3, padx=2, pady=2)
seven_button.grid(column=0, row=2, padx=2, pady=2)
eight_button.grid(column=1, row=2, padx=2, pady=2)
nine_button.grid(column=2, row=2, padx=2, pady=2)
zero_button.grid(column=0, row=5, columnspan=2, padx=2, pady=2)
decimal_button.grid(column=2, row=5, padx=2, pady=2)
sqrt_button.grid(column=0, row=1, padx=2, pady=2)
clr_button.grid(column=1, row=1, padx=2, pady=2)
div_button.grid(column=2, row=1, padx=2, pady=2)
multi_button.grid(column=3, row=1, padx=2, pady=2)
minus_button.grid(column=3, row=2, padx=2, pady=2)
add_button.grid(column=3, row=3, padx=2, pady=2)
equal_button.grid(column=3, row=4, rowspan=2, padx=2, pady=2)


def main():
    update_display()
    root.mainloop()


if __name__ == "__main__":
    main()
