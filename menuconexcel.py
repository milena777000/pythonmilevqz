from tkinter import Tk, Menu, messagebox, simpledialog,Text
import pandas as pd 




class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create__menu()
        self.nombreexcel="/home/b5/Documentos/milena.colegio/5bmilevqz/visualcodepyth/excel.youuuuuuuuuuuuu.xls"
        self.gente=pd.read_excel(self.nombreexcel)
        
        #crear un area de texto para mostrar los resultados
        self.text_area=Text(master,wrap='word', height=20, width=60)
        self.text_area.pack(side='left', fill='both',expand=True)
        
    def create__menu(self):
        # Crear la barra de menú
        barra_menus = Menu(self.master)

        # Crear el menú "Excel"
        menu_excel = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Excel", menu=menu_excel)

        # Agregar opciones al menú "Excel"
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)

        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=barra_menus)

    def show_all(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")

    def show_name(self):
        name = simpledialog.askstring("Nombre", "Introduce tu nombre:")
        if name:
            messagebox.showinfo("Nombre ingresado", f"Tu nombre es: {name}")

    def show_over_18(self):
        age = simpledialog.askinteger("Edad", "Introduce tu edad:")
        if age is not None:
            if age >= 18:
                messagebox.showinfo("Acceso permitido", "Eres mayor de 18 años.")
            else:
                messagebox.showwarning("Acceso denegado", "Eres menor de 18 años.")

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        # Crear el menú
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
        