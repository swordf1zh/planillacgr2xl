#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from cx_Freeze import setup, Executable
from mods import rth_helper_fns as rth

reload(sys)
sys.setdefaultencoding('utf8')

#delete the old build drive
os.system("rmdir /s /q build")

rth.print_titulo("Iniciando compilación...")

exe = Executable(
        script = 'planillacgr2xl.py',
        icon = 'icon.ico',
        targetName = 'Convertir planillas.exe'
        )

includefiles = ['icon.ico', 'icon-uninstall.ico', 'README.md', 'LICENSE']
excludes = ['_ssl', 'locale', 'calendar', 'unittest']

build_exe_options = {'include_files':includefiles, 'excludes': excludes}

setup(
    name = 'Procesador de planillas de la CGR de Panamá',
    version = '1.0.0',
    description = 'Programa para procesar los archivos de planilla de la Contraloría General de la República de Panamá y transformarlos a un libro de Excel en formato .xlsx',
    author = 'Ricardo Tribaldos Hernández < ricardo@tribaldos.org >',
    options = {'build_exe': build_exe_options},
    executables = [exe]
)

rth.print_titulo("Eliminando basura...")
os.system("del /s/q *.pyc")

rth.print_titulo("Compilación completa!")