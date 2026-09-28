import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionRestaurante:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Restaurante - Tkinter")
        self.root.geometry("920x560")
        self.root.minsize(780, 500)

        self.icono_app = None

        # Ruta principal del proyecto
        ruta_base = Path(__file__).resolve().parent

        # Configurar icono de la ventana
        self.configurar_icono_ventana(ruta_base)

        # Preparar los servicios
        archivo_servicio = ArchivoServicio(
            ruta_base / "datos"
        )

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        # Vista que actualmente se encuentra visible
        self.vista_actual = None

        # Mostrar pantalla de inicio de sesión
        self.mostrar_login()

    def configurar_icono_ventana(self, ruta_base):
        """
        Carga el icono de la aplicación desde:
        assets/logo/icono.png
        """

        ruta_icono = (
            ruta_base
            / "assets"
            / "logo"
            / "icono.png"
        )

        if not ruta_icono.exists():
            return

        try:
            self.icono_app = tk.PhotoImage(
                file=str(ruta_icono)
            )

            self.root.iconphoto(
                True,
                self.icono_app
            )

        except tk.TclError:
            pass

    def cambiar_vista(self, nueva_vista):
        """
        Reemplaza la vista actual por una nueva
        dentro de la misma ventana.
        """

        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = nueva_vista

        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_login(self):
        """
        Muestra la pantalla de inicio de sesión.
        """

        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_interfaz_principal
        )

        self.cambiar_vista(vista)

    def mostrar_interfaz_principal(self, usuario_actual):
        """
        Muestra la interfaz principal después
        de iniciar sesión correctamente.
        """

        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )

        self.cambiar_vista(vista)

    def ejecutar(self):
        """
        Inicia el ciclo principal de Tkinter.
        """

        self.root.mainloop()


if __name__ == "__main__":
    app = AplicacionRestaurante()
    app.ejecutar()