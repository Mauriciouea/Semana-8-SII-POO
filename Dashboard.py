import os

def mostrar_codigo(ruta_script):
    """Muestra el contenido del script especificado."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    """Muestra el menú principal y permite al usuario seleccionar un script."""
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Opciones iniciales del menú
    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 2/2.1. Estructuras de Datos/ejemplo_listas.py',
        '3': 'UNIDAD 3/3.3. Bases de Datos/consultas_sql.py'
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")
        print("A - Agregar un nuevo script")
        print("E - Eliminar un script del menú")

        eleccion = input("Elige un script para ver su código, 'A' para agregar uno, 'E' para eliminar uno o '0' para salir: ").strip().upper()
        
        if eleccion == '0':
            print("¡Hasta luego!")
            break
        elif eleccion == 'A':
            nuevo_script = input("Introduce la ruta del nuevo script (relativa a este directorio): ")
            opciones[str(len(opciones) + 1)] = nuevo_script  # Agrega el nuevo script al menú
            print(f"✓ Script '{nuevo_script}' agregado al menú.")
        elif eleccion == 'E':
            print("\n Scripts en el menú:")
            for key, value in opciones.items():
                print(f"{key} - {value}")
            script_a_eliminar = input("Introduce el número del script que deseas eliminar: ")
            if script_a_eliminar in opciones:
                eliminado = opciones.pop(script_a_eliminar)
                print(f"Script '{eliminado}' eliminado del menú.")
            else:
                print("Número de script no válido.")
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
