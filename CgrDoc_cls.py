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
        count = 0

        for line in fileData:
            fileList += (line, )
            count += 1

        fileData.close()

        rth.printToFile(' - %d líneas' % count)
        return fileList


    def getTipo(self):
        fileData = self.rawData
        maxLen = 0

        for line in fileData:
            maxLen = len(line) if (len(line) > maxLen) else maxLen

        if self.fileData.extension == '.txt':
            tipo = 'salarios' if (maxLen > 200) else 'descuentos'
        else:
            if self.fileData.name == 'Regdsc' and maxLen >= 80 and maxLen <= 82:
                tipo = 'conciliacion'
            else:
                raise IOError('No podemos procesar este archivo: %s' \
                              % self.fileData.filext)

        rth.printToFile(' - Archivo de %s' % tipo)
        return tipo


    def setColumnas(self):
        if self.tipo == 'salarios':
            self.columnas = colSalarios

        elif self.tipo == 'descuentos':
            self.columnas =  colDesctos

        elif self.tipo == 'conciliacion':
            self.columnas =  colConciliacion

        else:
            raise IOError('No podemos procesar este archivo: %s' \
                          % self.fileData.filext)

    def getColKeys(self):
        colKeys = ()

        for columna, largo in self.columnas:
            if columna != 'Filler':
                colKeys += (columna,)

        return colKeys

    def getMontoConc(self, montoStr):
        decIndex = len(montoStr)-2
        dollar = montoStr[:decIndex]
        cents = montoStr[decIndex:]

        return float(dollar + '.' + cents)

    def procesarData(self):
        self.setColumnas()

        for lineaRaw in self.rawData:
            cursorIni = 0
            linea = ()

            for columna, largo in self.columnas:
                cursorEnd = cursorIni + largo
                data = lineaRaw[cursorIni:cursorEnd].strip(' ')

                if columna != 'Filler':
                    if self.tipo == 'conciliacion' and columna == 'Monto':
                        linea += (self.getMontoConc(data),)
                    else:
                        linea += (data,)

                cursorIni = cursorEnd

            self.data += (linea,)