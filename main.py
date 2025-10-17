"""
FlowGo-PDF-Handler
Versión mínima (3 archivos)
"""

import sys
import os
from pypdf import PdfWriter, PdfReader


def print_help():
    print("Uso:")
    print("  python main.py --task merge --input <pdf1,pdf2,...> --output <pdf_salida>")
    print("  python main.py --task extract --input <pdf_entrada> --output <txt_salida>")
    print("")
    print("Ejemplos:")
    print("  python main.py --task merge --input examples/a.pdf,examples/b.pdf --output examples/unido.pdf")
    print("  python main.py --task extract --input examples/unido.pdf --output examples/texto.txt")


def read_args():
    args = {"--task": None, "--input": None, "--output": None}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] in args and i + 1 < len(sys.argv):
            args[sys.argv[i]] = sys.argv[i + 1]
            i += 2
        else:
            i += 1
    return args


def task_merge(input_paths, output_path):
    # Validaciones simples
    if not input_paths:
        print("No se proporcionaron PDFs de entrada."); return
    writer = PdfWriter()

    for path in input_paths:
        if not os.path.exists(path):
            print("No se encontró:", path); return
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)

    # Crear carpeta destino si hace falta
    d = os.path.dirname(output_path)
    if d:
        os.makedirs(d, exist_ok=True)

    with open(output_path, "wb") as f:
        writer.write(f)
    print("PDF combinado creado:", output_path)


def task_extract(input_path, output_txt):
    if not os.path.exists(input_path):
        print("No se encontró:", input_path); return

    reader = PdfReader(input_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    # Crear carpeta destino si hace falta
    d = os.path.dirname(output_txt)
    if d:
        os.makedirs(d, exist_ok=True)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    print("Texto extraído en:", output_txt)


def main():
    args = read_args()
    if args["--task"] == "merge":
        if args["--input"] and args["--output"]:
            archivos = [x.strip() for x in args["--input"].split(",")]
            task_merge(archivos, args["--output"])
        else:
            print_help()
    elif args["--task"] == "extract":
        if args["--input"] and args["--output"]:
            task_extract(args["--input"], args["--output"])
        else:
            print_help()
    else:
        print_help()


if __name__ == "__main__":
    main()
