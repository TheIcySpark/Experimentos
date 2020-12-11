import math


class RedNeuronal:
    def __init__(self, neuronas_entrada, descripcion_capas, descripcion_bias, descripcion_conexiones):
        descripcion_conexiones.insert(0, [])
        descripcion_bias.insert(0, [])
        self.red_entradas = []
        self.red_salidas = []
        i = 0
        while i < len(descripcion_capas):
            self.red_entradas.append([0] * descripcion_capas[i])
            self.red_salidas.append([0] * descripcion_capas[i])
            i += 1
        self.red_salidas[0] = neuronas_entrada
        self.red_conexiones = descripcion_conexiones
        self.red_bias = descripcion_bias

    
    def suma_conexion_sinaptica(self, capa, neurona):
        ret = 0.0
        neurona_conectada = 0
        while neurona_conectada < len(self.red_entradas[capa - 1]):
            ret += self.red_conexiones[capa][neurona][neurona_conectada] * self.red_salidas[capa - 1][neurona_conectada] 
            neurona_conectada += 1
        ret += self.red_bias[capa][neurona]
        return ret


    def prediccion(self):
        capa = 1
        while capa < len(self.red_entradas):
            neurona = 0
            while neurona < len(self.red_entradas[capa]):
                self.red_entradas[capa][neurona] = self.suma_conexion_sinaptica(capa, neurona)
                self.red_salidas[capa][neurona] = funcion_activacion(self.red_entradas[capa][neurona])
                neurona += 1
            capa += 1

        
def funcion_activacion(x):
    return 1 / (1 + math.exp(-x))


if __name__ == "__main__":
    red = RedNeuronal([0.05, 0.1], [2, 2, 2], [[0.35, 0.35], [0.6, 0.6]], 
            [[[0.15, 0.2], [0.25, 0.3]], [[0.40, 0.45], [0.50, 0.55]]])
    red.prediccion()