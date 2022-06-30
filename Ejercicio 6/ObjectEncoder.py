import json

class Objectencoder:
    def lectura(self, archivo):
        with open(archivo, encoding='UTF-8') as fuente:
            dic = list(json.load(fuente))
            if dic == {}:
                dic = None
            fuente.close()
            return dic

    def guardado(self, elementos, archivo):
        with open(archivo, 'w', encoding='UTF-8') as destino:
            json.dump(elementos, destino, indent=4)
            destino.close()
