#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time, rth_helper_fns as rth
import openpyxl as xls

class Reporte:

    def __init__(self):
        rth.printToFile('GENERACIÓN DE REPORTE', True)
        self.output = xls.Workbook()


    def cargar(self, hoja, data, titulos):

        msg = self.outputAddSheet(hoja, titulos, data)

        return msg


    def outputAddSheet(self, hoja, titulos, data):
        if len(data) > 0:
            # Seleccionamos la hoja activa
            sheet = self.output.get_active_sheet()

            # Si la hoja activa no es una hoja nueva, se crea una
            if sheet.title[:5] != 'Sheet':
                self.output.create_sheet()
                newSheet = self.output.get_sheet_names().pop()
                sheet = self.output.get_sheet_by_name(newSheet)

            sheet.title = hoja
            sheet.append(titulos)

            for row in data:
                sheet.append(row)

            msg = 'Se creó la hoja <%s>, se agregaron [ %d ] registros' \
                  % (hoja, len(data))
            rth.printToFile(msg)
            return msg


    def save(self, path = '', nombre = ''):
        timestamp = int(time.time())

        outputName = '%s_%d.xlsx' % ( nombre, timestamp ) if (nombre != '') \
                     else '%d.xlsx' % ( timestamp )

        if path == '':
            outputFileName = outputName
        else:
            outputFilePath = path
            if not os.path.exists(outputFilePath):
                os.makedirs(outputFilePath)
            outputFileName = os.path.normpath(os.path.join(outputFilePath, outputName))

        msg = '\nGuardando archivo: %s' % outputFileName
        rth.printToFile(msg)
        self.output.save(outputFileName)
        return 'El reporte se guardó con el nombre: %s' \
               % outputFileName