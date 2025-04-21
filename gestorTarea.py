import json
print("por fin ...")
def cargarJson(nombreArchivo):
    try:
        with open(nombreArchivo,"r",encoding="utf-8") as archivo:
            contenido=archivo.read().strip()
            if not contenido:
                return {}
            return json.loads(contenido)
            
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        return{}
    except PermissionError:
        return{}
    except IOError:
        return{}
    
def actualizarJson(datos,nombreArchivo):
    with open(nombreArchivo,"w", encoding="utf-8")as archivo:
        json.dump(datos,archivo, indent=4)
        