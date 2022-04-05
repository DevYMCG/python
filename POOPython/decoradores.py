class CasillaDeVotacion: # Declaramos nuestra clase principal

    def __init__(self, identificador, pais): # Definimos los parametros
        self.__identificador = identificador 
        self.__pais = pais # Declaramos los atributos privados
        self.__region = None
    
    @property
    def region(self): # Definimos el metodo para obtener la region
        return self.__region
    
    @region.setter # Propiedad setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La región {region} no es valida en {self.__pais}')


if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    print(f'{casilla.region}')
    casilla.region = 'Venezuela'
    print(f'{casilla.region}')