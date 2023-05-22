#
# write_target_list.py - Construção da lista de alvos.
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
#     0 ~> Caminho absoluto até caminho da pessoa.
#     1 ~> Caminho relativo, até caminho alvo.
#
args_list = sys.argv

#
# Caminho absoluto até alvo.
#
abs_path = os.path.expanduser(args_list[1])

#
# Correr a arvore.
#
for pos in listdir(abs_path):
    print("Gravando nome do caminho {0} em ~/.assalto/cicle.txt\n".format(pos))

    #
    # Gravando no final do arquivo.
    #
    f = open(os.path.expanduser("~/.assalto/cicle.txt"), "a")
    f.write("{0}\n".format(pos))
    f.close()
