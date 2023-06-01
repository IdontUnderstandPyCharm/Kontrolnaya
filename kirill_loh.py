#11

class Tovar:
    
    def __init__(self, name_tovara, name_magazina, cena):
        self.name_tovara = name_tovara
        self.name_magazina = name_magazina
        self.cena = cena
        
    def inf(self):
        return [self.name_tovara, self.name_magazina, int(self.cena)]
    
    def __add__(self, name):
        return name.cena + self.cena
    
        
class Sklad:
    def __init__(self):
        self.mas = []
        
    def names(self, name):
        for i in self.mas:
            if i.name_tovara == name:
                print(i.inf())
                
    def sortik(self, prim):
        for i in range(len(self.mas)):
            for j in range(i+1, len(self.mas)):
                if self.mas[i].inf()[prim] > self.mas[j].inf()[prim]:
                    self.mas[i], self.mas[j] = self.mas[j], self.mas[i]
        for i in self.mas:
            print(i.inf())
            
            
tovar1 = Tovar('sfgsfg1', 'sfgdg', 10)
tovar2 = Tovar('sfgdg', 'sfgsfg1', 20)
sklad = Sklad()
sklad.mas.extend([tovar1, tovar2])
print(sklad.mas[0].inf())
print(tovar1 + tovar2)
sklad.sortik(2)
