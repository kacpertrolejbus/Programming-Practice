class iterator:
    def __init__(self, dane):
        self._dane = dane
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._dane):
            el  = self._dane[self._index]
            self._index += 1
            return el
        else:
            raise StopIteration

class MojaKolekcja:
    def __init__(self):
        self._dane = []

    def dodaj(self, el):
        self._dane.append(el)

    def __iter__(self):
        return iterator(self._dane)
    
print("Start:")
kolekcja = MojaKolekcja()
kolekcja.dodaj("Element 67")
kolekcja.dodaj("Element 2137")

for przedmiot in kolekcja:
    print(przedmiot)


