#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from mods import rth_helper_fns as rth, rth_helper_cls as rthCls, Reporte

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
            self.columnas = [
                ('Numero de Cheque/Recibo', 7),
                ('Nombre', 20),
                ('Apellido Paterno', 15),
                ('Apellido Materno', 15),
                ('Apellido de Casada', 15),
                ('Provincia de Cedula', 2),
                ('Iniciales de la Cedula', 2),
                ('Tomo de la Cedula', 4),
                ('Asiento de la Cedula', 5),
                ('Numero de Seguro Social', 7),
                ('Codigo de Area', 1),
                ('Codigo de Entidad', 2),
                ('Numero de Planilla', 5),
                ('Numero de Posición', 5),
                ('Estatus del Funcionario', 2),
                ('Monto de Sueldo Bruto', 10),
                ('Monto de Seguro Social', 8),
                ('Clave de Renta', 3),
                ('Monto de Impuesto sobre la Renta', 8),
                ('Monto de Seguro Educativo', 8),
                ('Monto de Descuento-1', 8),
                ('Clave de Descuento-1 ', 1),
                ('Monto de Descuento-2', 8),
                ('Clave Descuento-2 ', 1),
                ('Monto de Descuento-3', 8),
                ('Clave de Descuento-3 ', 1),
                ('Monto de Descuento-4', 8),
                ('Clave de Descuento-4 ', 1),
                ('Monto de Descuento-5', 8),
                ('Clave de Descuento-5 ', 1),
                ('Monto de Descuento-6', 8),
                ('Clave de Descuento-6 ', 1),
                ('Monto de Descuento-7', 8),
                ('Clave de Descuento-7 ', 1),
                ('Monto de Sueldo Neto', 9),
                ('Fecha de Pago', 8),
                ('Tipo de Pago', 1),
                ('Forma de Pago', 2),
                ('Codigo de Banco', 9),
                ('Tipo de Cuenta', 1),
                ('Numero de Cuenta', 20),
                ('Centro de Pago', 10),
                ('Provincia donde Labora', 2),
                ('Año de Proceso', 4),
                ('Mes de Proceso', 1),
                ('Quincena de Proceso ', 1)
            ]

        elif self.tipo == 'descuentos':
            self.columnas =  [
                ('Provincia de Cedula', 2),
                ('Iniciales de la Cedula', 2),
                ('Tomo de la Cedula', 4),
                ('Asiento de la Cedula', 5),
                ('Tipo de descuento', 1),
                ('Fecha de Aplicación', 8),
                ('Código de Aplicación', 1),
                ('Área', 1),
                ('Entidad', 2),
                ('Número de Planilla', 5),
                ('Número de Posición', 5),
                ('Estado del Empleado', 2),
                ('Clave del Descuento', 8),
                ('Subclave del Descuento', 8),
                ('Posición del Descuento', 2),
                ('Monto Inicial', 8),
                ('Valor  A Efectuar', 7),
                ('Valor Efectuado', 7),
                ('Saldo del Descuento', 7),
                ('Demandante', 40),
                ('Código del Préstamo', 1),
                ('Nombre', 20),
                ('Apellido', 15),
                ('Blanco', 1)
            ]

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
    reporte = Reporte.Reporte()

    for index, fileDir in enumerate(sys.argv):
        if index > 0:
            readNload(fileDir)

    path = rthCls.Filename(sys.argv[1]).head
    reporte.save(path, 'planillas')

except NameError:
    e = sys.exc_info()[0]
    print u'¡Upps.. ocurrió un error!\n\nPor favor, intente nuevamente.', e

finally:
    print '\n\nPresione cualquier tecla para salir...'
    raw_input()