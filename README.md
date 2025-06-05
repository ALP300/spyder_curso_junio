# Proyecto Análisis de Datos ATP

Este proyecto realiza un análisis de datos del ATP Tour utilizando Python y pandas.

## Requisitos

- Python 3.x
- pandas
- numpy

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Instala las dependencias:
   ```bash
   pip install pandas numpy
   ```

## Datos

Debes descargar el archivo CSV con los datos del ATP Tour (2000-2016) desde Kaggle:

[Descargar ATP_DATA.csv](https://www.kaggle.com/datasets/jordangoblet/atp-tour-20002016)

Coloca el archivo `ATP_DATA.csv` en la raíz del proyecto.

## Uso

Ejecuta el script principal para ver un resumen de los datos:

```bash
python ejercicio2.py
```

## Estructura del proyecto

- `ejercicio2.py`: Script principal de análisis.
- `.gitignore`: Ignora archivos CSV y otros archivos innecesarios.
- `README.md`: Este archivo.

## Notas

- Los archivos `.csv` están ignorados en el control de versiones por seguridad y tamaño.
- Si tienes problemas de codificación al leer el CSV, asegúrate de usar `encoding='latin1'` en pandas.

---
Autor: Leo