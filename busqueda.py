import webbrowser
import argparse
import urllib.parse
import sys

parser = argparse.ArgumentParser(description='Buscador en múltiples buscadores')
parser.add_argument('-b', action='store', dest='busqueda', default=False)
parser.add_argument('-p', action='store_true', default=False, dest='personas', help='Busca en los buscadores de personas')
parser.add_argument('-t', action='store_true', default=False, dest='telefonos', help='Busca en buscadores para teléfonos')
parser.add_argument('-g', action='store_true', default=False, dest='general', help='Busca en buscadores generales')
parser.add_argument('-d', action='store_true', default=False, dest='dispositivos', help='Busca en buscadores de dispositivos')

def getBuscadoresPersonas():
    return open('buscadores-personas.txt','r').readlines()
def getBuscadoresTelefonos():
    return open('buscadores-telefonos.txt','r').readlines()
def getBuscadoresGeneral():
    return open('buscadores-generales.txt','r').readlines()
def getBuscadoresDispositivos():
    return open('buscadores-dispositivos.txt','r').readlines()


salir = True
if len(sys.argv) > 1:
    argumentos = parser.parse_args()
    busqueda = urllib.parse.quote(argumentos.busqueda)

    if(argumentos.personas == True):
        salir = False
        for buscador in getBuscadoresPersonas():
            webbrowser.open(buscador.replace('{{query}}', busqueda))
            print(buscador.replace('{{query}}', busqueda))

    if(argumentos.telefonos == True):
        salir = False
        for buscador in getBuscadoresTelefonos():
            webbrowser.open(buscador.replace('{{query}}', busqueda))
            print(buscador.replace('{{query}}', busqueda))

    if(argumentos.general == True):
        salir = False
        for buscador in getBuscadoresGeneral():
            webbrowser.open(buscador.replace('{{query}}', busqueda))
            print(buscador.replace('{{query}}', busqueda))

    if(argumentos.dispositivos == True):
        salir = False
        for buscador in getBuscadoresDispositivos():
            webbrowser.open(buscador.replace('{{query}}', busqueda))
            print(buscador.replace('{{query}}', busqueda))

if salir == True:
    print("Necesitas pasar al menos una opción: -p, -t, -g o -d e indicar la búsqueda con -b")
    print("-p Busca en los buscadores de personas")
    print("-t Busca en buscadores para teléfonos")
    print("-g Busca en buscadores generales")
    print("-d Busca en buscadores de dispositivos")
    exit()
