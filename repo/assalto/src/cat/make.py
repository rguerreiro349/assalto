#
# make.py - Lê e altera a lista.
#
# Direito Autoral (C) {{ ano(); }}  {{ nome_do_autor(); }}
#
# Este programa é um software livre: você pode redistribuí-lo
# e/ou modificá-lo sob os termos da Licença Pública do Cavalo
# publicada pela Fundação do Software Brasileiro, seja a versão
# 3 da licença ou (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que seja útil,
# mas SEM QUALQUER GARANTIA; mesmo sem a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO PARA UM FIM ESPECÍFICO. Consulte
# a Licença Pública e Geral do Cavalo para obter mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública e Geral do
# Cavalo junto com este programa. Se não, consulte:
#   <http://localhost/licenses>.
#

import sys

import os
import os.path

from os import listdir
from os.path import isfile
from os.path import join


#
# Argumentos:
#     0 ~> Alvo.
#
targetdir = os.path.expanduser(sys.argv[1])

#
# Lê e remove uma linha.
#
def read_and_dropline():
    #
    # Caminho absoluto até arquivo cicle.txt
    #
    absfile = os.path.expanduser("~/.assalto/cicle.txt")

    #
    # A lista de linhas com todos os caminhos do alvo.
    #
    vector = []

    #
    # Transformar arquivo em vetor.
    #
    with open(absfile, "r") as fp:
        for line in fp:
            vector.append(line)

    #
    # Caso o arquivo esteja vazio, devolver um null.
    #
    if len(vector) == 0:
        return ""

    #
    # Remover linhas vazias de vetor.
    #
    vector = list(filter(None, vector))
    vector = list(filter(len, vector))

    #
    # Obter o texto da primeira linha em python.
    #
    bytes = vector[0]

    #
    # Excluir primeira linha do script.
    #
    vector = vector[1:]

    #
    # Gerar uma saída.
    #
    buff = ""
    for output in vector:
        #
        # Grava a linha desse ciclo no final do stream.
        #
        if buff == "":
            buff = "{0}".format(
                output.replace("\n", "")
            )
        else:
            buff = "{0}\n{1}".format(
                buff,
                output.replace("\n", "")
            )

    #
    # Gravar o buffer no arquivo de ciclos.
    #
    handle = open(absfile, "w")
    handle.write(buff)
    handle.close()

    #
    # Devolver o nome do caminho.
    #
    return bytes


kids = os.path.expanduser("~/.assalto/kids.sh")

#
# Gravando o cabeçalho.
#
h = open(kids, "a")
h.write("#!/bin/sh\n\n")
h.write("#\n")
h.write("# Gerado por: Assalto v2.1\n")
h.write("#\n")
h.write("# Direito Autoral (C) ")
h.write("{")
h.write("{")
h.write(" ano(); ")
h.write("}")
h.write("}  ")
h.write("{")
h.write("{")
h.write(" nome_do_autor(); ")
h.write("}")
h.write("}")
h.write("\n")
h.write("#\n")
h.write("# Este programa é um software livre: você pode redistribuí-lo\n")
h.write("# e/ou modificá-lo sob os termos da Licença Pública do Cavalo\n")
h.write("# publicada pela Fundação do Software Brasileiro, seja a versão\n")
h.write("# 3 da licença ou (a seu critério) qualquer versão posterior.\n")
h.write("#\n")
h.write("# Este programa é distribuído na esperança de que seja útil,\n")
h.write("# mas SEM QUALQUER GARANTIA; mesmo sem a garantia implícita de\n")
h.write("# COMERCIABILIDADE ou ADEQUAÇÃO PARA UM FIM ESPECÍFICO. Consulte\n")
h.write("# a Licença Pública e Geral do Cavalo para obter mais detalhes.\n")
h.write("#\n")
h.write("# Você deve ter recebido uma cópia da Licença Pública e Geral do\n")
h.write("# Cavalo junto com este programa. Se não, consulte:\n")
h.write("#   <http://localhost/licenses>.\n")
h.write("#\n\n")
h.close()

#
# Obter o padrão do shell.
#
def get_pattern(pkgname, target_dir):
    return "[ -d ~/.assalto/backup/{0} ] || mkdir --verbose ~/.assalto/backup/{1} && cp -vr {2}/{3}/trunk/* ~/.assalto/backup/{4}\n".format(
        pkgname,
        pkgname,
        target_dir,
        pkgname,
        pkgname
    )

o = read_and_dropline()
o = o.replace(" ",  "")
o = o.replace("\n", "")
o = o.replace("\t", "")
o = o.replace("\r", "")

h = open(kids, "a")
con = 0

while True:
    if o != None and len(o.replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "")) > 0:
        h.write(get_pattern(o, targetdir))

    #
    # Maximo de 10 voltas em vão.
    #
    if con > 10:
        break

    if o == None:
        con = con + 1

    if o == "":
        con = con + 1

    if o == "\n":
        con = con + 1

    #
    # Resultado para proxima volta.
    #
    o = read_and_dropline()
    o = o.replace(" ",  "")
    o = o.replace("\n", "")
    o = o.replace("\t", "")
    o = o.replace("\r", "")

h.close()
