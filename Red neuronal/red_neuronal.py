import math


class RedNeuronal:
    def __init__(self, neuronas_entrada, descripcion_capas, descripcion_bias, descripcion_conexiones):
        descripcion_conexiones.insert(0, [])
        descripcion_bias.insert(0, [])
        self.red_entradas = []
        self.red_salidas = []
        self.red_errores = []
        i = 0
        while i < len(descripcion_capas):
            self.red_entradas.append([0] * descripcion_capas[i])
            self.red_salidas.append([0] * descripcion_capas[i])
            self.red_errores.append([0] * descripcion_capas[i])
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

    def calculo_error_ultima_capa(self, salidas_esperadas):
        neurona = 0
        while neurona < len(self.red_errores[-1]):
            self.red_errores[-1][neurona] = self.red_salidas[-1][neurona] - salidas_esperadas[neurona]
            neurona += 1
    

    def dp_salida_conexion(self, capa, neurona):
        return self.red_salidas[capa][neurona] * (1 - self.red_salidas[capa][neurona])


    def dp_conexion_salida(self, capa, neurona, neurona_conectada):
        return self.red_conexiones[capa][neurona][neurona_conectada]


    def calculo_error_capa(self, capa):
        neurona = 0
        while neurona < len(self.red_errores[capa]):
            self.red_errores[capa][neurona] = 0.0
            neurona_conectada = 0
            while neurona_conectada < len(self.red_errores[capa + 1]):
                self.red_errores[capa][neurona] += self.dp_salida_conexion(capa + 1, neurona_conectada) \
                        * self.dp_conexion_salida(capa + 1, neurona_conectada, neurona) * \
                        self.red_errores[capa + 1][neurona_conectada]
                neurona_conectada += 1
            print()
            neurona += 1

    def entrenamiento(self, salidas_esperadas):
        self.prediccion()
        self.calculo_error_ultima_capa(salidas_esperadas)
        capa = len(self.red_errores) - 2
        while capa >= 0:
            self.calculo_error_capa(capa)
            capa -= 1
        print(self.red_errores)

        
def funcion_activacion(x):
    return 1 / (1 + math.exp(-x))


if __name__ == "__main__":
    red = RedNeuronal([0.05, 0.1], [2, 2, 2], [[0.35, 0.35], [0.6, 0.6]], 
            [[[0.15, 0.2], [0.25, 0.3]], [[0.40, 0.45], [0.50, 0.55]]])
    red.entrenamiento([0.01, 0.99])