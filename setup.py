#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

exe = Executable(
        script = 'planillacgr2xl.py',
        icon = 'icon.ico',
        targetName = 'Convertir planillas.exe'
        )

includefiles = ['icon.ico']
excludes = ['_ssl', 'locale', 'calendar', 'unittest']

build_exe_options = {'include_files':includefiles, 'excludes': excludes}

setup(
    name = 'Procesador de planillas de la CGR de Panamá',
    version = '0.1',
    description = 'Programa para procesar los archivos de planilla de la Contraloría General de la República de Panamá y transformarlos a un libro de Excel en formato .xlsx',
    author = 'Ricardo Tribaldos Hernández < ricardo@tribaldos.org >',
    options = {'build_exe': build_exe_options},
    executables = [exe]
)