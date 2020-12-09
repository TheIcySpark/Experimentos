import math

class Red_neuronal:
    def __init__ (self, descripcion_capas, descripcion_bias, descripcion_pesos):
        self.CAPAS = 0
        self.BIAS = 1
        self.PESOS = 2
        self.ERRORES = 3
        self.red = [[], [[]], [], []]
        self.red[self.ERRORES] = [0] * descripcion_capas[-1]
        i = 0
        while i < len(descripcion_capas):
            self.red[self.CAPAS].append([])
            self.red[self.CAPAS][i] = [0] * descripcion_capas[i]
            i += 1
        i = 0
        while i < len(descripcion_bias):
            self.red[self.BIAS].append([])
            self.red[self.BIAS][i + 1] = descripcion_bias[i]
            i += 1
        i = 0
        while i < len(descripcion_pesos):
            self.red[self.PESOS].append([])
            self.red[self.PESOS][i] = descripcion_pesos[i]
            i += 1
    

    def suma_sinaptica(self, capa, neurona):
        i = 0
        ret = 0.0
        capa -= 1
        while i < len(self.red[self.CAPAS][capa]):
            ret += self.red[self.CAPAS][capa][i] * self.red[self.PESOS][capa][i][neurona]
            i += 1
        ret += self.red[self.BIAS][capa + 1][neurona]
        return ret


    def prediccion(self):
        capa = 1
        while capa < len(self.red[self.CAPAS]):
            neurona = 0
            while neurona < len(self.red[self.CAPAS][capa]):
                self.red[self.CAPAS][capa][neurona] = funcion_activacion(self.suma_sinaptica(capa, neurona))
                neurona += 1
            capa += 1
    

    def calculo_errores(self, resultados_esperados):
        neurona = 0
        while neurona < len(self.red[self.ERRORES]):
            self.red[self.ERRORES][neurona] = math.pow(resultados_esperados[neurona] -
                    self.red[self.CAPAS][-1][neurona], 2) / 2
            neurona += 1
    

    def backpropagation(self, resultados_esperados):
        taza_aprendisaje = 0.5
        neurona = 0
        while neurona < len(self.red[self.PESOS][1]):
            neurona_b = 0
            while neurona_b < len(self.red[self.PESOS][1][neurona]):
                d_total, d_neurona, d_peso, derivada  = 0.0, 0.0, 0.0, 0.0
                d_total = self.red[self.CAPAS][-1][neurona_b] - resultados_esperados[neurona_b]
                d_neurona = self.red[self.CAPAS][-1][neurona_b] * (1 - self.red[self.CAPAS][-1][neurona_b])
                d_peso = self.red[self.CAPAS][1][neurona]
                derivada = d_total * d_neurona * d_peso
                self.red[self.PESOS][1][neurona][neurona_b] = \
                    self.red[self.PESOS][1][neurona][neurona_b] - taza_aprendisaje * derivada
                neurona_b += 1
            neurona += 1
        print(self.red[self.PESOS])


    def entrenamiento(self, inputs,  resultados_esperados):
        neurona = 0
        while neurona < len(self.red[self.CAPAS][0]):
            self.red[self.CAPAS][0][neurona] = inputs[neurona]
            neurona += 1
        self.prediccion()
        self.calculo_errores(resultados_esperados)
        self.backpropagation(resultados_esperados)



def funcion_activacion(x):
    return 1 / (1 + math.exp(-x))

    
if __name__ == "__main__":
    red = Red_neuronal([2,2,2], [[0.35, 0.35], [0.6, 0.6]], 
    [[[0.15, 0.25], [0.2, 0.3]], [[0.4, 0.5], [0.45, 0.55]]])
    red.entrenamiento([0.05, 0.1], [0.01, 0.99])
