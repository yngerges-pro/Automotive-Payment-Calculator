import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pathlib import Path
import tkinter as tk


current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
EXCEL_FILE = current_dir / 'Car.xlsx'
df = pd.read_excel(EXCEL_FILE)

def Ana():
    totalListed = []
    downListed = []
    for i in range(32):
        downListed.append(df['Down Payment'][i])
        totalListed.append(df['Total'][i])
    

    n = 31
    scoreListed = []
    totalforScores = []
    for _ in range(4):
        n += 1
        scoreListed.append(df['Credit Score'][n])
        totalforScores.append(df['Total'][n])

    a = 35
    totalforTerm = []
    TermListed = []
    for _ in range(4):
        a += 1
        TermListed.append(df['Loan Term'][a])
        totalforTerm.append(df['Total'][a])

    fig, axs = plt.subplots(2, 2, figsize=(8, 4))

    
    axs[0][0].scatter(downListed,totalListed, c='red')
    axs[0][0].set_title("Total Payment vs Down Payment")

    

    axs[0][1].scatter(scoreListed,totalforScores, c='blue')
    axs[0][1].set_title("Total Payment vs Credit Score")

    
    
    axs[1][0].scatter(TermListed,totalforTerm, c='green')
    axs[1][0].set_title("Total Payment vs Loan Term")

    axs[1][1].remove()

    fig.suptitle("Graph")

    fig.tight_layout()
    plt.show()

#----------------------------------slopes-------------------------------------------------
    slope, _ = np.polyfit(downListed, totalListed, 1)
    # # # Print the slope
    scoreListed = [300,600,660,720]
    slopeforScore, _ = np.polyfit(scoreListed, totalforScores, 1)
    slopeforterm, _ = np.polyfit(TermListed,totalforTerm,1)
    
#----------------------------------slopes-------------------------------------------------
    return totalListed,totalforScores,totalforTerm, slope, slopeforScore, slopeforterm


def DataAnalysisfun():
    totalListed,totalforScores,totalforTerm, slope, slopeforScore, slopeforterm = Ana()
    max_val_downPayment = np.max(totalListed)
    min_val_downPayment = np.min(totalListed)

    max_val_score = np.max(totalforScores)
    min_val_score = np.min(totalforScores)

    max_val_Term = np.max(totalforTerm)
    min_val_Term = np.min(totalforTerm)
    return min_val_downPayment, max_val_downPayment, min_val_score, max_val_score, min_val_Term,max_val_Term, slope, slopeforScore, slopeforterm 



def function():
    min_val_downPayment, max_val_downPayment, min_val_score, max_val_score, min_val_Term, max_val_Term, slope, slopeforScore, slopeforterm = DataAnalysisfun()

    win1 = tk.Tk()
    win1.title('Data Analysis')
    win1.geometry("560x320")
    win1.config(bg="#FFEEF2")

    min_down_label = tk.Label(win1, text='With an starting price of $80,000, the total payment for $80,000 down payment is $' + f'{min_val_downPayment:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    min_down_label.pack(anchor="w")

    max_down_label = tk.Label(win1, text='With an starting price of $80,000, The total payment for $2,500 down payment: $' + f'{max_val_downPayment:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    max_down_label.pack(anchor="w")

    min_score_label = tk.Label(win1, text='With an starting price of $80,000, The total payment for 720-850 credit score: $' + f'{min_val_score:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    min_score_label.pack(anchor="w")

    max_score_label = tk.Label(win1, text=' With an starting price of $80,000, The total payment for 300-599 credit score: $' + f'{max_val_score:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    max_score_label.pack(anchor="w")

    min_term_label = tk.Label(win1, text='With an starting price of $80,000, The total payment for 72 Months loan term: $' + f'{min_val_Term:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    min_term_label.pack(anchor="w")

    max_term_label = tk.Label(win1, text='With an starting price of $80,000, The maximum total payment for 36 Months loan term: $' + f'{max_val_Term:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    max_term_label.pack(anchor="w")

    slope_down_label = tk.Label(win1, text='The slope of total payment vs down payment: ' + f'{slope:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    slope_down_label.pack(anchor="w")

    slope_score_label = tk.Label(win1, text='The slope of total payment vs credit score: '  + f'{slopeforScore:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    slope_score_label.pack(anchor="w")


    slope_term_label = tk.Label(win1, text='The slope of total payment vs loan term: ' + f'{slopeforterm:.2f}', bg= "#FFEEF2" ,fg = "#98847F", font = ('Lato', 12))
    slope_term_label.pack(anchor="w")

    exit_button = tk.Button(win1, text='Exit', command=win1.destroy, background="#FFC1D8")
    exit_button.pack()

    win1.mainloop()

    return win1


