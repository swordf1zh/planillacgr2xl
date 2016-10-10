#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from mods import rth_helper_cls as rthCls, Reporte
from CgrDoc_cls import *
from bigText import *

# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')

def readNload(fileDir):
    fileInfo = rthCls.Filename(fileDir)

    if fileInfo.isDir:
        ready2import = ();
        for file in os.listdir(fileDir):
            filename = os.path.abspath(os.path.join(fileDir, file))
            ready2import += (readNload(filename),)
        return ready2import

    else:
        if fileInfo.extension == '.txt' or fileInfo.name == 'Regdsc':
            cgrDoc = CgrDoc(fileDir)
            rth.printToFile(' - Lectura de archivo completa')
            return (cgrDoc,)


try:
    rth.printToFile(bigTitle)

    cgrDocs = ();

    if len(sys.argv) == 1:
        raise rthCls.MyException('DragOnly')

    for index, fileDir in enumerate(sys.argv):
        if index > 0:
            cgrDocs += (readNload(fileDir),)

    cgrDocsFlat = [element for tupl in cgrDocs for element in tupl]

    if len(cgrDocsFlat) > 0:
        rth.printToFile('Generando archivo de Excel', True)
        reporte = Reporte.Reporte()

        for cgrDoc in cgrDocsFlat:
            reporte.cargar(cgrDoc.tipo, cgrDoc.data, cgrDoc.getColKeys())

        path = rthCls.Filename(sys.argv[1]).head
        reporte.save(path, 'planillas')
        rth.printToFile('¡LISTO!')

except rthCls.MyException as e:
    if str(e) == 'DragOnly':
        msg = (
        'ADVERTENCIA:\n'
        'Para utilizar este programa debe arrastrar los archivos a procesar \n'
        'y arrojarlos sobre el ícono del programa. \n\n'
        '¡Intente nuevamente!'
        )
        rth.printToFile(msg)

except:
    msg = (
    '¡Upps.. ocurrió un error! \n\n'
    'Por favor, intente nuevamente.'
    )
    rth.printToFile(msg)

finally:
    print '\n\nPresione cualquier tecla para salir...'
    raw_input()