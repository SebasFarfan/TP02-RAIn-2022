import string
import nltk
from nltk.util import ngrams


def leerTexto(archivoTexto):
    ''' función que obtiene el contenido de un archivo txt en una variable de string.

        Args: 
        archivo de texto: archivo.txt

        return: str
      '''
    texto = open(archivoTexto, 'r')
    datos = texto.read()
    texto.close()
    return datos


def obtenerParrafoTexto(texto):
    '''
    Función que obtiene el primer parrafo de un texto.

    Args:
    texto: str texto al que se le va a extraer el parrafo.

    Return: str el primer parrafo.
    '''
    i = 0
    parrafo = ''
    for i in range(0, len(texto)):
        parrafo += texto[i]
        if texto[i] in '.':
            if texto[i+1] in '\n':
                break
    return parrafo


def eliminarSignosPuntuacion(texto):
    '''
    función que elimina los signos de puntuación de un texto.

    Args:
    texto:str

    return: str
    '''
    textoLimpio = ''
    for palabra in texto:
        if palabra not in string.punctuation:
            textoLimpio += palabra
    return textoLimpio


def extraer_ngrams(texto, num):
    '''
    Función que extrae n-grams de un texto.

    Args:
    texto: str 
    num: int numero que especifica la cantidad de gramas

    Return: list [] 
    '''
    # tokenizamos
    tokens = nltk.word_tokenize(texto, 'spanish')
    n_gram = ngrams(tokens, num)
    return [' '.join(grams) for grams in n_gram]


# ---------------------------- principal ------------------------
# leer el archivo de texto
contenido = leerTexto("texto1.txt")

# eliminar signos de puntuación
textoSinSignosPuntuacion = eliminarSignosPuntuacion(contenido)

# mostrar 2-grams
# grams=extraer_ngrams(textoSinSignosPuntuacion, 2)
# print('2-grams','-'*20)
# for gram in grams:
#     print(gram)

# mostrar 3-grams
grams=extraer_ngrams(textoSinSignosPuntuacion, 3)
print('3-grams','-'*20)
for gram in grams:
    print(gram)
