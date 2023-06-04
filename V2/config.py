import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Config:
    def __init__(self) -> None:
        self.size="1000x800"
        # Cargar la imagen de fondo
        self.image = Image.open("background.png")
        self.bg_image = ImageTk.PhotoImage(self.image)
        
        self.styles_config = {         
                "TNotebook": {
                    "configure": {
                        "tabmargins": [0, 0, 0, 0],
                        "tabposition":'wn',
                        "background": "gray",
                    } 
                }, 

                "TNotebook.Tab": {
                    "configure": {
                        "padding": [12, 8],
                        "background": "lightgray",
                        "width" :22,
                        "foreground":"black"
                    },
                    "map": {
                        "background": [("selected", "lightblue"),("active", "white")],
                        "expand": [("selected", [1, 1, 1, 0])] ,
                },
                    
                },
        }
        self.styles = ttk.Style()
        #Si existe el estilo da error y lo modifica o actualiza.
        try:
            self.styles.theme_create( "MyStyle", parent="alt", settings= self.styles_config)
        except:
            #Actualiza el fondo que tiene
            self.styles.theme_settings( "MyStyle", settings= self.styles_config)
        self.styles.theme_use("MyStyle")