import tkinter as tk
from tkinter import messagebox

# Function to calculate the monthly payment and total amount paid
def calculate():
    try:
        # Get the values from the entry fields and convert to float
        loan_amount = float(loan_amount_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100
        loan_term_years = float(loan_term_entry.get())

        # Convert the loan term to months
        loan_term_months = loan_term_years * 12

        # Calculate the monthly interest rate
        monthly_interest_rate = interest_rate / 12

        # Calculate the monthly payment
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-loan_term_months))

        # Calculate the total amount paid
        total_amount_paid = monthly_payment * loan_term_months

        # Update the labels with the results
        monthly_payment_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        total_amount_paid_label.config(text=f"Total Amount Paid: ${total_amount_paid:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields.")


# Function to validate input as integer
def validate_input(new_value):
    if not new_value:
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        messagebox.showerror("Error", "Please enter integer values only.")
        return False


# Create the GUI
window = tk.Tk()
window.title("Loan Calculator")
#set title
window.config(background="pink")
font = ("Courier New", 15, "underline")
tk.Label(window,text="Loan Calculator",bg="red",borderwidth=6,height=1,font=font).grid(row = 1,column = 8)

font1 = ("Helvetica", 10, "bold")
font2 = ("Helvetica", 15, "bold")
# Create the loan amount label and entry field
loan_amount_label = tk.Label(window, text="Loan Amount:",bg="pink",borderwidth=6,height=5,font=font1)
loan_amount_label.grid(row=2, column=7, padx=5, pady=5)
loan_amount_entry = tk.Entry(window,justify ="center",width=20,font=font1)
loan_amount_entry.grid(row=2, column=9, padx=5, pady=5)

# Create the interest rate label and entry field
interest_rate_label = tk.Label(window, text="Interest Rate (%):",bg="pink",borderwidth=6,height=5,font=font1)
interest_rate_label.grid(row=3, column=7, padx=5, pady=5)
interest_rate_entry = tk.Entry(window,justify ="center",width=20,font=font1,)
interest_rate_entry.grid(row=3, column=9, padx=5, pady=5)
# Create the loan term label and entry field
loan_term_label = tk.Label(window, text="Loan Term (years):",bg="pink",borderwidth=6,height=5,font=font1)
loan_term_label.grid(row=4, column=7, padx=5, pady=5)
loan_term_entry = tk.Entry(window,justify ="center",width=20,font=font1,)
loan_term_entry.grid(row=4, column=9, padx=5, pady=5)

# Add validation to ensure that the user only enters integers
vcmd = (window.register(validate_input), '%P')
loan_amount_entry.config(validatecommand=vcmd)
interest_rate_entry.config(validatecommand=vcmd)
loan_term_entry.config(validatecommand=vcmd)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate Payment", command=calculate,bg="blue",font=font2)
calculate_button.grid(row=7, column=8, padx=5, pady=5)

# Create the labels to display the results
monthly_payment_label = tk.Label(window, text="Monthly Payment:",bg="pink",borderwidth=6,height=5,font=font1)
monthly_payment_label.grid(row=5, column=8, padx=5, pady=5)
total_amount_paid_label = tk.Label(window, text="Total Amount Paid:",bg="pink",borderwidth=6,height=5,font=font1)
total_amount_paid_label.grid(row=6, column=8, padx=5, pady=5)

# Run the GUI
window.mainloop()
