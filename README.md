# Procesador de planillas de la Contraloría General de la República de Panamá

> Programa para procesar los archivos de planilla y transformarlos a un libro de Excel en formato '.xlsx'

## Pre-requisitos
Para compilar la aplicación se requieren las siguientes librerías:
* cx_Freeze
```shell
pip install cx_Freeze
```
* openpyxl
```shell
pip install openpyxl
```

## ¿Cómo empezar?
Para generar un archivo ejecutable:
```shell
python setup.py build
```

Para usar el programa, simplemente hay que arrastrar las carpetas o archivos de planillas y/o descuentos hasta el ejecutable.

## Pendiente
    [ ] Conseguir el título y ancho de las columnas para cada hoja.

## ¿Cómo contribuir?
Favor mantener el estilo de codificación y usar esta [convención] para los commits.

## Versiones
v0.0.1 - versión inicial

## Licencia
Copyright (c) 2015 Ricardo Tribaldos. Licenciado bajo licencia MIT.

[convención]:https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y