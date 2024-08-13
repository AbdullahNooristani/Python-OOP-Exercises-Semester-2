import tkinter as tk
from tkinter import filedialog, font, messagebox, PhotoImage


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Abdullah" and password == "1234":
        messagebox.showinfo("Success", "Login successful!")
        show_main_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# نمایش صفحه اصلی
def show_main_screen():
    login_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
    root.geometry("800x600")

# توابع کار خانگی
def homework_1():
    text = """Homework 1:
Python provides a set of built-in functions for common tasks. Here are some of them:

1. len(): Returns the number of items in an object.
   Example: len("Hello") => 5

2. type(): Returns the type of an object.
   Example: type(123) => <class 'int'>

3. print(): Prints objects to the console.
   Example: print("Hello, World!") => Output: Hello, World!

4. range(): Generates a sequence of numbers.
   Example: list(range(5)) => [0, 1, 2, 3, 4]

5. abs(): Returns the absolute value of a number.
   Example: abs(-10) => 10

6. sum(): Returns the sum of a sequence of numbers.
   Example: sum([1, 2, 3, 4]) => 10

7. max() and min(): Returns the maximum and minimum value in a sequence.
   Example: max([1, 2, 3]) => 3
            min([1, 2, 3]) => 1

8. sorted(): Returns a sorted list of the specified iterable object.
   Example: sorted([3, 1, 2]) => [1, 2, 3]

9. dir(): Lists the attributes and methods of an object.
   Example: dir([]) => Lists methods available for lists

10. help(): Provides help about a module or function.
    Example: help(sorted) => Provides information about the sorted function

    """
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

def homework_2():
    text = """Homework 2:
Python has several built-in libraries that are essential for various tasks. Some of them include:

1. os: Provides a way to interact with the operating system.
   - os.getcwd(): Gets the current working directory.
   - os.listdir(path): Lists files and directories in a given path.
   - os.path.join(path, *paths): Joins one or more path components.

2. sys: Provides access to system-specific parameters and functions.
   - sys.argv: A list of command-line arguments passed to a script.
   - sys.exit([arg]): Exits the program with optional status code.

3. math: Provides mathematical functions.
   - math.sqrt(x): Returns the square root of x.
   - math.factorial(x): Returns the factorial of x.
   - math.pi: Provides the constant π.

4. datetime: Provides classes for manipulating dates and times.
   - datetime.date(year, month, day): Represents a date.
   - datetime.datetime(year, month, day, hour, minute, second): Represents a date and time.
   - datetime.timedelta(days, seconds): Represents a duration.

5. random: Provides functions for generating random numbers.
   - random.randint(a, b): Returns a random integer between a and b.
   - random.choice(seq): Returns a random element from a non-empty sequence.

6. json: Provides functions for parsing and generating JSON data.
   - json.loads(json_string): Parses a JSON string into a Python dictionary.
   - json.dumps(object): Converts a Python object into a JSON string.
    """
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

def homework_3():
    text = """Homework_2:
Fibonacci Sequence in Python:

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

print(fibonacci(10)) => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

def homework_4():
    text = """Homework 4:
Factorial Calculation in Python:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) => 120
    """
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

def homework_5():
    text = """About Us:
This software was created by Abdullah Nooristani, the son of Ziauddin Nooristani, born in 2005.
Abdullah is currently studying Software Engineering Department in the Computer Science Faculty at Kabul University.

Features of this software include:
Include all of the homework in semester 2 
This application is designed to be user-friendly, with a focus on simplicity and efficiency.

    """
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)

# تابع خروج از برنامه
def exit_app():
    result = messagebox.askquestion("Exit", "Are you sure you want to exit?", icon='warning')
    if result == 'yes':
        root.quit()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("800x600")

# تنظیم فونت‌ها
default_font = font.Font(family="Arial", size=12)

# ایجاد صفحه ورود
login_frame = tk.Frame(root, bg="#2C3E50")
login_frame.pack(fill='both', expand=True)

# آیکون ورود
login_icon = PhotoImage(file="login_icon.png")
login_icon_label = tk.Label(login_frame, image=login_icon, bg="#2C3E50")
login_icon_label.pack(pady=20)

# عنوان صفحه ورود
login_title = tk.Label(login_frame, text="Login to Your Account", font=('Helvetica', 20, 'bold'), bg="#2C3E50", fg="white")
login_title.pack(pady=10)

# فریم ورودی‌ها
input_frame = tk.Frame(login_frame, bg="#34495E", padx=20, pady=20)
input_frame.pack(pady=20)


username_label = tk.Label(input_frame, text="Username", font=('Arial', 14), bg="#34495E", fg="white")
username_label.grid(row=0, column=0, pady=10, sticky="w")
username_entry = tk.Entry(input_frame, font=('Arial', 14), width=20)
username_entry.grid(row=0, column=1, pady=10)


def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(  show = "*")
        toggle_button.config(text = "SHOW")
    else:
        password_entry.config(show ="")
        toggle_button.config(text = "HIDE")
toggle_button = tk.Button(input_frame,  width = 5,bg = "white",text = "SHOW",  command = toggle_password)
toggle_button.grid(column = 3, row = 1, padx = 8)

password_label = tk.Label(input_frame, text="Password", font=('Arial', 14), bg="#34495E", fg="white")
password_label.grid(row=1, column=0, pady=10, sticky="w")
password_entry = tk.Entry(input_frame, show="*", font=('Arial', 14), width=20)
password_entry.grid(row=1, column=1, pady=10)

# دکمه ورود
login_button = tk.Button(login_frame, text="Login", command=login, font=('Arial', 14, 'bold'), bg="#1ABC9C", fg="white", width=20)
login_button.pack(pady=20)

# دکمه خروج
exit_button = tk.Button(login_frame, text="Exit", command=exit_app, font=('Arial', 14, 'bold'), bg="#E74C3C", fg="white", width=20)
exit_button.pack(pady=10)


main_frame = tk.Frame(root, bg="lightblue")


text_area = tk.Text(main_frame, wrap='word', font=default_font)
text_area.pack(fill='both', expand=True, padx=10, pady=10)


btn_frame = tk.Frame(main_frame, bg="lightblue")
btn_frame.pack(pady=10)

btn_homework_1 = tk.Button(btn_frame, text="homework 1", command=homework_1, font=('Arial', 12, 'bold'), bg="#1ABC9C", fg="white", width=20)
btn_homework_1.grid(row=0, column=0, padx=5, pady=5)

btn_homework_2 = tk.Button(btn_frame, text="homework 2", command=homework_4, font=('Arial', 12, 'bold'), bg="#3498DB", fg="white", width=20)
btn_homework_2.grid(row=0, column=1, padx=5, pady=5)

btn_homework_3 = tk.Button(btn_frame, text="homework3", command=homework_3, font=('Arial', 12, 'bold'), bg="#9B59B6", fg="white", width=20)
btn_homework_3.grid(row=0, column=2, padx=5, pady=5)

btn_homework_4 = tk.Button(btn_frame, text="About", command=homework_5, font=('Arial', 12, 'bold'), bg="#E74C3C", fg="white", width=20)
btn_homework_4.grid(row=0, column=3, padx=5, pady=5)

btn_homework_5 = tk.Button(btn_frame, text="exit", command=quit, font=('Arial', 12, 'bold'), bg="#F39C12", fg="white", width=20)
btn_homework_5.grid(row=0, column=4, padx=5, pady=5)


root.mainloop()