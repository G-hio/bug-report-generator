# Bug Report Generator

Una herramienta diseñada para estandarizar la comunicación de incidentes técnicos entre los equipos de QA y Desarrollo. El objetivo es eliminar la ambigüedad en los reportes y reducir el tiempo de resolución de errores (MTTR).

###  Por qué usarlo?
Un reporte mal redactado genera reprocesos. Esta herramienta asegura que cada incidencia contenga la información técnica mínima necesaria para ser procesada por un desarrollador sin necesidad de preguntas adicionales.

###  Características:
- **Estandarización:** Genera reportes basados en las mejores prácticas de la industria (IEEE 829).
- **Categorización:** Clasificación automática por Severidad y Prioridad.
- **Formato Markdown:** Listo para copiar y pegar directamente en GitHub Issues, Jira o Azure DevOps.

###  Tecnologías:
- **Lenguaje:** [Aquí pones si es Java, Python o JS]
- **Lógica:** Validación de campos obligatorios y formateo de texto dinámico.

###  Ejemplo de Salida:
> **ID:** BUG-001  
> **Título:** Fallo de validación en campo de correo electrónico  
> **Pasos:** 1. Ingresar a /registro, 2. Escribir 'test@@gmail.com', 3. Click en enviar.  
> **Resultado Obtenido:** El sistema permite el registro con doble '@'.  
> **Resultado Esperado:** El sistema debe mostrar un mensaje de error de formato.
