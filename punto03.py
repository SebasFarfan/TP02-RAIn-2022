import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

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
    Función que elimina los stopwords en español de una lista de palabras.

    Args:
    listaPalabra: list [] 

    return: list [] 
    '''
    stop_words=set(stopwords.words('spanish'))
    listaSinStopWords=[]
    for palabra  in listaPalabra:
        if palabra not in stop_words:
            listaSinStopWords.append(palabra)
    return listaSinStopWords

def tokenizar(texto):
    '''
    Función que Tokeniza en español un texto. 

    Args:
    texto: str

    return: List []
    '''
    tokens = nltk.word_tokenize(texto,'spanish')
    return tokens

# ----------------------- principal ---------------------------------------
# leer el archivo de texto
contenido = leerTexto("texto1.txt")

# eliminar signos de puntuación
textoSinSignosPuntuacion = eliminarSignosPuntuacion(contenido)

# tokenizar texto
listaPalabras = tokenizar(textoSinSignosPuntuacion)

# eliminar stopwords
listaPalabrasSinStopWords=eliminarStopWords(listaPalabras)

# aplicamos SnoballStemer
espaniolStemer = SnowballStemmer('spanish')

# muestra los resultados
print('{0:20}{1:20}'.format('Palabra','SnowballStemmer'))
print('-'*60)
for palabra in listaPalabrasSinStopWords:
    print('{0:20}{1:20}'.format(palabra,espaniolStemer.stem(palabra)))

