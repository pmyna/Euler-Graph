from class_graph import Graph
import tkinter as tk
import ttkbootstrap as ttk
from tkinter.font import nametofont
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def get_euler(knots, edges_str):
    edges_array = edges_str.replace(" ", "").split(";")
        
    user_graph = Graph(knots)
    for i in range(len(edges_array)):
        user_graph.addEdge(int(edges_array[i][0]), int(edges_array[i][2]))
        
    output.set(str(user_graph.findEuler()))
     
# Set up GUI
window = ttk.Window(themename='lumen')
window.title("Euler Graph")
window.geometry('400x400')

# Header
default_font = nametofont("TkDefaultFont")
ttk.Label(window, text="Undirected Euler Graphs", font=(default_font, 20, 'bold')).pack(pady=10)

info_label = ttk.Labelframe(window, text="Enter your Knots and Edges", padding=20)
info_label.pack()

# Frames
frame_knots = ttk.Frame(info_label)
frame_knots.pack(pady=10)

frame_edges = ttk.Frame(info_label)
frame_edges.pack(pady=10)

frame_buttons = ttk.Frame(window)
frame_buttons.pack(pady=10)

frame_output = ttk.Frame(window)
frame_output.pack(pady=10)

# Input fields
ttk.Label(frame_knots, text="Number of Knots:").pack(side='left', padx=10)
options = [*range(2, 100, 1)]
num_knots = ttk.Combobox(frame_knots, bootstyle="info", state='readonly', values=options, width=3, justify='center')
num_knots.pack(side="left")

ttk.Label(frame_edges, text="Set Edges between Knots:").pack(pady=10)
edges_format = ttk.Label(frame_edges, text="Example for 3 Knots: 1-2; 1-3; 2-3", font=(default_font, 10, 'italic'))
edges_format.pack()

edges = tk.StringVar()
ttk.Entry(frame_edges, bootstyle="info", textvariable=edges).pack(pady=10)

# Buttons
submit_btn = ttk.Button(frame_buttons, text="Search Eulerpath", command=lambda: get_euler(int(num_knots.get()), edges.get())).pack(side= 'left', padx=10)
example_btn = ttk.Button(frame_buttons, text="Example", command=lambda: get_euler(3, "1-2; 1-3; 2-3"), bootstyle="outline").pack(side= 'left')

# Output field (temp)
result_label = ttk.Label(frame_output, text="Result:")
result_label.pack(side='left')

output = tk.StringVar()
output_label = ttk.Label(frame_output, textvariable=output)
output_label.pack(padx=5)

# Run GUI
window.mainloop()

### ToDos ###
'''
- plotly graph output doesn't open anymore
- clear entry after submit
'''