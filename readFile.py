def readFile(fileToRead):   
    try:
        with open(fileToRead, 'r', encoding='utf-8') as file:                        
            for line in file:                
                print(line)
    except FileNotFoundError:
        print(f"Error: El archivo '{fileToRead}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

fileToRead = "informacion.txt"
readFile(fileToRead)