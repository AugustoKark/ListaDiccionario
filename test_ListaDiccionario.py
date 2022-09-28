import unittest

def Buscar_Repetidos(lista):

    resultado={}
    

    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                ac=lista[i]
                lista[i]=lista[j]
                lista[j]=ac

    for elem in lista:
        

        if elem not in resultado:
            
            resultado[elem]=1
        else:
            resultado[elem]+=1
    return resultado

    
    

class Repetido(unittest.TestCase):
    def test_1(self):
        valor = Buscar_Repetidos([8,7])
        self.assertEqual(valor, {7:1, 8:1})
    
    
    def test_2(self):
        valor = Buscar_Repetidos([8,7,8])
        self.assertEqual(valor, {7:1, 8:2})

    
    def test_3(self):
        valor = Buscar_Repetidos([8,7,8,7,9])
        self.assertEqual(valor, {7:2, 8:2, 9:1})

    
    def test_4(self):
        valor = Buscar_Repetidos([101,8,7,8,7,9])
        self.assertEqual(valor, {7:2, 8:2, 9:1, 101:1})
    

    def test_5(self):
        valor = Buscar_Repetidos([101,8,7,8,7,9, 432, 432])
        self.assertEqual(valor, {7:2, 8:2, 9:1, 101:1, 432:2})

   


if __name__ == '__main__':
     unittest.main() 