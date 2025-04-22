import json

def cargarJson(nombreArchivo):
    try:
        with open(nombreArchivo, 'r', encoding='utf-8') as file:
            content = file.read().strip()  
            if not content:
                return {}  
            return json.loads(content)  

    except FileNotFoundError:
        print("Archivo no Existente, se retornara un diccionario vacio")
        return {}
    except PermissionError:
        print("Permisos no necesarios para leer el archivo, se retornara un diccionario vacio")
        return {}
    except json.JSONDecodeError as e:
        return {}
    except IOError:
        return {}

def updateJson(datos,nombreArchivo):
    with open(nombreArchivo,'w',encoding="utf-8") as file: 
        json.dump(datos,file,indent=4)