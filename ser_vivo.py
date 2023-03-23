class Ser_Vivo:
      
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        
    def ataque(self, inimigo ):
        validaDefesa = False
        ataque = int(input('Pontos de ataque:'))
               
        while validaDefesa == False:
            defesa = int(input('Defesa usada pelo inimigo:'))
            if defesa > int(ataque):
                print("Defesa não pode ser maior que o ataque")
            else:
                validaDefesa = True
                inimigo.pontos_vida = inimigo.pontos_vida - (ataque - defesa)
              
                
        return (f'O {type(inimigo).__name__} foi atacado por {self.nome}. Dano sofrido: {(ataque - defesa)}')
            
     
    def aumenta_vida(self, personagem , quant_vida):
        personagem.pontos_vida += quant_vida
        return (f'Status de vida {personagem.pontos_vida}')
        
        
    def status_vida(self): 
        return (f'Status de vida do {type(self).__name__} : {self.pontos_vida} ')
        
    
    # def ataque(self,pontos_ataque, inimigo ):
    #     check = False
        
    #     while check == False:
    #         pontos_defesa = int(input ('Defesa:'))
    #         if pontos_defesa > int(pontos_ataque):
    #             print("Defesa não pode ser maior que o ataque")
    #         else:
    #             check = True
    #             inimigo.pontos_vida = inimigo.pontos_vida - (pontos_ataque - pontos_defesa)
                
    #     return (f'O {type(inimigo).__name__} foi atacado. Status de vida {inimigo.pontos_vida}')
        
   
  
        
        
          