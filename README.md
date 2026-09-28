# Restaurante_app__2.7
Nombre: Arely Betzabe Poalasin Shiguango
## Aplicación de gestión de restaurante con Python y Tkinter

## 1. Descripción del proyecto

**Restaurante_app__2.7** es una aplicación de escritorio desarrollada en **Python** utilizando **Tkinter** para la creación de la interfaz gráfica.

El proyecto representa la evolución de una aplicación de restaurante desarrollada durante diferentes semanas de la asignatura de Programación Orientada a Objetos. En esta versión se conserva la estructura modular del proyecto y se incorporan mejoras en la interfaz gráfica y en el manejo de eventos.

La aplicación permite trabajar principalmente con:

- Usuarios.
- Productos.
- Ventas.
- Persistencia de información mediante archivos JSON.
- Inicio de sesión.
- Interfaz gráfica.
- Operaciones CRUD para productos.
- Registro de ventas.
- Navegación mediante un menú lateral.
- Manejo de eventos mediante botones y callbacks.

Además, se incorporó una carpeta `assets` para organizar los recursos visuales utilizados por la aplicación, incluyendo el logotipo y los iconos de las diferentes opciones del sistema.

---

# 2. Objetivo del proyecto

El objetivo de `Restaurante_app__2.6` es desarrollar una aplicación de escritorio funcional para administrar información básica de un restaurante, aplicando los conocimientos adquiridos sobre programación orientada a objetos, interfaces gráficas, persistencia de datos y manejo de eventos.

En esta versión se buscó principalmente:

- Mantener la arquitectura modular desarrollada anteriormente.
- Separar la interfaz gráfica de la lógica del negocio.
- Mantener la información almacenada en archivos JSON.
- Incorporar una sección para registrar ventas.
- Relacionar usuarios con productos al momento de registrar una venta.
- Utilizar botones asociados mediante `command=`.
- Utilizar métodos callback para responder a las acciones del usuario.
- Mejorar la presentación visual de la aplicación.
- Organizar los recursos gráficos dentro de `assets`.
- Corregir el tamaño de los iconos para que puedan visualizarse correctamente.
- Mantener la aplicación preparada para continuar evolucionando en futuras semanas.

---

# 3. Tecnologías utilizadas

El proyecto fue desarrollado con las siguientes tecnologías y herramientas:

| Tecnología | Uso dentro del proyecto |
|---|---|
| Python | Lenguaje principal |
| Tkinter | Creación de la interfaz gráfica |
| ttk | Componentes gráficos y estilos |
| JSON | Almacenamiento de información |
| pathlib | Manejo de rutas y archivos |
| Git | Control de versiones |
| GitHub | Almacenamiento y publicación del proyecto |

No se utiliza una base de datos externa. La información se conserva mediante archivos JSON ubicados dentro de la carpeta `datos`.

---

# 4. Estructura del proyecto

La organización principal de `Restaurante_app__2.6` es la siguiente:

```text
Restaurante_app__2.6/
│
├── main.py
│
├── assets/
│   ├── logo/
│   │   ├── logo.png
│   │   └── icono.png
│   │
│   └── icons/
│       ├── home.png
│       ├── users.png
│       ├── products.png
│       ├── sales.png
│       ├── logout.png
│       ├── add.png
│       ├── search.png
│       ├── edit.png
│       ├── delete.png
│       └── clean.png
│
├── datos/
│   ├── usuarios.json
│   ├── productos.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
└── README.md
```

Cada carpeta cumple una función específica dentro del sistema.

---

# 5. Organización por módulos

Uno de los aspectos importantes del proyecto es que no se colocó todo el código dentro de `main.py`.

El sistema se dividió en diferentes módulos para facilitar su mantenimiento y comprensión.

La organización utilizada es:

```text
main.py
   ↓
ui
   ↓
servicios
   ↓
modelos
   ↓
datos JSON
```

La interfaz se encarga principalmente de recibir las acciones del usuario y mostrar información, mientras que los servicios realizan las operaciones correspondientes.

---

# 6. Archivo `main.py`

El archivo `main.py` es el punto de entrada de la aplicación.

Su función principal es preparar la ventana de Tkinter, configurar sus dimensiones, cargar el icono de la aplicación, crear los servicios y mostrar inicialmente la pantalla de inicio de sesión.

La ventana principal se configura con:

```python
self.root.title("Restaurante - Tkinter")
self.root.geometry("920x560")
self.root.minsize(780, 500)
```

Esto permite que la aplicación tenga un tamaño adecuado para mostrar el menú lateral y el contenido principal.

También se establece el icono de la ventana mediante:

```python
self.root.iconphoto(True, self.icono_app)
```

El archivo utilizado para este propósito es:

```text
assets/logo/icono.png
```

---

# 7. Cambio de vistas

La aplicación utiliza una variable para controlar la vista actualmente mostrada:

```python
self.vista_actual = None
```

Cuando se necesita cambiar de pantalla, se destruye la vista anterior y se coloca la nueva.

El procedimiento utilizado es:

```python
def cambiar_vista(self, nueva_vista):
    if self.vista_actual is not None:
        self.vista_actual.destroy()

    self.vista_actual = nueva_vista
    self.vista_actual.pack(fill="both", expand=True)
```

Esto permite utilizar una sola ventana principal y cambiar el contenido que se presenta al usuario.

El flujo inicial es:

```text
main.py
   ↓
LoginView
   ↓
validación
   ↓
MainView
```

---

# 8. Pantalla de inicio de sesión

La pantalla de inicio de sesión se encuentra en:

```text
ui/login_view.py
```

Su función es permitir que el usuario ingrese al sistema antes de acceder a las funciones principales.

Esta vista utiliza los servicios del restaurante para realizar la validación correspondiente.

Una vez que el usuario inicia sesión correctamente, se ejecuta el callback:

```text
al_iniciar_sesion
```

y la aplicación cambia hacia `MainView`.

---

# 9. Ventana principal

La ventana principal se encuentra en:

```text
ui/main_view.py
```

Esta es la parte principal de la interfaz después del inicio de sesión.

Se dividió visualmente en dos áreas:

```text
┌─────────────────────┬──────────────────────────────────┐
│                     │                                  │
│      MENÚ           │          CONTENIDO               │
│      LATERAL        │          PRINCIPAL              │
│                     │                                  │
│      Inicio         │                                  │
│      Usuarios       │                                  │
│      Productos      │                                  │
│      Ventas         │                                  │
│                     │                                  │
│      Cerrar sesión  │                                  │
│                     │                                  │
└─────────────────────┴──────────────────────────────────┘
```

El menú permite navegar entre las diferentes secciones del sistema.

---

# 10. Menú lateral

El menú lateral fue diseñado utilizando un `Frame` de Tkinter.

Dentro de este panel se incorporaron:

- Logo.
- Nombre del usuario actual.
- Botón Inicio.
- Botón Usuarios.
- Botón Productos.
- Botón Ventas.
- Botón Cerrar sesión.

Los botones se crean mediante un método reutilizable:

```python
crear_boton(...)
```

Esto evita repetir el mismo código para cada botón.

---

# 11. Uso de imágenes e iconos

En esta versión se incorporaron recursos visuales mediante la carpeta:

```text
assets/
```

La organización utilizada es:

```text
assets/
│
├── logo/
│   ├── logo.png
│   └── icono.png
│
└── icons/
    ├── home.png
    ├── users.png
    ├── products.png
    ├── sales.png
    ├── logout.png
    ├── add.png
    ├── search.png
    ├── edit.png
    ├── delete.png
    └── clean.png
```

Se decidió separar el logotipo de los iconos funcionales.

### `logo.png`

Se utiliza como logotipo dentro de la interfaz.

### `icono.png`

Se utiliza como icono de la ventana de la aplicación.

### Iconos de `icons`

Se utilizan en los botones de navegación y en las diferentes acciones del sistema.

---

# 12. Corrección del tamaño de los iconos

Durante el desarrollo se detectó un problema visual: algunos archivos PNG tenían dimensiones que provocaban que los botones del menú ocuparan demasiado espacio.

En otros casos, los iconos se visualizaban demasiado pequeños.

Para solucionar este problema se modificó el método encargado de cargar los iconos.

La aplicación obtiene primero la imagen:

```python
icono_original = tk.PhotoImage(
    file=str(ruta_icono)
)
```

Posteriormente se comprueba su tamaño y se realiza el ajuste correspondiente.

Cuando el icono es demasiado pequeño se utiliza:

```python
icono_original.zoom(
    factor,
    factor
)
```

De esta forma, los iconos pueden visualizarse con un tamaño más apropiado dentro de los botones.

También se mantiene una referencia de las imágenes mediante:

```python
self.iconos[nombre_archivo] = icono
```

Esto es importante porque Tkinter puede eliminar una imagen de memoria si no existe una referencia activa hacia ella.

---

# 13. Logo del menú lateral

El logotipo también se carga de manera independiente.

La aplicación utiliza:

```text
assets/logo/logo.png
```

para mostrarlo en la parte superior del menú lateral.

El tamaño se controla antes de mostrarlo para evitar que una imagen demasiado grande ocupe todo el menú.

De esta manera se consiguió una distribución más equilibrada:

```text
┌─────────────────────┐
│       LOGO          │
│                     │
│ Usuario actual      │
│                     │
│ Inicio              │
│ Usuarios            │
│ Productos           │
│ Ventas              │
│                     │
│                     │
│ Cerrar sesión       │
└─────────────────────┘
```

---

# 14. Sección Inicio

La opción **Inicio** muestra un resumen general de la información disponible.

Se presentan tarjetas con cantidades como:

- Usuarios registrados.
- Productos registrados.
- Ventas registradas.

Por ejemplo:

```text
Usuarios registrados     3

Productos registrados    5

Ventas registradas       4
```

Las cantidades se obtienen desde `RestauranteServicio`.

Esto permite que la información mostrada en la pantalla se actualice de acuerdo con los datos almacenados.

---

# 15. Sección Usuarios

La opción **Usuarios** permite consultar los usuarios registrados.

La información se presenta utilizando un `Treeview`.

Las columnas utilizadas incluyen:

```text
Identificador
Nombre
Usuario
```

Los datos se obtienen mediante:

```python
self.restaurante_servicio.listar_usuarios()
```

La interfaz no accede directamente al archivo JSON.

En cambio, solicita la información al servicio correspondiente.

---

# 16. Sección Productos

La sección **Productos** permite gestionar los productos del restaurante.

La interfaz contiene un formulario para introducir:

```text
Código
Nombre
Categoría
Precio
```

También se incorporaron botones para realizar diferentes operaciones.

```text
Registrar
Cargar por código
Actualizar
Eliminar
Limpiar
```

Cada botón ejecuta un método específico.

---

# 17. Registro de productos

Para registrar un producto se utiliza:

```python
self.registrar_producto
```

El método obtiene la información introducida en el formulario y la envía al servicio:

```python
self.restaurante_servicio.registrar_producto(...)
```

Después de registrar correctamente el producto:

1. Se limpia el formulario.
2. Se actualiza la tabla.
3. Se muestra un mensaje al usuario.
4. Se actualiza la información de la barra de estado.

---

# 18. Búsqueda de productos

El sistema permite buscar un producto utilizando su código.

El método:

```python
cargar_producto_en_formulario()
```

obtiene el código introducido y solicita al servicio que encuentre el producto.

Si el producto existe, sus datos son cargados nuevamente en el formulario.

Esto facilita posteriormente su actualización.

---

# 19. Actualización de productos

La opción **Actualizar** utiliza los datos existentes en el formulario.

La información se envía al servicio:

```python
self.restaurante_servicio.actualizar_producto(...)
```

Si la operación es correcta, la tabla se actualiza para mostrar los nuevos datos.

---

# 20. Eliminación de productos

La opción **Eliminar** utiliza el código del producto.

El método:

```python
eliminar_producto()
```

solicita al servicio que elimine el producto correspondiente.

Después de realizar la operación se:

- Limpia el formulario.
- Actualiza la tabla.
- Actualiza el contador de productos.
- Muestra un mensaje de confirmación.

---

# 21. Sección Ventas

La sección **Ventas** fue incorporada para aplicar el manejo básico de eventos.

En esta sección se puede seleccionar:

- Un usuario existente.
- Un producto existente.

La interfaz utiliza componentes `Combobox` para realizar estas selecciones.

La estructura visual es:

```text
Registrar venta

Usuario:    [ Usuario seleccionado ]

Producto:   [ Producto seleccionado ]

            [ Registrar venta ]
```

Debajo se encuentra la tabla de ventas registradas.

---

# 22. Relación entre usuario y producto

Para registrar una venta no se crean usuarios ni productos nuevos.

Se utilizan elementos que ya existen en el sistema.

Los usuarios se obtienen mediante:

```python
self.restaurante_servicio.listar_usuarios()
```

Los productos se obtienen mediante:

```python
self.restaurante_servicio.listar_productos()
```

Posteriormente se construyen las opciones de los `Combobox`.

Por ejemplo:

```text
001 - Juan Pérez
002 - María López
```

y:

```text
P001 - Hamburguesa
P002 - Jugo natural
```

Internamente se conserva el identificador correspondiente.

---

# 23. Manejo de eventos

Uno de los conceptos principales incorporados en esta versión es el manejo de eventos de Tkinter.

Un evento ocurre cuando el usuario realiza una acción sobre un componente de la interfaz.

En este proyecto, el ejemplo principal es el botón:

```text
Registrar venta
```

El botón se relaciona con el método:

```python
self.registrar_venta
```

mediante:

```python
command=self.registrar_venta
```

Esto significa que el método no se ejecuta al crear el botón, sino cuando el usuario hace clic sobre él.

---

# 24. Flujo del evento de una venta

El proceso completo de registro de una venta funciona de la siguiente manera:

```text
1. El usuario abre la sección Ventas
                ↓
2. Selecciona un usuario
                ↓
3. Selecciona un producto
                ↓
4. Presiona "Registrar venta"
                ↓
5. Tkinter ejecuta el callback
                ↓
6. registrar_venta() obtiene las selecciones
                ↓
7. Se identifican usuario y producto
                ↓
8. Se llama a RestauranteServicio
                ↓
9. Se registra la venta
                ↓
10. Se guarda la información
                ↓
11. Se actualiza la tabla
                ↓
12. Se muestra un mensaje al usuario
```

Este flujo permite observar claramente la comunicación entre la interfaz y la lógica del sistema.

---

# 25. Callback `registrar_venta`

El método:

```python
registrar_venta()
```

funciona como callback de la operación.

Primero obtiene el usuario seleccionado:

```python
usuario_id = self.opciones_usuarios_venta.get(
    self.usuario_venta_combo.get(),
    ""
)
```

Después obtiene el producto:

```python
producto_codigo = self.opciones_productos_venta.get(
    self.producto_venta_combo.get(),
    ""
)
```

Finalmente solicita al servicio registrar la venta:

```python
venta = self.restaurante_servicio.registrar_venta(
    usuario_id,
    producto_codigo,
)
```

La interfaz, por lo tanto, no se encarga directamente de escribir el archivo JSON.

---

# 26. Persistencia de las ventas

Las ventas se almacenan en:

```text
datos/ventas.json
```

Esto permite que la información permanezca disponible después de cerrar el programa.

Cuando se inicia nuevamente la aplicación, los datos pueden ser recuperados mediante los servicios correspondientes.

El proceso de persistencia mantiene la separación:

```text
MainView
   ↓
RestauranteServicio
   ↓
ArchivoServicio
   ↓
ventas.json
```

---

# 27. Tabla de ventas

Después de registrar una venta, la interfaz actualiza el `Treeview`.

La tabla contiene información como:

```text
Venta
Usuario
Producto
Fecha
```

La información relacionada con el usuario y el producto se busca mediante sus identificadores.

Por ejemplo:

```text
Venta     Usuario             Producto             Fecha
1         001 - Juan Pérez    P001 - Hamburguesa   ...
2         002 - María López   P002 - Jugo          ...
```

Esto permite que la información sea más comprensible para el usuario.

---

# 28. Actualización de la interfaz

Después de realizar una operación, la aplicación actualiza la información mostrada.

Por ejemplo, después de registrar una venta:

```python
self.limpiar_formulario_venta()
self.refrescar_ventas()
```

De esta manera:

1. Se limpian las selecciones.
2. Se vuelve a cargar la tabla.
3. Se actualiza el contador de ventas.
4. El usuario recibe una confirmación.

Esto evita que el usuario tenga que cerrar y volver a abrir la aplicación para visualizar el cambio.

---

# 29. Barra de estado

La ventana principal también incluye una barra de estado.

Esta permite visualizar información general del sistema:

```text
Productos: X | Usuarios: X | Ventas: X | Datos JSON locales
```

Los valores se actualizan mediante:

```python
actualizar_barra_estado()
```

Esto permite tener una referencia rápida del contenido registrado.

---

# 30. Cierre de sesión

La aplicación cuenta con un botón:

```text
Cerrar sesión
```

Este botón utiliza un callback:

```python
self.cerrar_sesion
```

Al ejecutarse, se llama al método proporcionado desde `main.py`:

```python
self.al_cerrar_sesion()
```

Esto permite regresar a la pantalla de inicio de sesión sin cerrar completamente la aplicación.

---

# 31. Manejo de errores

En las operaciones de productos y ventas se utilizan bloques `try/except`.

Por ejemplo:

```python
try:
    ...
except ValueError as error:
    messagebox.showerror(
        "Ventas",
        str(error)
    )
```

Esto permite mostrar mensajes comprensibles cuando una operación no puede realizarse.

De esta manera se evita que un error de validación provoque directamente el cierre de la aplicación.

---

# 32. Separación de responsabilidades

Uno de los aspectos importantes del proyecto es la separación entre las diferentes partes del sistema.

### Interfaz

Se encuentra principalmente en:

```text
ui/
```

Su función es mostrar información y recibir acciones.

### Servicios

Se encuentran en:

```text
servicios/
```

Contienen la lógica de las operaciones.

### Modelos

Se encuentran en:

```text
modelos/
```

Representan las entidades utilizadas por el sistema.

### Datos

Se encuentran en:

```text
datos/
```

Conservan la información mediante archivos JSON.

### Recursos visuales

Se encuentran en:

```text
assets/
```

Contienen los iconos y logotipos utilizados por la aplicación.

---

# 33. Flujo general de la aplicación

El funcionamiento completo puede representarse de la siguiente manera:

```text
                         ┌──────────────┐
                         │   main.py    │
                         └──────┬───────┘
                                │
                                ↓
                       ┌─────────────────┐
                       │    LoginView    │
                       └────────┬────────┘
                                │
                         Inicio de sesión
                                │
                                ↓
                       ┌─────────────────┐
                       │    MainView     │
                       └────────┬────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ↓                  ↓                  ↓
         Usuarios           Productos           Ventas
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ↓
                    RestauranteServicio
                                ↓
                       ArchivoServicio
                                ↓
                         Archivos JSON
```

---

# 34. Paso a paso de la evolución realizada

## Paso 1. Organización del proyecto

Se mantuvo una estructura modular para separar la interfaz, los servicios, los modelos y los datos.

---

## Paso 2. Preparación de los archivos JSON

Se conservaron los archivos destinados al almacenamiento de:

```text
usuarios.json
productos.json
ventas.json
```

---

## Paso 3. Preparación de los servicios

Se mantuvieron:

```text
ArchivoServicio
RestauranteServicio
```

para manejar el acceso y las operaciones relacionadas con los datos.

---

## Paso 4. Implementación del inicio de sesión

Se mantuvo `LoginView` como primera pantalla de la aplicación.

Después de validar al usuario se muestra `MainView`.

---

## Paso 5. Organización de la ventana principal

Se construyó un menú lateral y un área de contenido.

El menú permite cambiar entre:

```text
Inicio
Usuarios
Productos
Ventas
```

---

## Paso 6. Incorporación de recursos gráficos

Se creó la organización:

```text
assets/logo/
assets/icons/
```

para mantener separados los recursos visuales.

---

## Paso 7. Corrección de los iconos

Durante las pruebas se observó que algunos PNG tenían un tamaño inadecuado.

Se modificó la carga de imágenes para controlar su tamaño mediante `PhotoImage`, `zoom()` y `subsample()` según el caso.

También se conservaron referencias a las imágenes para evitar problemas de visualización en Tkinter.

---

## Paso 8. Incorporación de ventas

Se agregó una sección específica para registrar ventas.

Esta sección utiliza un usuario y un producto existentes.

---

## Paso 9. Implementación del evento

El botón:

```text
Registrar venta
```

se conectó con el callback:

```python
command=self.registrar_venta
```

De esta forma, el clic del usuario inicia la operación.

---

## Paso 10. Comunicación con el servicio

El callback obtiene las selecciones y las envía a:

```python
RestauranteServicio
```

La interfaz no realiza directamente la persistencia.

---

## Paso 11. Guardado de la venta

La venta se almacena en:

```text
datos/ventas.json
```

permitiendo conservar la información.

---

## Paso 12. Actualización visual

Después de registrar una venta:

- Se limpia el formulario.
- Se actualiza la tabla.
- Se actualizan los contadores.
- Se muestra un mensaje de confirmación.

---

# 35. Ejemplo del manejo de eventos

El concepto de evento puede observarse de manera sencilla:

```python
boton = ttk.Button(
    contenedor,
    text="Registrar venta",
    command=self.registrar_venta
)
```

Cuando se crea el botón, solamente se establece qué método debe ejecutarse.

La acción ocurre posteriormente:

```text
Usuario hace clic
        ↓
Tkinter detecta el evento
        ↓
Ejecuta registrar_venta()
        ↓
Se obtiene la información
        ↓
Se llama al servicio
        ↓
Se guarda la venta
        ↓
Se actualiza la interfaz
```

Es importante que se utilice:

```python
command=self.registrar_venta
```

y no:

```python
command=self.registrar_venta()
```

porque la segunda forma ejecutaría el método inmediatamente al construir el botón.

---

# 36. Ejecución del proyecto

Para ejecutar el proyecto se necesita tener instalado Python.

Desde la terminal se debe ingresar a la carpeta del proyecto:

```bash
cd C:\Restaurante_app__2.6
```

Después se ejecuta:

```bash
python main.py
```

También puede ejecutarse utilizando directamente el intérprete de Python instalado en el equipo.

---

# 37. Inicio de la aplicación

Al ejecutar:

```bash
python main.py
```

se abre la ventana de la aplicación.

El proceso esperado es:

```text
Aplicación
   ↓
Inicio de sesión
   ↓
Validación
   ↓
Panel principal
```

Una vez dentro del panel principal se puede utilizar el menú lateral.

---

# 38. Pruebas realizadas

Durante el desarrollo se realizaron comprobaciones relacionadas con:

### Inicio de la aplicación

Se verificó que `main.py` pudiera iniciar la aplicación y cargar los servicios.

### Inicio de sesión

Se comprobó la navegación desde `LoginView` hacia `MainView`.

### Menú lateral

Se verificó que las diferentes opciones fueran visibles y funcionales.

### Iconos

Se corrigió el tamaño de los archivos PNG para evitar que ocuparan demasiado espacio o fueran prácticamente invisibles.

### Productos

Se comprobó el funcionamiento de:

- Registro.
- Búsqueda.
- Actualización.
- Eliminación.
- Limpieza del formulario.

### Usuarios

Se comprobó la visualización de los usuarios registrados.

### Ventas

Se comprobó la selección de usuario y producto y el registro de una venta.

### Persistencia

Se verificó el uso de los archivos JSON para conservar los datos.

---

# 39. Resultado final

La versión `Restaurante_app__2.6` permite contar con una aplicación de restaurante más organizada y visualmente completa.

El sistema integra:

```text
Inicio de sesión
       +
Interfaz gráfica
       +
Usuarios
       +
Productos
       +
Ventas
       +
Persistencia JSON
       +
Manejo de eventos
       +
Callbacks
       +
Recursos gráficos
```

La incorporación del manejo de eventos permite que las acciones realizadas por el usuario tengan una respuesta dentro del sistema, manteniendo la lógica principal fuera de la interfaz.

---

# 40. Conclusiones

El desarrollo de `Restaurante_app__2.6` permitió continuar la evolución del sistema de restaurante incorporando nuevos elementos sin tener que reconstruir la aplicación desde cero.

Uno de los aprendizajes principales fue comprender cómo una acción realizada en una interfaz gráfica puede iniciar una operación mediante un evento. En este caso, el botón de registro de venta utiliza `command=` para ejecutar un callback que obtiene la información seleccionada y la comunica con `RestauranteServicio`.

También se reforzó la importancia de mantener separadas las responsabilidades. La interfaz se encarga de la interacción con el usuario, mientras que los servicios realizan las operaciones y los archivos JSON permiten conservar la información.

Otro aspecto trabajado fue la mejora visual de la aplicación. La organización de los recursos dentro de `assets` permitió separar el logotipo de los iconos. Además, se corrigió el tamaño de las imágenes para que los elementos gráficos se integraran correctamente en el menú y los botones.

En conjunto, esta versión representa una continuación del proyecto anterior y deja una base organizada para incorporar nuevas funcionalidades en las siguientes etapas.

---

# 41. Autor

**Arely Betzabe Poalasin Shiguango**

Proyecto académico desarrollado en Python como parte de la asignatura de Programación Orientada a Objetos.

---

# 42. Resumen de funcionalidades

| Funcionalidad | Estado |
|---|---|
| Inicio de sesión | Implementado |
| Interfaz gráfica Tkinter | Implementado |
| Menú lateral | Implementado |
| Logo del restaurante | Implementado |
| Icono de aplicación | Implementado |
| Iconos de navegación | Implementado |
| Gestión de usuarios | Implementado |
| Gestión de productos | Implementado |
| Registro de productos | Implementado |
| Búsqueda de productos | Implementado |
| Actualización de productos | Implementado |
| Eliminación de productos | Implementado |
| Registro de ventas | Implementado |
| Selección de usuario | Implementado |
| Selección de producto | Implementado |
| Manejo de eventos | Implementado |
| Uso de `command=` | Implementado |
| Callbacks | Implementado |
| Persistencia JSON | Implementado |
| Tabla de información | Implementado |
| Barra de estado | Implementado |
| Cierre de sesión | Implementado |

---

# 43. Comando de ejecución

Para iniciar la aplicación:

```bash
python main.py
```

El proyecto está preparado para continuar su desarrollo manteniendo la arquitectura modular y las funcionalidades incorporadas hasta la versión `Restaurante_app__2.6`.
