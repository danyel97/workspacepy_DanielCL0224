import tkinter as tk
from tkinter import ttk,filedialog,Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageTk
from migrations.init import exportZip
from servicios.loadData import loadData
from servicios.transformation import TransformationOrders
import os
class GraphApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Graph Example")
        self.master.geometry("800x600")
        # Cargar la imagen del logo
        self.logo_image = Image.open("C://Users//User//Desktop//courseWorkspace//workspacepy0224//modulo5//proyecto//imagenes//LOGO-DATUX.png")  # Reemplaza "logo.png" con la ruta de tu imagen
        self.logo_image = self.logo_image.resize((250, 100))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.ruta=''
        self.create_widgets()

    def create_widgets(self):
        # Agregar el logo como Label
        self.logo_label = ttk.Label(self.master, image=self.logo_image)
        self.logo_label.pack(pady=10)
        button_container = ttk.Frame(self.master)
        button_container.pack(side=tk.LEFT, padx=10, pady=0)
        #select data 
        button = tk.Button(button_container, text="Seleccionar Carpeta", command=self.select_folder)
        button.pack(pady=20)
        self.generate_button_3 = ttk.Button(button_container, text="Descomprimir Data", command=self.exportData, style="Large.TButton")
        self.generate_button_3.pack(side=tk.TOP, padx=5, pady=5)
        self.generate_button_2 = ttk.Button(button_container, text="Cargar Data", command=self.loadData, style="Large.TButton")
        self.generate_button_2.pack(side=tk.TOP, padx=5, pady=10)
        # Botón 
        self.generate_button_1 = ttk.Button(button_container, text="Reporte Relacion Edad Consumo", command=self.generate_graph, style="Large.TButton")
        self.generate_button_1.pack(side=tk.TOP, padx=5, pady=15)
        # Marco para contener el gráfico
        self.graph_frame = ttk.Frame(self.master)
        self.graph_frame.pack()
        # Label para indicar que el proceso se realizó correctamente
        self.success_label = Label(self.master, text="", fg="green")
        self.success_label.pack(pady=5)

    def generate_graph(self):
        data= TransformationOrders()
        print(data)
        # Crear un objeto de figura de Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        #columnas del grafico
        #ax.scatter(data['Age'], data['mean'], alpha=0.7)
        ax.scatter(data['Age'], data['mean'], alpha=0.7, c=data['user_id'], cmap='viridis')
        # Añadir etiquetas y título al gráfico (cambiar)
        ax.set_xlabel('Edad')
        ax.set_ylabel('Promedio de Ventas')
        ## (cambiar) titulo
        ax.set_title('Relación entre Edad y Promedio de Ventas por Usuario')

        # Crear el objeto de lienzo de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()
        self.success_label.config(text='grafico complete', fg="green")

    def select_folder(self):
        initial_dir = os.getcwd() 
        folder_path = filedialog.askdirectory(initialdir=initial_dir, title="Seleccionar Carpeta con Archivos", mustexist=True)
        if folder_path:
            self.ruta=folder_path
            print("Carpeta seleccionada:", folder_path)

    def exportData(self):
        msg=exportZip()
        self.success_label.config(text=msg, fg="green")

    def loadData(self):
        ruta=self.ruta.split('/')[-1]
        msg=loadData(ruta)
        self.success_label.config(text=msg, fg="green")
        pass

def initApp():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()



