# FlowGo-PDF-Handler

Automatizaciones simples con archivos PDF (nivel junior-friendly).

## Tareas disponibles
- `merge`: unir varios PDF en uno solo  
- `extract`: extraer texto de un PDF a un archivo `.txt`

## Ejemplos de uso
```bash
python main.py --task merge --input examples/archivo1.pdf,examples/archivo2.pdf --output examples/unido.pdf
python main.py --task extract --input examples/unido.pdf --output examples/texto.txt


## Requisitos

Python 3.10+
Instalar:

pip install pypdf

Estructura mínima
FlowGo-PDF-Handler/
├─ .gitignore
├─ README.md
└─ main.py