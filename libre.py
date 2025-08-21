#!/usr/bin/env python3

import time
import os
import urllib.request
import shutil
import sys
import zipfile

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_ascii_art():
    ascii_art = """
 /$$       /$$ /$$                           /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$ 
| $$      |__/| $$                          | $$  / $$ /$$__  $$ /$$__  $$ /$$$_  $$
| $$       /$$| $$$$$$$   /$$$$$$   /$$$$$$ |  $$/ $$/|__/  \ $$| $$  \__/| $$$$\ $$
| $$      | $$| $$__  $$ /$$__  $$ /$$__  $$ \  $$$$/    /$$$$$/| $$$$$$$ | $$ $$ $$
| $$      | $$| $$  \ $$| $$  \__/| $$$$$$$$  >$$  $$   |___  $$| $$__  $$| $$\ $$$$
| $$      | $$| $$  | $$| $$      | $$_____/ /$$/\  $$ /$$  \ $$| $$  \ $$| $$ \ $$$
| $$$$$$$$| $$| $$$$$$$/| $$      |  $$$$$$$| $$  \ $$|  $$$$$$/|  $$$$$$/|  $$$$$$/
|________/|__/|_______/ |__/       \_______/|__/  |__/ \______/  \______/  \______/ 

                             > github.com/plvxt <                                       
    """
    print(ascii_art)

def create_xploit_folders():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    xploit_dir = os.path.join(base_dir, "Xploit")
    entry_point_dir = os.path.join(xploit_dir, "Content", "0000000000000000", "5841122D", "000D0000")
    os.makedirs(entry_point_dir, exist_ok=True)
    return xploit_dir, entry_point_dir

def download_entry_point(entry_point_dir):
    clear_screen()
    print_ascii_art()
    
    url = "https://archive.org/download/bb360demogod/DD774F20C36263F22AFD0A8B6FD742AC9E400B0A58"
    file_path = os.path.join(entry_point_dir, "DD774F20C36263F22AFD0A8B6FD742AC9E400B0A58")
    
    print("\nPaso 1: Descargando Rock Band Blitz (Demo)...\n")
    
    try:
        if os.path.exists(file_path):
            print("El archivo ya existe. Omitiendo descarga.")
            print("Ubicación: " + file_path)
            return True
            
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(int(downloaded * 100 / total_size), 100)
            sys.stdout.write(f"\rProgreso: {percent}% [{downloaded} / {total_size} bytes]")
            sys.stdout.flush()
            
        print(f"Guardando en: {file_path}")
        urllib.request.urlretrieve(url, file_path, reporthook=report_progress)
        
        print("\n\nDescarga completada con éxito.")
        print("\nPaso 1 completado.")
        time.sleep(1.5)
        return True
        
    except Exception as e:
        print(f"\n\nError al descargar el archivo: {e}")
        return False

def download_and_extract_update(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    url = "https://archive.org/download/bad-update/BadUpdate.zip"
    zip_path = os.path.join(xploit_dir, "BadUpdate.zip")
    macosx_folder = os.path.join(xploit_dir, "__MACOSX")
    
    print("\nPaso 2: Descargando y extrayendo BadUpdate.zip...\n")
    
    try:
        if os.path.exists(zip_path):
            print("El archivo BadUpdate.zip ya existe. Omitiendo descarga.")
        else:
            def report_progress(block_num, block_size, total_size):
                downloaded = block_num * block_size
                percent = min(int(downloaded * 100 / total_size), 100)
                sys.stdout.write(f"\rProgreso: {percent}% [{downloaded} / {total_size} bytes]")
                sys.stdout.flush()
            
            print(f"Guardando en: {zip_path}")
            urllib.request.urlretrieve(url, zip_path, reporthook=report_progress)
            print("\n\nDescarga completada con éxito.")
        
        print("\nExtrayendo BadUpdate.zip en la raíz de Xploit...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(xploit_dir)
        
        print("\nExtracción completada con éxito.")
        
        if os.path.exists(zip_path):
            os.remove(zip_path)
            print(f"Archivo {zip_path} eliminado.")
        
        if os.path.exists(macosx_folder) and os.path.isdir(macosx_folder):
            shutil.rmtree(macosx_folder)
        
        print("\nPaso 2 completado.")
        time.sleep(1.5)
        return True
        
    except Exception as e:
        print(f"\n\nError al descargar o extraer el archivo: {e}")
        return False

def download_xeunshackle(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    url = "https://github.com/Byrom90/XeUnshackle/releases/download/v1.02/XeUnshackle-BETA-v1_02.zip"
    zip_path = os.path.join(xploit_dir, "XeUnshackle.zip")
    macosx_folder = os.path.join(xploit_dir, "__MACOSX")
    readme_file = os.path.join(xploit_dir, "README - IMPORTANT.txt")
    temp_dir = os.path.join(xploit_dir, "temp_xeunshackle")
    
    print("\nPaso 3: Descargando y extrayendo XeUnshackle...\n")
    
    try:
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(int(downloaded * 100 / total_size), 100)
            sys.stdout.write(f"\rProgreso: {percent}% [{downloaded} / {total_size} bytes]")
            sys.stdout.flush()
        
        print(f"Guardando en: {zip_path}")
        urllib.request.urlretrieve(url, zip_path, reporthook=report_progress)
        print("\n\nDescarga completada con éxito.")
        
        os.makedirs(temp_dir, exist_ok=True)
        
        print("\nExtrayendo XeUnshackle.zip...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        print("\nMoviendo archivos a la raíz de Xploit...")
        xeunshackle_folder = None
        
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            if os.path.isdir(item_path) and "XeUnshackle" in item:
                xeunshackle_folder = item_path
                break
        
        if xeunshackle_folder:
            for item in os.listdir(xeunshackle_folder):
                src = os.path.join(xeunshackle_folder, item)
                dst = os.path.join(xploit_dir, item)
                
                if item == "BadUpdatePayload" and os.path.isdir(src):
                    if not os.path.exists(dst):
                        shutil.copytree(src, dst)
                    else:
                        for file_item in os.listdir(src):
                            src_file = os.path.join(src, file_item)
                            dst_file = os.path.join(dst, file_item)
                            if os.path.isdir(src_file):
                                if not os.path.exists(dst_file):
                                    shutil.copytree(src_file, dst_file)
                            else:
                                shutil.copy2(src_file, dst_file)
                elif os.path.isdir(src):
                    if os.path.exists(dst) and item != "BadUpdatePayload":
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    if os.path.exists(dst):
                        os.remove(dst)
                    shutil.copy2(src, dst)
            
            print("Archivos movidos correctamente.")
        else:
            print("No se encontró la carpeta XeUnshackle dentro del archivo ZIP.")
        
        shutil.rmtree(temp_dir)
        print(f"Directorio temporal eliminado.")
        
        if os.path.exists(zip_path):
            os.remove(zip_path)
            print(f"Archivo {zip_path} eliminado.")
        
        if os.path.exists(macosx_folder) and os.path.isdir(macosx_folder):
            shutil.rmtree(macosx_folder)
        
        if os.path.exists(readme_file):
            os.remove(readme_file)
        return True
        
    except Exception as e:
        print(f"\n\nError al descargar o extraer el archivo: {e}")
        return False

def download_freemyxe(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    url = "https://archive.org/download/default_freemyxe/default.xex"
    payload_dir = os.path.join(xploit_dir, "BadUpdatePayload")
    file_path = os.path.join(payload_dir, "default.xex")
    
    print("\nPaso 3: Descargando FreeMyXe...\n")
    
    try:
        print("ADVERTENCIA: FreeMyXe no tendrá soporte para Dashlaunch ni para funciones completas tipo RGH.")
        confirm = input("¿Estás seguro de querer usar FreeMyXe? (s/n): ").lower()
        
        if confirm != 's':
            print("\nDescarga de FreeMyXe cancelada.")
            return False
        
        os.makedirs(payload_dir, exist_ok=True)
        
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(int(downloaded * 100 / total_size), 100)
            sys.stdout.write(f"\rProgreso: {percent}% [{downloaded} / {total_size} bytes]")
            sys.stdout.flush()
        
        print(f"Guardando en: {file_path}")
        urllib.request.urlretrieve(url, file_path, reporthook=report_progress)
        
        print("\n\nDescarga completada con éxito.")
        return True
        
    except Exception as e:
        print(f"\n\nError al descargar el archivo: {e}")
        return False

def select_patch(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    print("\nPaso 3: Selecciona qué parche quieres usar:\n")
    print("  1. XeUnshackle")
    print("  2. FreeMyXe")
    print("  3. Salir")
    
    while True:
        choice = input("\nSelecciona una opción (1-3): ")
        
        if choice == "1":
            if download_xeunshackle(xploit_dir):
                return select_dashboard(xploit_dir)
            return False
        elif choice == "2":
            if download_freemyxe(xploit_dir):
                return select_dashboard(xploit_dir)
            return False
        elif choice == "3":
            print("\nSaliendo...")
            return False
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 3.")
            time.sleep(1.5)

def download_dashboard(xploit_dir, dashboard_type):
    clear_screen()
    print_ascii_art()
    
    dash_dir = os.path.join(xploit_dir, "dash")
    os.makedirs(dash_dir, exist_ok=True)
    
    urls = {
        "freestyle3": "https://archive.org/download/freestyle-3/Freestyle3.zip",
        "ranita": "https://archive.org/download/ranita-dash/RanitaDash.zip",
        "aurora": "https://archive.org/download/auroradash/auroradash.zip"
    }
    
    names = {
        "freestyle3": "Freestyle3",
        "ranita": "Ranita Xbox",
        "aurora": "Aurora"
    }
    
    url = urls[dashboard_type]
    zip_path = os.path.join(xploit_dir, f"{dashboard_type}.zip")
    macosx_folder = os.path.join(xploit_dir, "dash", "__MACOSX")
    
    print(f"\nPaso 4: Descargando y extrayendo {names[dashboard_type]}...\n")
    
    if dashboard_type == "aurora":
        print("ADVERTENCIA: Aurora es un dashboard muy simple sin tantas opciones de personalización/configuraciones.")
        confirm = input("¿Deseas continuar con Aurora? (s/n): ").lower()
        if confirm != 's':
            print("\nDescarga de Aurora cancelada.")
            return False
            
    try:
        def report_progress(block_num, block_size, total_size):
            downloaded = block_num * block_size
            percent = min(int(downloaded * 100 / total_size), 100)
            sys.stdout.write(f"\rProgreso: {percent}% [{downloaded} / {total_size} bytes]")
            sys.stdout.flush()
            
        print(f"Guardando en: {zip_path}")
        urllib.request.urlretrieve(url, zip_path, reporthook=report_progress)
        print("\n\nDescarga completada con éxito.")
        
        print(f"\nExtrayendo {dashboard_type}.zip en la carpeta dash...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(dash_dir)
        print("\nExtracción completada con éxito.")
        
        if os.path.exists(zip_path):
            os.remove(zip_path)
            print(f"Archivo {zip_path} eliminado.")
            
        if os.path.exists(macosx_folder) and os.path.isdir(macosx_folder):
            shutil.rmtree(macosx_folder)
            print(f"Carpeta {macosx_folder} eliminada.")
            
        configure_dashlaunch(xploit_dir)
        
        clear_screen()
        print_ascii_art()
        print("\nPaso 4 completado.")
        print("\n¡Listo!, ahora solo deberás copiar tus archivos a tu USB previamente formateada desde la consola.")
        time.sleep(1.5)
        return True  
        
    except Exception as e:
        print(f"\n\nError al descargar o extraer el archivo: {e}")
        return False  
        
    finally:
        input("\nPresiona Enter para continuar...")
def configure_dashlaunch(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    launch_ini_path = os.path.join(xploit_dir, "launch.ini")   
    
    if not os.path.exists(launch_ini_path):
        print("\nNo se encontró el archivo launch.ini. No se pudo configurar Dashlaunch.")
        return False  
        
    print("\nPaso 4 (continuación): Configurando Dashlaunch...")
    
    with open(launch_ini_path, 'r') as file:
        lines = file.readlines()
    
    if len(lines) >= 37:
        lines[36] = "Default = Usb:\\dash\\default.xex\n" 
    else:
        for i, line in enumerate(lines):
            if line.strip().startswith("Default = "):
                lines[i] = "Default = Usb:\\dash\\default.xex\n"
                break
    
    with open(launch_ini_path, 'w') as file:
        file.writelines(lines)
    
    print("Dashlaunch configurado correctamente.")
    return True

def select_dashboard(xploit_dir):
    clear_screen()
    print_ascii_art()
    
    print("\nPaso 4: Selecciona qué dashboard quieres usar:\n")
    print("  1. Freestyle3")
    print("  2. Ranita Xbox")
    print("  3. Aurora")
    
    while True:
        choice = input("\nSelecciona una opción (1-3): ")
        
        if choice == "1":
            return download_dashboard(xploit_dir, "freestyle3")
        elif choice == "2":
            return download_dashboard(xploit_dir, "ranita")
        elif choice == "3":
            return download_dashboard(xploit_dir, "aurora")
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 3.")
            time.sleep(1.5)

def show_info():
    print("\nInformación sobre LibreX360\n")
    print("LibreX360 es una herramienta pra generar la programación para Xbox 360.")
    
    print("\nCreado por: Isabelle M. (plvxt)")
    print("github.com/plvxt")
    
    input("\nPresiona Enter para continuar...")

def main_menu():
    while True:
        clear_screen()
        print_ascii_art()
        
        print("\nMenú Principal:")
        print("  1. Generar Programación Xbox360")
        print("  2. Información sobre LibreX360")
        print("  3. Salir")
        
        choice = input("\nSelecciona una opción (1-3): ")
        
        if choice == "1":
            clear_screen()
            print_ascii_art()
            xploit_dir, entry_point_dir = create_xploit_folders()
            if download_entry_point(entry_point_dir):
                if download_and_extract_update(xploit_dir):
                    select_patch(xploit_dir)
        elif choice == "2":
            clear_screen()
            print_ascii_art()
            show_info()
        elif choice == "3":
            clear_screen()
            print_ascii_art()
            print("\n¡Gracias por usar LibreX360!")
            print("Saliendo del programa...\n")
            time.sleep(1.5)
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 3.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta pronto!\n")
