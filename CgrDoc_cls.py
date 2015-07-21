#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from mods import rth_helper_fns as rth, rth_helper_cls as rthCls
from columnas import *

# encoding=utf8
reload(sys)
sys.setdefaultencoding('utf8')

class CgrDoc:

    def __init__(self, file):
        self.fileData = rthCls.Filename(file)
        rth.printToFile('Procesando archivo de la CGR: %s' \
                        % self.fileData.filext, True)
        self.data = ()
        self.rawData = self.file2list(file)
        self.tipo = self.getTipo()
        self.procesarData()


    def file2list(self, path):
        fileData = open(path, 'r')

        fileList = ()

        for line in fileData:
            fileList += (line, )

        fileData.close()

        return fileList


    def getTipo(self):
        fileData = self.rawData
        maxLen = 0

        for line in fileData:
            maxLen = len(line) if (len(line) > maxLen) else maxLen

        tipo = 'salarios' if (maxLen > 200) else 'descuentos'

        return tipo


    def getCedula(self, cedula):
        cedulaParts = (2,2,4,5)

        cursorIni = 0
        cedulaPre = []

        for part in cedulaParts:
            cursorEnd = cursorIni + part

            formattedPart = cedula[cursorIni:cursorEnd] \
                            .lstrip('0') \
                            .strip(' ')
            cedulaPre.append(formattedPart)

            cursorIni = cursorEnd

        return '%s-%s-%s' % (cedulaPre[0] + cedulaPre[1], \
                             cedulaPre[2], cedulaPre[3])


    def setColumnas(self):
        if self.tipo == 'salarios':
            self.columnas = colSalarios

        elif self.tipo == 'descuentos':
            self.columnas =  colDesctos

    def getColKeys(self):
        colKeys = ()

        for columna, largo in self.columnas:
            colKeys += (columna,)

        return colKeys

    def procesarData(self):
        self.setColumnas()

        for lineaRaw in self.rawData:
            cursorIni = 0
            linea = ()

            for columna, largo in self.columnas:

                cursorEnd = cursorIni + largo

                data = lineaRaw[cursorIni:cursorEnd].strip(' ')

                linea = linea + (self.getCedula(data),) \
                        if (columna == 'Cédula')  \
                        else linea + (data,)

                cursorIni = cursorEnd

            self.data += (linea,)