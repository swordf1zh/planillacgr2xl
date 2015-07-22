#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from mods import rth_helper_cls as rthCls, rth_helper_fns as rth, Reporte
from CgrDoc_cls import *

# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')

def readNload(fileDir):
    fileInfo = rthCls.Filename(fileDir)

    if fileInfo.isDir:
        for file in os.listdir(fileDir):
            filename = os.path.abspath(os.path.join(fileDir, file))
            readNload(filename)

    else:
        if fileInfo.extension == '.txt':
            cgrDoc = CgrDoc(fileDir)
            reporte.cargar(cgrDoc.tipo, cgrDoc.data, cgrDoc.getColKeys())


try:
    titl = 'PROCESADOR DE PLANILLAS DE LA CONTRALORIA GENERAL DE LA REPUBLICA'
    ver = 'v0.1.0'
    rth.printTxtHeader(titl, ver)

    reporte = Reporte.Reporte()

    for index, fileDir in enumerate(sys.argv):
        if index > 0:
            readNload(fileDir)

    path = rthCls.Filename(sys.argv[1]).head
    reporte.save(path, 'planillas')

    print '\n\nPROCESO FINALIZADO CON EXITO!'

except NameError:
    e = sys.exc_info()[0]
    print u'¡Upps.. ocurrió un error!\n\nPor favor, intente nuevamente.', e

except IndexError:
    print (u'\n\n\nPara usar este programa simplemente arrastre los archivos \n' +
           u'a procesar hasta el ícono del programa en el escritorio.\n')

finally:
    print '\n\nPresione cualquier tecla para salir...'
    raw_input()