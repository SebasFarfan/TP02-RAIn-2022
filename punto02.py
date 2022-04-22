import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


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

def eliminarSignosPuntuacion(texto):
    '''
    función que elimina los signos de puntuación de un texto.

    Args:
    texto:str

    return: str
    '''
    textoLimpio=''
    for palabra in texto:
        if palabra not in string.punctuation:
            textoLimpio+=palabra
    return textoLimpio

def eliminarStopWords(listaPalabra):
    '''
    Función que elimina los stopwords en ingles de una lista de palabras.

    Args:
    listaPalabra: list [] 

    return: list [] 
    '''
    stop_words=set(stopwords.words('english'))
    listaSinStopWords=[]
    for palabra  in listaPalabra:
        if palabra not in stop_words:
            listaSinStopWords.append(palabra)
    return listaSinStopWords

def tokenizar(texto):
    '''
    Función que Tokeniza en ingles un texto. 

    Args:
    texto: str

    return: List []
    '''
    tokens = nltk.word_tokenize(texto)
    return tokens

# ---------------------- principal -------------------------
# leer el archivo de texto
contenido = leerTexto("texto2.txt")

# eliminar signos de puntuación
textoSinSignosPuntuacion = eliminarSignosPuntuacion(contenido)

# tokenizar texto
listaPalabras = tokenizar(textoSinSignosPuntuacion)

# eliminar stopwords
listaPalabrasSinStopWords=eliminarStopWords(listaPalabras)

# proceso de Porter y Lancaster
porter = PorterStemmer()
lancaster = LancasterStemmer()

# mostramos proceso de Stemming con los algoritmos de Porter y Lancaster
print('{0:20}{1:20}{2:20}'.format('palabra','Porter','Lancaster'))
print('-'*60)
for palabra in listaPalabrasSinStopWords:
    print('{0:20}{1:20}{2:20}'.format(palabra, porter.stem(palabra), lancaster.stem(palabra)))
