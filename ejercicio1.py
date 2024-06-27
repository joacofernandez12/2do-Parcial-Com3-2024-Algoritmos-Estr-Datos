 code>(11, 7, 2023)</code>.<
  fecha1 = date(11, 7, 2023) 
  fecha2 = date(2024, 7, 5) 
 dcalcular_dif_fecha(self, otra_fecha):
 dcalcular_dif_fechaiferencia = fecha2 - fecha1 print(f"La diferencia en días entre {fecha1} y {fecha2} es de {dias_de_diferencia} días.")
 class Alumno(dict):
     __init__(self, nombre: str, dni: int, fecha_ingreso: date, carrera: str):
        super().__init__()
        self['Nombre'] = nombre
        self['DNI'] = dni
        self['FechaIngreso'] = fecha_ingreso
        self['Carrera'] = carrera
 alumno = Alumno("Javier Gomez", 43356847, datetime(2022, 1, 15), "Ingeniería")print(alumno)
 antiguedad(self):
        hoy = date.today()
        delta = hoy - self['FechaIngreso']
        return delta.days // 365
__init__(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None 
        ListaDoblementeEnlazada:
        __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
lista_alumnos = ListadoblementeEnlazada()
 lista_alumnos.agregar(alumno1)
 lista_alumnos.agregar(alumno2)
 lista_alumnos.agregar(alumno3)
 alumno1 = Alumno("Lucas Denegri", 39562715, datetime(2020, 3, 25), "Derecho")
alumno2 = Alumno("Julieta Perez", 41256845 , datetime(2021, 2, 20), "Medicina")
 alumno3 = Alumno("Gustavo Vera", 42954623, datetime(2022, 1, 15), "Ingeniería")
 
__init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def esta_vacia(self):
        return self.size == 0

    def agregar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.size += 1
lista_alumnos = ListaDoblementeEnlazada()
.agregar(alumno2)
lista_alumnos.agregar(alumno3)
lista_alumnos.agregar(alumno1)
alumno3 = Alumno("Julieta Perez", 41256845 , datetime(2020, 2, 20), "Medicina")
alumno1 = Alumno("Gustavo Vera", 42954623, datetime(2022, 1, 15), "Ingeniería")
alumno2 = Alumno("Lucas Denegri", 39562715, datetime(2023, 3, 25), "Derecho")
crear_directorio(directorio): os.makedirs(directorio)
        print(f"Directorio '{directorio}' creado.")
    except FileExistsError:
        print(f"El directorio '{directorio}' ya existe.")
    except Exception as e:
        print(f"Error al crear el directorio '{directorio}': {e}")
guardar_lista_alumnos(directorio, nombre_archivo, lista_alumnos):
open(os.path.join(directorio, nombre_archivo), 'w') as archivo:
            json.dump([dict(alumno) for alumno in lista_alumnos], archivo, indent=4)
        print(f"Archivo '{nombre_archivo}' guardado en el directorio '{directorio}'.")
        mover_directorio(origen, destino): os.rename(origen, destino)
        print(f"Directorio movido de '{origen}' a '{destino}'.")
        print(f"Error al mover el directorio de '{origen}' a '{destino}': {e}")borrar_archivo(directorio, nombre_archivo):os.rename(origen, destino)
        print(f"Directorio movido de '{origen}' a '{destino}'.")
    except Exception as e:
        print(f"Error al mover el directorio de '{origen}' a '{destino}': {e}")
borrar_archivo(directorio, nombre_archivo):os.remove(os.path.join(directorio, nombre_archivo))
        print(f"Archivo '{nombre_archivo}' eliminado del directorio '{directorio}'.")
    except Exception as e:
        print(f"Error al eliminar el archivo '{nombre_archivo}': {e}")
borrar_directorio(directorio): os.rmdir(directorio)
        print(f"Directorio '{directorio}' eliminado.")
    except Exception as e:
        print(f"Error al eliminar el directorio '{directorio}': {e}")