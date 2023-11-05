from class_graph import Graph
import tkinter as tk
import ttkbootstrap as ttk
from tkinter.font import nametofont

def example():
    example_graph = Graph(6)

    example_graph.addEdge(2, 3)
    example_graph.addEdge(1, 2)
    example_graph.addEdge(1, 3)
    example_graph.addEdge(2, 4)
    example_graph.addEdge(3, 5)
    example_graph.addEdge(4, 6)
    example_graph.addEdge(5, 6)
    example_graph.addEdge(2, 5)
    example_graph.addEdge(3, 4)
    example_graph.addEdge(4, 5)

    example_graph.drawGraph()

# Set up GUI
window = ttk.Window(themename='lumen')
window.title("Euler Graph")
window.geometry('400x300')

# Header
default_font = nametofont("TkDefaultFont")
header = ttk.Label(window, text="Undirected Euler Graphs", font=(default_font, 20, 'bold'))
header.pack(pady=10)

info_label = ttk.Labelframe(window, text="Enter your Knots and Edges", padding=20)
info_label.pack()

# Frames
frame_knots = ttk.Frame(info_label)
frame_knots.pack(pady=10)

frame_edges = ttk.Frame(info_label)
frame_edges.pack(pady=10)

frame_buttons = ttk.Frame(window)
frame_buttons.pack(pady=10)

# Input fields
knots = tk.IntVar()
knots_label = ttk.Label(frame_knots, text="Number of Knots:")
knots_label.pack(side='left', padx=10)
num_knots = ttk.Entry(frame_knots, textvariable=knots, bootstyle="info", width=3, justify='center')
num_knots.pack(side="left")

edges_label = ttk.Label(frame_edges, text="Set Edges between Knots:")
edges_label.pack(pady=10)


# Buttons
submit_btn = ttk.Button(frame_buttons, text="Search Eulerpath")
submit_btn.pack(side= 'left', padx=10)
example_btn = ttk.Button(frame_buttons, text="Example", command=example, bootstyle="outline")
example_btn.pack(side= 'left')

# Run GUI
window.mainloop()

### ToDO: ###
'''
- Möglichkeit, Edges anzugeben (abhängig von Number of Knots)
- erstellte Grafik innerhalb des Programms anzeigen
- "Example" Button gibt ein Beispiel aus
- "Reset" Button (alle Felder leeren)
- nach erstellen der Grafik "Search Eulerpath" ausgrauen -> Reset/New Graph
   + Example wieder Outline
- Ausgabe, wenn kein Eulerpfad gefunden wurde
- Knoten & Kanten auf der Grafik ausgeben (Legende)
'''


'''def main():
    G1 = Graph(3)

    G1.addEdge(1, 2)
    G1.addEdge(1, 3)
    G1.addEdge(2, 3)

    G2 = Graph(4)

    G2.addEdge(1, 2)
    G2.addEdge(2, 3)
    G2.addEdge(1, 3)
    G2.addEdge(3, 4)

    G3 = Graph(6)

    G3.addEdge(1, 2)
    G3.addEdge(2, 3)
    G3.addEdge(1, 3)
    G3.addEdge(2, 4)
    G3.addEdge(3, 5)
    G3.addEdge(4, 6)
    G3.addEdge(5, 6)
    G3.addEdge(2, 5)
    G3.addEdge(3, 4)
    G3.addEdge(4, 5)

    # Find Euler Circle
    print("G1:", G1.findEuler())
    print("G2:", G2.findEuler())
    print("G3:", G3.findEuler())
    print("G3:", G3.findEuler())

    # Plot Graph
    G1.drawGraph()
    G2.drawGraph()
    G3.drawGraph()


if __name__ == '__main__':
    main()
'''