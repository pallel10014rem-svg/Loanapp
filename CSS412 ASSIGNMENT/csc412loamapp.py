import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class LoanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Loan Simulation App")
        self.root.geometry("500x600")

        title = tk.Label(root, text="Smart Loan Simulation App", font=("Arial", 18, "bold"))
        title.pack(pady=10)
         # Loan Amount
        tk.Label(root, text="Loan Amount (₦)").pack()
        self.loan_entry = tk.Entry(root)
        self.loan_entry.pack()

        # Interest Rate
        tk.Label(root, text="Annual Interest Rate (%)").pack()
        self.rate_entry = tk.Entry(root)
        self.rate_entry.pack()

        # Duration
        tk.Label(root, text="Loan Duration (Years)").pack()
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        # Monthly Payment
        tk.Label(root, text="Monthly Payment (₦)").pack()
        self.payment_entry = tk.Entry(root)
        self.payment_entry.pack()

         # Extra Payment
        tk.Label(root, text="Extra Monthly Payment (₦)").pack()
        self.extra_entry = tk.Entry(root)
        self.extra_entry.pack()

        # Default Month
        tk.Label(root, text="Default Month (0 if none)").pack()
        self.default_entry = tk.Entry(root)
        self.default_entry.pack()

        calculate_btn = tk.Button(root, text="Simulate Loan", command=self.simulate_loan)
        calculate_btn.pack(pady=15)

        self.result_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
        self.result_label.pack(pady=10)

    def simulate_loan(self):
        try:
            loan = float(self.loan_entry.get())
            annual_rate = float(self.rate_entry.get())
            years = int(self.time_entry.get())
            monthly_payment = float(self.payment_entry.get())
            extra_payment = float(self.extra_entry.get())
            default_month = int(self.default_entry.get())

            monthly_rate = annual_rate / 100 / 12
            balance = loan

            balances = []
            months = []

            total_paid = 0
            total_interest = 0
            month = 0

            while balance > 0:
                month += 1

                interest = balance * monthly_rate
                total_interest += interest

                balance += interest

                payment = monthly_payment + extra_payment

                # Loan default simulation
                if month == default_month:
                    penalty = 0.1 * balance
                    balance += penalty
                    messagebox.showwarning(
                        "Loan Default",
                         f"Default occurred in month {month}. 10% penalty added!"
                    )

                if payment > balance:
                    payment = balance

                balance -= payment
                total_paid += payment

                balances.append(balance)
                months.append(month)

                # Prevent infinite loop
                if month > years * 12 * 3:
                    break
            
            
            result = (
                f"Loan Fully Repaid!\n\n"
                f"Months Taken: {month}\n"
                f"Total Paid: ₦{total_paid:,.2f}\n"
                f"Total Interest: ₦{total_interest:,.2f}\n"
            )

            self.result_label.config(text=result)
            
            # Visualization
            plt.figure(figsize=(8, 5))
            plt.plot(months, balances, marker='o')
            plt.title("Loan Balance Over Time")
            plt.xlabel("Months")
            plt.ylabel("Remaining Balance (₦)")
            plt.grid(True)
            plt.show()

        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
app = LoanApp(root)
root.mainloop()
