import os
def pecera(largoMin, largoMax, largoPeces):
    count = 0
    
    for jhon_size in range(largoMin, largoMax + 1):
        valid = True
        # print (f"Jhon: {jhon_size}")
        
        for pez in largoPeces:
            # print(f"Pez: {pez}")
            if jhon_size >= pez / 10 and jhon_size <= pez / 2:
                valid = False
                break
            
            if pez >= jhon_size / 10 and pez <= jhon_size / 2:
                valid = False
                break
        
        if valid:
            count += 1
            # print(f"Tamaño válido para Jhon: {jhon_size}")
    
    return count


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = os.path.join(current_dir, 'problema_01_input.txt')
    output_file = os.path.join(current_dir, 'output.txt')

    try:
        with open(input_file, 'r') as br:
            with open(output_file, 'w') as fw:
                for line in br:
                    parts = line.strip().split(';')
                    
                    largoMin = int(parts[0])
                    largoMax = int(parts[1])
                    largoPeces = list(map(int, parts[2].split(',')))
                    
                    cantidad_validos = pecera(largoMin, largoMax, largoPeces)
                    
                    fw.write(f"{cantidad_validos}\n")
                    
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    except IOError as e:
        print(f"Error de E/S: {e}")

if __name__ == "__main__":
    main()