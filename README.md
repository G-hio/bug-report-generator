#  Bug Report Generator & QA Suite

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![QA](https://img.shields.io/badge/QA-Testing-green?logo=checkmarx&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Professional_Grade-blue)]()

Este proyecto es una herramienta de automatización para **Analistas de QA e Ingenieros de Software**. Permite transformar reportes técnicos en formato JSON a archivos CSV estructurados y priorizados, facilitando el triaje de errores en ciclos de desarrollo ágil.

##  Características Principales

* **Priorización Automática:** Ordena incidentes por severidad (Critical, High, Medium, Low) mediante lógica de pesos.
* **Logging Profesional:** Implementa la librería `logging` para trazabilidad de errores en un archivo `execution.log`.
* **Unit Testing:** Incluye una suite de pruebas con `unittest` para garantizar la integridad de la lógica de negocio.
* **Exportación Estándar:** Genera archivos CSV compatibles con Microsoft Excel, Google Sheets y Jira.

##  Tecnologías Utilizadas

* **Python 3.14:** Lenguaje principal para la lógica de automatización.
* **JSON/CSV:** Formatos de intercambio de datos estándar.
* **Unittest:** Framework para pruebas unitarias.

##  Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/G-hio/bug-report-generator.git](https://github.com/G-hio/bug-report-generator.git)
    cd bug-report-generator
    ```

2.  **Ejecutar la herramienta:**
    Pasa tu archivo JSON como argumento:
    ```bash
    python generate_report.py sample_results.json
    ```

3.  **Ejecutar las pruebas unitarias:**
    Para validar que el sistema funciona correctamente:
    ```bash
    python test_report.py
    ```

##  Ejemplo de Estructura JSON
El sistema espera una estructura profesional como la siguiente:
```json
[
  {
    "id": "BUG-001",
    "title": "Fallo de autenticación",
    "severity": "critical",
    "status": "open"
  }
]e formato.
