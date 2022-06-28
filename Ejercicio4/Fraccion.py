class Fraccion():
    __numerador = None
    __denominador = None

    def __init__(self, numerador, denominador=1):
        result = self.simplificar(numerador, denominador, 0)
        self.__numerador = result[0]
        self.__denominador = result[1]
        if self.__numerador == 0:
            self.__numerador = 0
            self.__denominador = 1
        if self.__denominador < 0:
            self.__denominador = -self.__denominador
            self.__numerador = -self.__numerador

    def __str__(self):
        if self.getDenominador() == 1:
            cadena = str(self.getNumerador())
        else:
            cadena = str(self.__numerador)+'/'+str(self.__denominador)
        return cadena

    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador

    def __add__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = int((((den1*den2)/den1)*num1+((den1*den2)/den2)*num2))
        result_den = (den1*den2)
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __radd__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = int((((den1*den2)/den1)*num1+((den1*den2)/den2)*num2))
        result_den = (den1*den2)
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __sub__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = int((((den1*den2)/den1)*num1-((den1*den2)/den2)*num2))
        result_den = (den1*den2)
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __rsub__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = int((((den1*den2)/den1)*num1-((den1*den2)/den2)*num2))
        result_den = (den1*den2)
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __mul__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = num1 * num2
        result_den = den1 * den2
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __rmul__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = num1 * num2
        result_den = den1 * den2
        result = self.simplificar(result_num, result_den, 0)
        result = Fraccion(result[0], result[1])
        return result

    def __floordiv__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = num1 * den2
        result_den = den1 * num2
        if result_den == 0:
            result = 'Math ERROR'
        else:
            result = self.simplificar(result_num, result_den, 0)
            result = Fraccion(result[0], result[1])
        return result

    def __rfloordiv__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion(otro)
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = otro.getNumerador()
        den2 = otro.getDenominador()
        result_num = num1 * den2
        result_den = den1 * num2
        if result_den == 0:
            result = 'Math ERROR'
        else:
            result = self.simplificar(result_num, result_den, 0)
            result = Fraccion(result[0], result[1])
        return result

    def simplificar(self, num, den, m):
        if (abs(num) == 0 or abs(num == 1)) or (abs(den) == 0 or abs(den == 1)):
            result = [num, den]
            return result
        if m == 0:
            if abs(num) < abs(den):
                m = abs(num)
            else:
                m = abs(den)
            return self.simplificar(num, den, m)
        else:
            if m >= 2:
                if abs(num) % m == 0 and abs(den) % m == 0:
                    num = int(num / m)
                    den = int(den / m)
                    if abs(num) < abs(den):
                        m = abs(num)
                    else:
                        m = abs(den)
                    return self.simplificar(num, den, m)
                else:
                    return self.simplificar(num, den, m - 1)
        resultado = [num, den]
        return resultado
