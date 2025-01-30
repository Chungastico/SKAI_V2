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
│   ├── start.py // NO TOCAR
│   └── Modelo/
│       ├── keras_Model.h5
│       └── labels.txt
```

## Uso
Para ejecutar el sistema, utiliza:

```bash
python Codigo/start.py
```

## Cómo funciona el proyecto
Dentro de la carpeta `teachable` se encuentra el modelo de IA.
Puedes acceder a Teachable Machine a través del siguiente enlace:

[Teachable Machine](https://teachablemachine.withgoogle.com/train)

Entre otros archivos, puedes modificar el contenido de `Codigo/Modelo/` donde se encuentra la IA entrenada. **No cambies el archivo `labels.txt`, solo el `keras_model.h5`.**

## Uso de Git: Cómo hacer commits
Para contribuir al proyecto y mantener un historial limpio, sigue estos pasos para hacer commits correctamente:

### 1. Agregar cambios al área de preparación (staging)
Si has modificado archivos y deseas agregarlos al commit, usa:
```bash
git add .
```
Para agregar un archivo específico, usa:
```bash
git add nombre_del_archivo.ext
```

### 2. Crear un commit con un mensaje descriptivo
```bash
git commit -m "Descripción breve del cambio"
```
Ejemplo:
```bash
git commit -m "Corrige bug en la carga del modelo de IA"
```

### 3. Subir los cambios al repositorio remoto
Si es tu primera vez subiendo cambios, usa:
```bash
git push origin main
```
Si ya has subido cambios antes y quieres sincronizar con la última versión:
```bash
git pull origin main --rebase
```
Luego, vuelve a subir los cambios:
```bash
git push origin main
```

## Contribuir
Si deseas contribuir al proyecto, sigue estos pasos:

1. Realiza un **fork** del repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b nombre-de-tu-rama
   ```
3. Realiza tus modificaciones y sigue los pasos para hacer commits.
4. Sube tu rama al repositorio remoto:
   ```bash
   git push origin nombre-de-tu-rama
   ```
5. Crea un **Pull Request** en GitHub para revisión.

---
Este documento se actualizará conforme evolucione el proyecto.
