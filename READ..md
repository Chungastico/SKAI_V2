# Proyecto SKAI

SKAI es un sistema de clasificación de residuos basado en inteligencia artificial. Utiliza redes neuronales para identificar distintos tipos de desechos y facilitar su separación automática.

## Instalación

### 1. Clonar el repositorio
Ejecuta el siguiente comando en tu terminal para clonar el proyecto:

```bash
git clone https://github.com/Chungastico/SKAI_V2.git
```

### 2. Crear un entorno virtual
Para aislar las dependencias del proyecto, crea un entorno virtual:

```bash
python -m venv venv
```

### 3. Activar el entorno virtual
#### En Linux/Mac:
```bash
source venv/bin/activate
```

#### En Windows:
```bash
venv\Scripts\activate
```

### 4. Instalar los requisitos del proyecto

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto
```
SKAI/
├── .gitignore
├── README.md
├── requirements.txt
├── Codigo/
│   ├── start.py
│   └── Modelo/
│       ├── keras_Model.h5
│       └── labels.txt
└── docs/  # (Opcional) Documentación y ejemplos de uso
```

## Uso
Para ejecutar el sistema, utiliza:

```bash
python Codigo/start.py
```

## Contribuir
Si deseas contribuir al proyecto, puedes realizar un fork, crear una nueva rama con tus cambios y enviar un pull request.

---
Este documento se actualizará conforme evolucione el proyecto.
