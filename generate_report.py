import json
import csv
import sys
from datetime import datetime
from typing import List, Dict, Any

# Configuracion de prioridades para el ordenamiento del reporte
PRIORITY_MAP = {
    'critical': 1,
    'high': 2,
    'medium': 3,
    'low': 4
}

def load_results(path: str) -> List[Dict[str, Any]]:
    """
    Carga los resultados desde un archivo JSON.
    Incluye validacion de existencia de archivo y formato interno.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no fue localizado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{path}' no contiene un JSON valido.")
        sys.exit(1)

def get_priority_weight(item: Dict[str, Any]) -> int:
    """
    Asigna un valor numerico a la severidad para permitir el ordenamiento.
    Por defecto asigna prioridad media (3) si el campo no existe.
    """
    severity = item.get('severity', 'medium').lower()
    return PRIORITY_MAP.get(severity, 3)

def generate_csv_report(results: List[Dict[str, Any]], output_file: str = 'bugs_report.csv'):
    """
    Procesa la lista de incidentes y genera un archivo CSV ordenado.
    """
    # Ordenamiento logico por severidad (de Critico a Bajo)
    sorted_results = sorted(results, key=get_priority_weight)

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Definicion de encabezados estandarizados
            headers = ['ID', 'TITULO', 'SEVERIDAD', 'ESTADO', 'FECHA_CREACION']
            writer.writerow(headers)
            
            for bug in sorted_results:
                writer.writerow([
                    bug.get('id', 'N/A'),
                    bug.get('title', 'Sin titulo'),
                    bug.get('severity', 'medium').upper(),
                    bug.get('status', 'open'),
                    bug.get('created', datetime.now().strftime('%Y-%m-%d'))
                ])
        
        print(f"Reporte generado exitosamente: {output_file}")
        print(f"Registros procesados: {len(sorted_results)}")
        
    except IOError as e:
        print(f"Error en la operacion de escritura de archivos: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso requerido: python generate_report.py <ruta_del_archivo.json>')
    else:
        file_input = sys.argv[1]
        data_results = load_results(file_input)
        generate_csv_report(data_results)
