# ...existing code...
# Programa demostrativo: Entrada y salida de datos (consola, archivos, JSON, CSV, binario)
import argparse
import csv
import json
import logging
from pathlib import Path
from typing import Any

ROOT = Path.cwd() / "io_demo_data"
ROOT.mkdir(parents=True, exist_ok=True)
TEXT_FILE = ROOT / "ejemplo.txt"
JSON_FILE = ROOT / "datos.json"
CSV_FILE = ROOT / "tabla.csv"
BIN_FILE = ROOT / "datos.bin"
LOG_FILE = ROOT / "io_demo.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
)

def input_int(prompt: str) -> int:
    while True:
        try:
            s = input(prompt).strip()
            val = int(s)
            logging.debug("input_int: %s -> %d", s, val)
            return val
        except ValueError:
            print("Entrada no válida. Introduce un entero.")
            logging.warning("Entrada no válida para int: %s", s)

def input_float(prompt: str) -> float:
    while True:
        try:
            s = input(prompt).strip()
            val = float(s)
            logging.debug("input_float: %s -> %f", s, val)
            return val
        except ValueError:
            print("Entrada no válida. Introduce un número (float).")
            logging.warning("Entrada no válida para float: %s", s)

def input_str(prompt: str, allow_empty: bool = False) -> str:
    while True:
        s = input(prompt)
        if s or allow_empty:
            logging.debug("input_str: %s", s)
            return s
        print("La cadena no puede estar vacía.")

def console_io_demo():
    print("=== DEMO: Entrada por consola ===")
    nombre = input_str("Nombre: ")
    edad = input_int("Edad: ")
    altura = input_float("Altura en metros (ej. 1.75): ")
    print(f"Hola {nombre}, tienes {edad} años y mides {altura:.2f} m.")
    logging.info("console_io_demo: %s, %d, %f", nombre, edad, altura)
    return {"nombre": nombre, "edad": edad, "altura": altura}

def text_file_demo(data: dict):
    print("Guardando datos en archivo de texto:", TEXT_FILE)
    try:
        with open(TEXT_FILE, "w", encoding="utf-8") as f:
            f.write(f"Nombre: {data['nombre']}\n")
            f.write(f"Edad: {data['edad']}\n")
            f.write(f"Altura: {data['altura']}\n")
        logging.info("text_file_demo: guardado en %s", TEXT_FILE)
        print("Guardado correctamente.")
    except Exception as e:
        logging.exception("Error guardando texto: %s", e)
        print("Error al guardar el archivo de texto:", e)

def json_demo(data: dict):
    print("Guardando y leyendo JSON:", JSON_FILE)
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
        logging.info("json_demo: guardado y leido %s", JSON_FILE)
        print("Contenido JSON leído:", loaded)
    except Exception as e:
        logging.exception("Error JSON: %s", e)
        print("Error trabajando con JSON:", e)

def csv_demo(data: dict):
    print("Guardando y leyendo CSV:", CSV_FILE)
    headers = ["nombre", "edad", "altura"]
    try:
        # Escribir
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerow(data)
        # Leer
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        logging.info("csv_demo: escrito y leido %s", CSV_FILE)
        print("Filas leídas del CSV:", rows)
    except Exception as e:
        logging.exception("Error CSV: %s", e)
        print("Error trabajando con CSV:", e)

def binary_demo(data: dict):
    print("Guardando datos binarios (pickle-like simple):", BIN_FILE)
    try:
        # Serialización simple: JSON bytes (ejemplo de binario)
        b = json.dumps(data, ensure_ascii=False).encode("utf-8")
        with open(BIN_FILE, "wb") as f:
            f.write(b)
        with open(BIN_FILE, "rb") as f:
            loaded = json.loads(f.read().decode("utf-8"))
        logging.info("binary_demo: escrito y leido %s", BIN_FILE)
        print("Contenido binario leído:", loaded)
    except Exception as e:
        logging.exception("Error binario: %s", e)
        print("Error trabajando con datos binarios:", e)

def interactive_menu():
    data = None
    while True:
        print("\nMENU:")
        print(" 1) Entrada por consola")
        print(" 2) Guardar en texto")
        print(" 3) Guardar/Leer JSON")
        print(" 4) Guardar/Leer CSV")
        print(" 5) Guardar/Leer binario")
        print(" 6) Mostrar archivos en carpeta de datos")
        print(" 0) Salir")
        opt = input_str("Elige una opción: ")
        if opt == "1":
            data = console_io_demo()
        elif opt == "2":
            if data:
                text_file_demo(data)
            else:
                print("Primero realiza la entrada por consola (opción 1).")
        elif opt == "3":
            if data:
                json_demo(data)
            else:
                print("Primero realiza la entrada por consola (opción 1).")
        elif opt == "4":
            if data:
                csv_demo(data)
            else:
                print("Primero realiza la entrada por consola (opción 1).")
        elif opt == "5":
            if data:
                binary_demo(data)
            else:
                print("Primero realiza la entrada por consola (opción 1).")
        elif opt == "6":
            files = list(ROOT.iterdir())
            print("Archivos en", ROOT, ":")
            for p in files:
                print(" -", p.name)
        elif opt == "0":
            print("Saliendo.")
            break
        else:
            print("Opción no válida.")

def demo_non_interactive():
    # Datos de ejemplo para ejecución no interactiva (útil para pruebas o CI)
    ejemplo = {"nombre": "Ana", "edad": 30, "altura": 1.68}
    text_file_demo(ejemplo   )
    json_demo(ejemplo)
    csv_demo(ejemplo)
    binary_demo(ejemplo)
    print("Ejecución no interactiva completada. Revisa", ROOT)
    logging.info("demo_non_interactive: completado")

def parse_args() -> Any:
    p = argparse.ArgumentParser(description="Demo I/O: consola, archivos, JSON, CSV, binario")
    p.add_argument("--non-interactive", action="store_true", help="Ejecutar demo completo sin interacción")
    return p.parse_args()

def main():
    args = parse_args()
    print("Inicio del demo de entrada y salida de datos.")
    if args.non_interactive:
        demo_non_interactive()
    else:
        interactive_menu()
    print("Fin del programa. Logs:", LOG_FILE)

if __name__ == "__main__":
    main()
# ...existing code...
