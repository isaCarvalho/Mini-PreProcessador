# Tira todos os espaços, tabulações, quebra de linhas e comentarios

import re

arq = open("novoArquivo.c", "r")
stri = arq.read()


def regexCharEsp(stri):
	# Expressao regular que tira comentarios de linha
	stri = re.sub(r'\/\/(.*)', "", stri)

	# Expressao regular que tira todos os espacos, quebras de linha e tabulacoes
	stri  = re.sub(r'\s|\n|\t', " ", stri)

	# Expressao regular que tira comentarios de bloco
	stri = re.sub(r'\/\*(.*)\*\/', "", stri)

	# Expressao regular que tira os espacos duplicados
	stri = re.sub(r'\s\s*', " ", stri)

	# Expressao regular que tira espacos desnecessarios
	stri = re.sub(r'\s*\;\s*', ";", stri)
	stri = re.sub(r'\s*\(\s*', "(", stri)
	stri = re.sub(r'\s*\)\s*', ")", stri)
	stri = re.sub(r'\s*\{\s*', "{", stri)
	stri = re.sub(r'\s*\}\s*', "}", stri)
	stri = re.sub(r'\s*\,\s*', ",", stri)
	stri = re.sub(r'\s*\=\s*', "=", stri)

	return stri

strFinal = regexCharEsp(stri)

# Escreve a string modificada no arquivo final pre processado
arqFinal = open("arquivoFinal.c", "w")
arqFinal.write(strFinal)
arqFinal.close()