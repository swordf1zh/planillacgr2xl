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

## ¿Cómo contribuir?
Favor mantener el estilo de codificación y usar esta [convención] para los commits.

## Versiones
- v0.1.0
  - Se incluyen archivos de referencia de la CGR con la descripción de las columnas.
  - Se establecen títulos y anchos para todas las columnas a procesar.
  - Se separa el código de la aplicación en varios archivos:
    - La clase CgrDoc se coloca en un archivo propio: 'CgrDoc_cls.py'
    - Los datos de las columnas se colocan en el archivo: 'columnas.py'
  - Se reemplaza la licencia de la aplicación

- 0.0.1 - versión inicial

## Licencia
Copyright (c) 2015 Ricardo Tribaldos. Este programa es distribuido bajo licencia pública general GNU (GNU General Public License).

[convención]:https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y