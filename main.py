from heroi import Heroi
from lobo import Lobo
from goblin import Goblin    

def main():
    heroi = Heroi("Batman")
    lobo = Lobo(50)
    goblin = Goblin(30)
    
    
    print(heroi.ataque(lobo))
   
    print(lobo.status_vida())
    
   
   
    
if __name__ == '__main__':
    main()