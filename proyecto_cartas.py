"""
Representaremos un juego de cartas con las siguientes clases:

Carta: Representaremos las cartas mediante esta clase.
Mazo: Representaremos el mazo de cartas mediante esta clase.
Mano: Representaremos la mano de cartas de un jugador mediante esta clase.
Juego: Representaremos un mazo mezclado de cartas mediante esta clase.
Truco: Representaremos la mano de dos jugadores del famoso juego de cartas conocido como Truco mediante esta clase.

Cada clase tiene sus respectivos metodos y atributos.

"""



class Carta:
  """
  Representaremos una carta mediante un palo y un numero.
  """

  def __init__(self , palo , numero):
    self.palo = palo
    self.numero = numero
    self.es_comodin = palo == 'Comodin'


  def __str__(self):
    
    if self.es_comodin:
      return 'Comodin'
    
    if self.numero == 10:
      tipo = 'Sota'
    elif self.numero == 11:
      tipo ='Caballo'
    elif self.numero == 12:
      tipo = 'Rey'
    elif self.numero == 1:
      tipo='As'
    else:
      tipo = self.numero
    return f'{tipo} de {self.palo}'


  def __eq__(self , other):
    return self.palo == other.palo and self.numero == other.numero





class Mazo:

  def __init__(self):
    """
    Representaremos un mazo mediante una lista de cartas.
    """
    palos = ["Basto" , "Espada" , "Copa" , "Oro" , "Comodin"]
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
    self.mazo=[]
      
        
    for palo in palos:
        for num in numeros:

          if palo == "Comodin":
              comodin1 = Carta("Comodin" , 0)
              comodin2 = Carta("Comodin" , 0)
              self.mazo.append(str(comodin1))
              self.mazo.append(str(comodin2))
              break

          carta = Carta (palo , num)
          self.mazo.append(str(carta))


  def mostrar_mazo(self):
    """
    La funcion muestra el mazo.
    """
    return self.mazo


  def cantidad_cartas(self):
    """
    La funcion muestra la cantidad de cartas que tiene el mazo.
    """
    return len(self.mazo)


  def mezclar_mazo(self):
    """
    la funcion mezcla el mazo.
    """
    random.shuffle(self.mazo)
        

  def sacar(self , carta):
    """
    La funcion recibe una carta y si la misma esta en el mazo la saca y devuelve True. En caso contrario devuelve False.
    """
            
    if str(carta) in self.mazo:
      self.mazo.remove(str(carta))
      return True
    else:
      return False


  def sacar_carta(self):
    """
    La funcion saca la ultima carta del mazo
    """
    first = self.mazo.pop(0)
    return first


  def quedan_cartas(self):
    """
    La funcion devuelve True si le quedan cartas al mazo. En caso contrario devuelve False.
    """
    return len(self.mazo) != 0
            


  def repartir_cartas(self , manos , numero ):
    """
    La funcion recibe una lista de manos y un numero.
    Reparte la cantidad de cartas indicadas por el numero a cada mano.
    Devuelve una lista de manos con las cartas repartidas
    """
    mazo.mezclar_mazo()
    num = 0
    manitos = []
        
    for mano in manos:
      mano = mano.ver_mano()

      while mazo.quedan_cartas() and len(mano) != numero :
        carta = mazo.sacar_carta()
        mano.append(carta)
        num +=1

        manitos.append(mano)
        mano=[]
        num = 0
        
        
    return manitos






class Mano:

  def __init__(self , nombre , numero): 
    """
    Representaremos una mano mediante una lista.
    """
    self.nombre = nombre 
    self.mano = []
    mazo = Mazo ()
    mazo.mezclar_mazo()
    


    while len(self.mano) < numero:
      carta = mazo.sacar_carta()
      self.mano.append(carta)
    


  def ver_mano(self):
    """
    La funcion muestra la mano.
    """
    return self.mano


  def agregar_carta(self , mazo):
    """
    La funcion recibe un mazo y agrega una carta a la mano.
    """
    mano = self.mano

    if mazo.quedan_cartas():
      agregada = True
      while agregada:
        carta = mazo.sacar_carta()
        if carta not in mano:
          mano.append(carta)
          agregada = False
    
    return mano
        
          
  def sacar_carta(self):
    """
    La funcion saca la ultima carta de la mano.
    """
    self.mano.pop(0)
    return self.mano





class Juego:
  """
  Representaremos un mazo mezclado de cartas.
  """

  def __init__(self, mazo):
    self.mazo = mazo
    mazo.mezclar_mazo()
    self.juego = mazo.mostrar_mazo()
    

  def mostrar_juego(self):
    return self.juego





class TrucoArgentino(Juego):
  
  def __init__ (self , jugador1 , jugador2 ,* args , ** kwargs ): 
    super().__init__(* args , ** kwargs )
    """
    Representaremos al famoso juego de cartas TrucoArgentino.
    El constructor recibe dos jugadores y un mazo.
    """

    self.jugador1 = jugador1
    self.jugador2 = jugador2
    

    palos = ["Basto" , "Espada" , "Copa" , "Oro" , "Comodin"]
    numeros = [8,9]

    
    for palo in palos:
      for num in numeros:
        carta = Carta (palo , num)
        self.mazo.sacar(str(carta))
        
    mano1 = Mano (self.jugador1 , 0)
    mano2 = Mano (self.jugador2 , 0)

    self.truco = self.mazo.repartir_cartas([mano1,mano2] , 3)


  def mostrar_truco(self):
    """
    La funcion muestra el truco.
    """
    return self.truco


  def gana_envido(self):
    """
    La funcion devuelve el nombre del jugador que gane el envido.
    En caso de empate, el jugador1 es mano.
    """

    puntos_jugador_1 = 0
    puntos_jugador_2 = 0
    numero = []
    palos = ["Espada" , "Basto" , "Copa" , "Oro"]
    
    palos_repetidos = {}
    num_jugador = 1

    
    for manos in self.truco:
      for carta in manos:
        for palo in palos:
          if palo in carta:
            if palo not in palos_repetidos:
              palos_repetidos[palo] =  [carta]
            else:
              palos_repetidos[palo].append(carta)

      
      for carta in palos_repetidos:
        valor = palos_repetidos[carta]
        
        if len(valor) > 1:
          for carta in valor:
            if carta[0] in ['2','3','4','5','6','7']:
              numero_de_carta = int(carta[0])
              numero.append(numero_de_carta)
            elif carta[0] == "A":
               numero_de_carta = 1
               numero.append(numero_de_carta)
            else:
              numero.append(0)

          numero.sort()
          
          if len(numero) == 3:
            numero1 = numero[1]
            numero2 = numero[2]

            puntos_jugador_num_jugador = numero1 + numero2 + 20
          
          elif len(numero) == 2:
            if 0 in numero:
              numero1 = numero[1]
              puntos_jugador_num_jugador = 20 + numero1
            else:
              numero1 = numero[0]
              numero2 = numero[1]

              puntos_jugador_num_jugador = numero1 + numero2 + 20

          else:
            puntos_jugador_num_jugador = 0


          if num_jugador == 1:
            puntos_jugador_1 = puntos_jugador_num_jugador
          else:
            puntos_jugador_2 = puntos_jugador_num_jugador

      numero = []
      palos_repetidos = {}
      num_jugador = 2
      

    if puntos_jugador_1 > puntos_jugador_2:
        return f"El jugador {self.jugador1} gana el envido.\n{self.jugador1} = {puntos_jugador_1}\n{self.jugador2} = {puntos_jugador_2}"
    elif puntos_jugador_1 == puntos_jugador_2:
        return f"El jugador {self.jugador1} gana el envido por ser mano.\n{self.jugador1} = {puntos_jugador_1}\n{self.jugador2} = {puntos_jugador_2}"
    else: 
        return f"El jugador {self.jugador2} gana el envido.\n{self.jugador1} = {puntos_jugador_1}\n{self.jugador2} = {puntos_jugador_2}"
        
        


