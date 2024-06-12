import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def generer_droite():
    try:
        px = float(entry_px.get())
        py = float(entry_py.get())
        revenu = float(entry_revenu.get())
        
        if px <= 0 or py <= 0 or revenu <= 0:
            raise ValueError("Values must be positive")
        
        tracer_droite(px, py, revenu)
    except ValueError as e:
        label_message.config(text=f"Error: {e}", bg="red")

def tracer_droite(px, py, revenu):
    # Calcul des points
    x_max = revenu / px
    y_max = revenu / py
    
    # Tracer la droite de budget
    plt.figure()
    plt.plot([0, x_max], [y_max, 0], label="Buget Line")
    plt.xlim(0, x_max * 1.1)
    plt.ylim(0, y_max * 1.1)
    plt.xlabel('Quantity of things X')
    plt.ylabel('Quantity of things Y')
    plt.title('Budget line')
    plt.legend()
    plt.grid(True)
    plt.show()

# Interface Tkinter
root = tk.Tk()
root.title("Budget line plotter")
root.iconbitmap("logo.ico")


# Labels et Entries
label_px = ttk.Label(root, text="Price of X (Px):")
label_px.grid(row=0, column=0, padx=10, pady=5)
entry_px = ttk.Entry(root)
entry_px.grid(row=0, column=1, padx=10, pady=5)

label_py = ttk.Label(root, text="Price of Y (Py):")
label_py.grid(row=1, column=0, padx=10, pady=5)
entry_py = ttk.Entry(root)
entry_py.grid(row=1, column=1, padx=10, pady=5)

label_revenu = ttk.Label(root, text="Income (m):")
label_revenu.grid(row=2, column=0, padx=10, pady=5)
entry_revenu = ttk.Entry(root)
entry_revenu.grid(row=2, column=1, padx=10, pady=5)

# Bouton
btn_generer = ttk.Button(root, text="Generate the Line", command=generer_droite)
btn_generer.grid(row=3, column=0, columnspan=2, pady=10)

# Message
label_message = ttk.Label(root, text="")
label_message.grid(row=4, column=0, columnspan=2, pady=5)

# Boucle principale
root.mainloop()
