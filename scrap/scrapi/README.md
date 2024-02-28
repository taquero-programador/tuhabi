## Probar API

### Instalar Python y Jupyter Notebook (opcional)
[Descargar Python](https://www.python.org/downloads/).

Instalar Notebook con Python:
```bash
python -m pip install notebook
```

Clonar el repositorio:
```bash
https://github.com/taquero-programador/tuhabi.git
```

Entrar al directorio y ejecutar:
```bash
jupyter notebook --no-browser --autoreload
```

En el navegador escribir `localhost:8888`, abrir el archivo `simple_api.ipynb`:
- Ejecutar la primera celda con `Ctrl` + `Enter` para instalar módulos.
- Dentro del directorio `scrapi` abrir una terminal y ejecutar `uvicorn main:app`

La próximas celdas del Notebook se pueden ejecutar con `Shift` + `Enter`: ejecuta la celda
actual y se mueve a la siguiente.

