#!/bin/sh

#
# remove-trunk.sh - Roteiro permite correr caminhos e passar
#   todos os arquivos de trunk para o caminho raiz.
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


#
# Criar caminho .assalto para esconderijos caso não exista.
#
[ -d ~/.assalto ] || mkdir --verbose ~/.assalto

#
# Criar caminho backup para gravar pastas em .assalto
#
[ -d ~/.assalto/backup ] || mkdir --verbose ~/.assalto/backup

#
# Criar o arquivo cicle.txt caso não exista. O arquivo cicle.txt é
# uma lista com todos os componentes existentes.
#
[ -f ~/.assalto/cicle.txt ] || touch ~/.assalto/cicle.txt

#
# Criar o script para fazer a execução.
#
[ -f ~/.assalto/kids.sh ] || touch ~/.assalto/kids.sh

#
# Esse objeto grava um caminho aonde o sistema deve fazer a leitura e gravação.
#
target_dir=""

#
# Introdução.
#
echo "A ferramenta assalto, no momento permite"
echo "separar todos os conteudos de um repositorio"
echo "baseado no arch do caminho trunk."
echo

#
# Obter um caminho alvo.
#
echo "Informe o caminho alvo."
echo "    Observação:"
echo "        É permitido o uso de simbolos '~' de tiu para"
echo "        informar a interface de shell que trata-se de"
echo "        um caminho relativo. Isso significa que o script"
echo "        do assalto obtem a pasta e nome de usuarios em"
echo "        sistemas unix."
echo
read -p "Caminho (Unix): " target_dir

#
# Gravar lista de caminhos em arquivo cicle.txt
#
/bin/python3 ../src/write_target_list.py $target_dir

#
# Obtem o nome do próximo pacote.
#
/bin/python3 ../src/cat/make.py $target_dir

#
# Executar lista de ordems gerada pelo sistema.
#
/bin/sh ~/.assalto/kids.sh
