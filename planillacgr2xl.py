#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from mods import rth_helper_cls as rthCls, Reporte
from CgrDoc_cls import *

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
    reporte = Reporte.Reporte()
    if len(sys.argv) == 1:
        raise rthCls.MyException('DragOnly')

    for index, fileDir in enumerate(sys.argv):
        if index > 0:
            readNload(fileDir)

except rthCls.MyException as e:
    if str(e) == 'DragOnly':
        msg = (
        'ADVERTENCIA:\n'
        'Para utilizar este programa debe arrastrar los archivos a procesar \n'
        'y arrojarlos sobre el ícono del programa. \n\n'
        '¡Intente nuevamente!'
        )
        rth.printToFile(msg)
    path = rthCls.Filename(sys.argv[1]).head
    reporte.save(path, 'planillas')

except NameError:
    e = sys.exc_info()[0]
    print u'¡Upps.. ocurrió un error!\n\nPor favor, intente nuevamente.', e

finally:
    print '\n\nPresione cualquier tecla para salir...'
    raw_input()