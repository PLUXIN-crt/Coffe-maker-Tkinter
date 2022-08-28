from sre_parse import State
from tkinter import *
from tkinter import PhotoImage
import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Labelframe
# Funcion asignadas a los botones


def seleccion_cafe():
    global cafe, precio
    if opccion.get() == 1:
        precio = 600
        cafe = "Moca"
    elif opccion.get() == 2:
        precio = 800
        cafe = "Capuchino"
    elif opccion.get() == 3:
        precio = 500
        cafe = "Expresso"
    elif opccion.get() == 4:
        precio = 1000
        cafe = "Latte"
    elif opccion.get() == 5:
        precio = 1200
        cafe = "Frapuchino"


# Variable
pagado = 0
# Ventana secundaria


def segunda():
    global opccion, boton1_inicial, ventana_inicial, ventana1, valor, combo2, ventana3
    ventana_inicial.withdraw()  # Cerramos la ventana "principal"
    ventana1 = Toplevel()  # Se abre una ventana superior
    ventana1.geometry("400x400")
    ventana1.title("Cafetera")
    ventana1.config(bg="black")
    opccion = IntVar()
    etiqueta = Label(ventana1, text="Seleccione un Cafe",
                     justify="center", font=15, fg="white", bg="black")
    etiqueta.pack()
    # Botones
    boton1 = Radiobutton(ventana1, value=1, variable=opccion,
                         command=seleccion_cafe, bg="black")  # Moca
    boton2 = Radiobutton(ventana1, value=2, variable=opccion,
                         command=seleccion_cafe, bg="black")  # capuchino
    boton3 = Radiobutton(ventana1, value=3, variable=opccion,
                         command=seleccion_cafe, bg="black")  # Expresso
    boton4 = Radiobutton(ventana1, value=4, variable=opccion,
                         command=seleccion_cafe, bg="black")  # Latte
    boton5 = Radiobutton(ventana1, value=5, variable=opccion,
                         command=seleccion_cafe, bg="black")  # Frapuchino
    boton1.place(x=10, y=20)
    etiqueta1 = Label(ventana1, text="Moca", justify="center",
                      font=24, fg="white", bg="black")
    etiqueta1.place(x=40, y=16)
    boton2.place(x=10, y=80)
    etiqueta2 = Label(ventana1, text="Capuchino",
                      justify="center", font=24, fg="white", bg="black")
    etiqueta2.place(x=40, y=78)
    boton3.place(x=10, y=140)
    etiqueta3 = Label(ventana1, text="Expresso",
                      justify="center", font=24, fg="white", bg="black")
    etiqueta3.place(x=40, y=138)
    boton4.place(x=330, y=30)
    etiqueta4 = Label(ventana1, text="Latte ", justify="center",
                      font=24, fg="white", bg="black")
    etiqueta4.place(x=290, y=30)
    boton5.place(x=330, y=90)
    etiqueta5 = Label(ventana1, text="Frapuchino",
                      justify="center", font=24, fg="white", bg="black")
    etiqueta5.place(x=240, y=90)
    # Etiquetas de precios
    mostrarp1 = Label(ventana1, text="El Precio es 600",
                      font=14, fg="red", bg="black").place(x=40, y=40)
    mostrarp2 = Label(ventana1, text="El Precio es 800",
                      font=14, fg="red", bg="black").place(x=40, y=100)
    mostrarp3 = Label(ventana1, text="El Precio es 500",
                      font=14, fg="red", bg="black").place(x=40, y=160)
    mostrarp4 = Label(ventana1, text="El Precio es 1000",
                      font=14, fg="red", bg="black").place(x=240, y=60)
    mostrarp5 = Label(ventana1, text="El Precio es 1200",
                      font=14, fg="red", bg="black").place(x=240, y=120)
    # Boton Accion
    Boton = Button(ventana1, text="Presione para continuar",
                   command=tercera_ventana, fg="white", bg="black").place(x=130, y=300)
    # Seleccionde cantidad
    etiqueta2 = Label(ventana1, text="Ingrese La cantidad de cafe",
                      fg="white", bg="black").place(x=10, y=220)  # Sin uso por ahora
    valor = IntVar()
    combo2 = Spinbox(ventana1, from_=1, to=2,
                     textvariable=valor, command=seleccion_cafe)
    combo2.place(x=10, y=250)
    boton_salir = Button(ventana1, text="Salir", command=ventana1.destroy,
                         fg="white", bg="black").place(x=350, y=360)
    ventana1.mainloop()


def tercera_ventana():
    while opccion.get() > 0:
        global ventana1, precio, valor, pago, ventana2
        cantidad = (valor.get())
        ventana1.withdraw()  # Cerramos la ventana "principal"
        ventana2 = Toplevel()  # Se abre una ventana superior
        ventana2.geometry("400x400")
        ventana2.title("Cafetera")
        ventana2.config(bg="Black")
        etiqueta_funcion = Label(ventana2, text="Pantalla de Pago")
        etiqueta_funcion.pack
        pago = StringVar()
        etiqueta9 = Label(ventana2, text="Debe Pagar ---->",
                          fg="white", bg="black").place(x=12, y=20)
        etiqueta1 = Label(ventana2, text="Ingrese el monto: ",
                          fg="white", bg="black").place(x=10, y=50)  # Etiqueta
        montoCaja = Entry(ventana2, textvariable=pago).place(
            x=120, y=50)  # Caja donde ingresar la variable
        boton6 = Button(ventana2, command=pago1, text="Pulse", fg="white", bg="black").place(
            x=130, y=78)  # Botton Para hacer la funcion
        boton_salir2 = Button(ventana2, text="Salir", command=ventana2.destroy,
                              fg="white", bg="black").place(x=350, y=360)  # Bototn salir
        if cantidad == 1:
            imprimir = Label(ventana2, text=(precio), bg="red")
            imprimir.place(x=150, y=20)
            imprimri2 = Label(ventana2, text="Cantidad de Cafe : 1",
                              fg="white", bg="black").place(x=100, y=110)
        else:
            precio = precio*2
            imprimir = Label(ventana2, text=(precio), bg="red")
            imprimir.place(x=150, y=20)
            imprimri2 = Label(ventana2, text="Cantidad de Cafe : 2",
                              fg="white", bg="black").place(x=100, y=110)
        ventana2.mainloop()
        print(precio)
    messagebox.showerror(title="Error", message="Ingrese una opcion!")


def pago1():
    global dinero, pago, pagado, precio, ventana2, boton
    pagado2 = int(pago.get())
    if (pago.get() == "500" or pago.get() == "100"):
        pagado3 = pagado2+pagado
        print("Pagado:", pagado)
        pagado3 = int(pagado)
        messagebox.showinfo(title="Lleva Pagado", message=pagado)
        if (int(pagado3) > precio):
            pagado3 = precio-pagado2
            messagebox.showinfo(title="Su vuelto es", message=pagado3)
            messagebox.showinfo(title="Cafe", message="Aqui esta su Cafe")
            ventana2.withdraw()  # Cerramos la ventana "principal"
            ventana3 = Toplevel()  # Se abre una ventana superior
            ventana3.geometry("400x400")
            ventana3.title("Cafetera")
            ventana3.config(bg="Black")
            boton_reinicio = Button(ventana3, text="Presione para pedir otro cafe",
                                    fg="red", command=segunda).place(x=118, y=120)
            boton_salir = Button(
                ventana3, text="Salir", command=ventana3.destroy, fg="red", bg="black").place(x=180, y=150)
            # salir2=int(salir.get())
            # if salir == 1:
            # ventana3.withdraw
        elif pagado-precio == 0:
            messagebox.showinfo(title="Cafe", message="Aqui esta su Cafe")
            ventana2.withdraw()  # Cerramos la ventana "principal"
            ventana3 = Toplevel()  # Se abre una ventana superior
            ventana3.geometry("400x400")
            ventana3.title("Cafetera")
            ventana3.config(bg="Black")
            boton_reinicio22 = Button(ventana3, text="Presione para pedir otro cafe",
                                      fg="red", command=segunda, bg="black").place(x=118, y=120)
            boton_salir11 = Button(
                ventana3, text="Salir", command=ventana3.destroy, fg="red", bg="black").place(x=180, y=150)
    else:
        messagebox.showerror(
            title="Error", message="Ingrese Un valor correcto")


# Ventana principal
global ventana_inicial
ventana_inicial = Tk()
ventana_inicial.geometry("400x400")
ventana_inicial.title("Cafetera")
imagen = PhotoImage(file="version1.png")
background = Label(image=imagen)
background.place(x=0, y=0, relwidth=1, relheight=1)
# Etiquetas
Etiqueta1_inicial = Label(
    text="Bienvenido a la Cafetera", bg="black", fg="white")
Etiqueta1_inicial.pack()
# Botones
boton1_inicial = Button(text="Continuar", fg="blue",
                        command=segunda, bg="black")
boton1_inicial.place(x=165, y=120)
boton2_inicial = Button(
    text="Salir", command=ventana_inicial.destroy, fg="red", bg="black")
boton2_inicial.place(x=180, y=150)
ventana_inicial.mainloop()
# Terminado ///
