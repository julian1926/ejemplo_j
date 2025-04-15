import json
def cargarJson(nombreArchivo):
    try:
        with open(nombreArchivo, "r", encoding="utf-8") as file:
            contenido=file.read().strip()
            if not contenido:
                return {}
            return json.loads(contenido)
        
    except FileNotFoundError:
        return {}
    except PermissionError:
        return {}
    except json.JSONDecodeError:
        return{}
    except IOError:
        return {}
    
def actualizarJson(datos,nombreArchivo):
    with open(nombreArchivo, "w", encoding="utf-8")as file:
        json.dump(datos,file , indent=4)
        

