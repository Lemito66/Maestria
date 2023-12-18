# Indicaciones

El siguiente repositorio se encuentra bajo un entorno virtual. Una vez descargado deberas instalar virtual venv



```
pip install virtualenv
```

- Luego crear tu carpeta venv, usar siempre por defecto el nombre de la carpeta venv

```
python -m venv <nombre_carpeta> 
```
- Verificar siempre que en tu terminal estes utilizando el entorno virtual. Puedes asegurarte de aquello presionando las teclas control + shift + p y seleccionar el interprete de venv
- Descargar todas las librerias del archivo requirements.txt

```
pip install -r requirements.txt
```

- Si utilizas más librerias, no olvides modificar nuestro archivo requierements.txt con el siguiente comando
```
python -m pip freeze > requirements.txt
```

- Si no se activa venv en tu terminal. Utiliza un cmd y escribe el siguiente comando

```
.\<nombre_carpeta>\Scripts\activate
```