from pathlib import Path
import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import mysql.connector
from AnalyzingPython import Ana


current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Car.xlsx'
df = pd.read_excel(EXCEL_FILE)

down = 0
trade = 0
name = "Down Payments"
rate = 0.1
score ="300-599"
term = 36
price = 80000
tax = 0.08
for _ in range(32):
    down += 2500
    # monthly rate
    try:
        pv = (price + (price * tax)) - down - trade 
        r = rate/12
        payment = (r * pv) / (1 - (1 + r) ** (-term))
        total = (payment * term) + down
        if down == price:
            term = 0
            payment = 0
            total = (price + (price * tax))
    except ZeroDivisionError:
       if down == price:
            term = 0
            payment = 0
            total = (price + (price * tax))


#-------------The rest of the data is just putting it through program----------------------------------------------

    # Payment_window['Monthly'].update(value=f'{payment:.2f}')
    # Payment_window['Total'].update(value=f'{total:.2f}')
    data = [{'Name': name, 'Price': price, 'Down Payment': down, 'Trade-In Value': trade, 'Credit Score': score, 'Loan Term': term, 'Monthly': payment, 'Total': total}]
    new_record = pd.DataFrame(data, index=[0])
    df = pd.concat([df, new_record], ignore_index=False)
    df.to_excel(EXCEL_FILE, sheet_name='name', index=False)