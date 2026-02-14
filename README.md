## Sistema de Gestión Veterinaria
Este programa permite registrar y administrar pacientes (mascotas) mediante una interfaz de consola.

## Características

- Registro de pacientes con información completa (nombre, edad, especie, enfermedad, dueño, etc.)
- Consulta de todos los registros
- Modificación de datos existentes
- Eliminación de registros con respaldo automático
- Almacenamiento en archivos de texto

## Tecnologías

- Python 3.x
- Archivos de texto para persistencia de datos

## Instalación y Uso

```bash
git clone https://github.com/fedepolito/portal-veterinaria.git
cd portal-veterinaria
python src/main.py
```

## Estructura

```
veterinaria/
├── src/
│   └── main.py
├── data/
│   ├── registrados.txt
│   └── eliminados.txt
└── README.md
```
