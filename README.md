# 📡 Network Availability Monitor

## Descripción
Herramienta de automatización desarrollada en **Python** para el monitoreo de disponibilidad de servidores y dispositivos de red.
Diseñada para agilizar el diagnóstico de conectividad en entornos corporativos (LAN/WAN), permitiendo a los administradores visualizar rápidamente el estado de múltiples activos.

## 🚀 Funcionalidades
* **Detección automática de SO:** Ajusta la sintaxis de comandos ICMP (Ping) según si el entorno es Windows o Linux/Unix.
* **Lectura externa:** Ingesta dinámica de hosts desde un archivo de configuración (`servidores.txt`), evitando el hardcoding.
* **Reporte Visual:** Interfaz de consola limpia con indicadores de estado (ONLINE/OFFLINE) y timestamp.
* **Manejo de Errores:** Control de excepciones para archivos inexistentes o interrupciones de ejecución.

## 🛠️ Tecnologías
* **Lenguaje:** Python 3.x
* **Librerías:** `subprocess` (Ejecución de procesos del sistema), `platform` (Identificación de entorno), `datetime`.

## 📋 Cómo usar
1.  Clonar el repositorio.
2.  Editar el archivo `servidores.txt` con las IPs o dominios a monitorear.
3.  Ejecutar el script:
    ```bash
    python monitor.py
    ```

## 👤 Autor
**Ezequiel Perezlindo**
*Técnico en Redes | Estudiante de Licenciatura en Informática*
