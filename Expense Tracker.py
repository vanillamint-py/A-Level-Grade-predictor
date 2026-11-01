import tkinter as tk 
from tkinter import messagebox, ttk
import csv
import os 
from datetime import datetime 

CSVfile = "expenses.csv"

if not os.path.exists(CSVfile):
    with open(CSVfile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

def addexpense():
    amount = entryamount.get().strip()
    category = entrycategory.get().strip()
    description = entrydescription.get().strip()
    
    if not amount or not category:
        messagebox.showwarning("Input error", "Amount and category are required.")
        return 
    
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input error", "Amount must be a valid number.")
        return 
    
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(CSVfile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
        
    entryamount.delete(0, tk.END)
    entrycategory.delete(0, tk.END)
    entrydescription.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Expense added.")
    viewexpenses()

def viewexpenses():
    display.delete("1.0", tk.END)
    
    if not os.path.exists(CSVfile):
        display.insert(tk.END, "No response.")
        return 
    
    display.insert(tk.END, f"{'Date':<12} / {'Amount':<8} / {'Category':<12} / Description\n")
    display.insert(tk.END, "-"*55 + "\n")
    
    with open(CSVfile, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                display.insert(tk.END, f"{row[0]:<12} / ${row[1]:<7} / {row[2]:<12} / {row[3]}\n")
                

def monthlysummary():
    display.delete("1.0", tk.END)
    
    categorytotal = {}
    totalspent = 0.0
    
    if not os.path.exists(CSVfile):
        display.insert(tk.END, "No expenses recorded yet.")
        return

    with open(CSVfile, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                amount = float(row[1])
                category = row[2]
                totalspent = totalspent + amount
                
                if category in categorytotal:
                    categorytotal[category] = categorytotal[category] + amount 
                else:
                    categorytotal[category] = amount 
    
    display.insert(tk.END, "=== MONTHLY SUMMARY STATUS ===\n\n")
    display.insert(tk.END, f"Total overall expense : ${totalspent:.2f}\n")
    display.insert(tk.END, "-"*35 + "\n")
    display.insert(tk.END, "Expenses by category :\n")
    
    for category, total in categorytotal.items():
        display.insert(tk.END, f" * {category:<15} : ${total:.2f}\n")
    
    
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("450x500")

tk.Label(root, text="Amount ($) :").pack(pady=5)
entryamount = tk.Entry(root)
entryamount.pack()
tk.Label(root, text="Category(e.g. Food, Transport) :").pack(pady=5)
entrycategory = tk.Entry(root)
entrycategory.pack()
tk.Label(root, text="Description :").pack(pady=5)
entrydescription = tk.Entry(root)
entrydescription.pack()

addbutton = tk.Button(root, text="Add Expense", command=addexpense)
addbutton.pack(pady=15)
viewbutton = tk.Button(root, text="View all expenses", command=viewexpenses)
viewbutton.pack(pady=5)
summarybutton = tk.Button(root, text="View monthly summary", command=monthlysummary)
summarybutton.pack(pady=5)

display = tk.Text(root, width=50, height=12)
display.pack(pady=15)

viewexpenses()
root.mainloop()
