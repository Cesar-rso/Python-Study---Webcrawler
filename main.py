import requests                              #Biblioteca de conexão com url para lidar com html
from bs4 import BeautifulSoup                #Biblioteca para varredura de itens em html
import operator

#Função principal que cria lista de palavras
def start(url, tag='a', arg_='class', argvalue='post-title'):
    word_list = []                                           #Variavel para armazenar a lista de palavras
    source_code = requests.get(url).text                     #Variavel onde se armazena o codigo html da url
    soup = BeautifulSoup(source_code, 'html.parser')         #Convertendo o codigo html para um objeto BeautifulSoup

    for post_text in soup.findAll(tag, {arg_: argvalue}):       #Procurando no 'objeto' html o texto de acordo com os parametros passados (qual tag, id da tag que quer procurar, etc)
        content = post_text.string                           #Copiando somente o texto e deixando de fora headers e outros códigos html

        words = str(content).lower().split()                 #Deixando tudo em letra minuscula e separando palavra por palavra, em vez de ter um unico bloco de texto
        for each_word in words:
            word_list.append(each_word)                      #Salvando cada palavra em um item de uma variavel lista
    clean_up_list(word_list)


#Função para remover caracteres especiais
def clean_up_list(word_list):
    clean_word_list = []                                    #Variavel lista para as palavras sem caracteres especiais
    for word in word_list:
        symbols = "!@#$%^&*()_+{}|:<>?,./;'[]\=-\""         #Variavel com os caracteres especiais que serão verificados
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")             #Para cada caracter especial na variavel symbols será verificado se contem o mesmo na palavra, e apagado se tiver
        if len(word) > 0:
            clean_word_list.append(word)                    #Caso a variavel com a palavra não tenha ficado completamente vazia, é adicionada a lista
    create_dictionary(clean_word_list)


#Função para criar dicionário das palavras, organizando por numero de vezes repetidas
def create_dictionary(clean_word_list):
    word_count = {}                                         #Variavel dicionario para a lista de palavras (dicionarios tem palavra chave e valor para cada item, em vez de somente valor)
    for word in clean_word_list:
        if word in word_count:                              #Para cada palavra nova é verificado se já existe no dicionario como palavra chave
            word_count[word] += 1                           #Em caso positivo, apenas adicionar 1 ao valor, que esta funcionando como contador
        else:
            word_count[word] = 1                            #Se não, a palavra é adicionada, com o valor inicial 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):  #Exibe na tela a lista de palavras, ordenada da menos usada para a mais usada
        print(key, value)

if __name__ == '__main__':
    url = input('Informe o site para o webcrawler: ')
    tag = input('Informe a tag para o webcrawler: ')
    argid = input('Informe um parametro da tag para o webcrawler: ')
    argvalue = input('Informe o valor do parametro para o webcrawler: ')

    start(url, tag, argid, argvalue)

