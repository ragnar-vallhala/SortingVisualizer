from sorting import *
from random import randint
import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import threading
from tkinter import ttk


size=10

arr = [randint(1,100) for i in range(size)]


def animate(i):
    global arr
    x = np.arange(len(arr))
    
    
    # Clear previous plot
    ax.clear()
    
    # Plot new data
    ax.bar(x,arr)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Live Plot')


def getArr(inArr):
    global arr
    arr = inArr
    time.sleep(0.1)
    
threds = []
def start_sorting():
    global selected_algorithm
    algo = selected_algorithm.get()
    print(selected_algorithm)
    sort = Sorting(getArr)
    if algo=='Quick Sort':
        t = threading.Thread(target=sort.quick_sort, args=(arr,))
        t.start()
        threds.append(t)
    elif  algo=='Bubble Sort':
        t=threading.Thread(target=sort.bubble_sort,args=(arr,))
        t.start()
        threds.append(t)
    elif  algo == 'Selection Sort':
        t=threading.Thread(target=sort.selection_sort,args=(arr,))
        t.start()
        threds.append(t)
    elif   algo == "Insertion Sort":
        t=threading.Thread(target=sort.insertion_sort,args=(arr,))
        t.start()
        threds.append(t)
    elif  algo=="Merge Sort":
        t=threading.Thread(target=sort.merge_sort,args=(arr,))
        t.start()
        threds.append(t)
    elif  algo=="Radix Sort":
        t=threading.Thread(target=sort.radix_sort,args=(arr,))
        t.start()
        threds.append(t)
    

def reinitialize():
    global arr
    arr = [randint(1,100) for i in range(size)]
    

root = tk.Tk()
root.title("Live Plot")

start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
start_button.pack()

init_button = tk.Button(root, text="Reinitialize", command=reinitialize)
init_button.pack()

options = ['Quick Sort', 'Merge Sort', 'Selection Sort', 'Bubble Sort', 'Radix Sort']  # Add more sorting algorithms here
selected_algorithm = tk.StringVar(value=options[0])
dropdown = ttk.Combobox(root, textvariable=selected_algorithm, values=options)
dropdown.pack()


fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()
ani = animation.FuncAnimation(fig, animate, interval=10)

# Run Tkinter main loop
root.mainloop()
res = (t.join() for t in threds)