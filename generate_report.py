import json
import csv
import sys
import logging
from datetime import datetime
from typing import List, Dict, Any

# Configuracion de Logging: Guarda un rastro de la ejecucion en 'execution.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("execution.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

PRIORITY_MAP = {'critical': 1, 'high': 2, 'medium': 3, 'low': 4}

def load_results(path: str) -> List[Dict[str, Any]]:
    """Carga datos JSON con manejo de errores profesional."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error critico al cargar el archivo: {e}")
        sys.exit(1)

def get_priority_weight(item: Dict[str, Any]) -> int:
    """Determina el peso de prioridad. Clave para las Pruebas Unitarias."""
    severity = str(item.get('severity', 'low')).lower()
    return PRIORITY_MAP.get(severity, 4)

def generate_csv_report(results: List[Dict[str, Any]], output_file: str = 'bugs_report.csv'):
    """Genera el reporte final ordenado por relevancia."""
    try:
        sorted_results = sorted(results, key=get_priority_weight)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'TITULO', 'SEVERIDAD', 'ESTADO', 'FECHA'])
            
            for bug in sorted_results:
                writer.writerow([
                    bug.get('id', 'N/A'),
                    bug.get('title', 'Sin titulo'),
                    bug.get('severity', 'medium').upper(),
                    bug.get('status', 'open'),
                    bug.get('created', datetime.now().strftime('%Y-%m-%d'))
                ])
        logging.info(f"Reporte generado exitosamente: {output_file}")
    except IOError as e:
        logging.error(f"Fallo de escritura en disco: {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.warning("Ejecucion sin argumentos. Se requiere un archivo JSON.")
        print('Uso: python generate_report.py sample_results.json')
    else:
        data = load_results(sys.argv[1])
        generate_csv_report(data)