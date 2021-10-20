
def min_numar(lst,cif):
    '''
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    :param lst: int
    :return: celui mai mic numar intreg cu ultima cifra egala cu o cifra citita de la tastatura
    '''
    rez=[]
    for el in lst:
        if el % 10 ==cif:
                rez.append(el)
    return rez
def test_min_numar():
    assert min_numar([1, 6, 34, 68, 40, 48, 20],8)==[48]

def numere_negative(lst):
    '''
    Afișarea tuturor numerelor negative nenule din listă
    :param lst: int
    :return: numerele negative nenule din lst
    '''
    rez=[]
    for el in lst:
        if el<0:
            rez.append(el)
    return rez
def test_numere_negative():
    assert numere_negative([-1,-2,-4,5,6,7])==[-1,-2,-4]
    assert numere_negative([-1,-2,-4,5,7,0])==[-1,-2,-4]
def read_list():
    lst = [int(el) for el in input('Introduceti elementele separate prin spatiu: ').split(' ')]
    return lst
def show_menu():
    print('''
    1. Citirea unei liste de numere întregi.
    2.  Afișarea tuturor numerelor negative nenule din listă (de ex. -1, -56).
    3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    4.Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este
strict pozitiv și toate prefixele sale sunt prime. De exemplu, 173 nu este superprim deoarece 1 nu
este prim, iar 239 este superprim deoarece 2, 23 și 239 sunt toate prime.
    5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    6. Afisare lista
    x. Iesire
    ''')
def main():
    lst = []
    while True:
        show_menu()
        cmd=input("Comand:")
        if cmd == '1':
            lst=read_list()
        elif cmd == '2':
            rez=numere_negative(lst)
            print(rez)
        elif cmd=='3':
            cif=int(input('cif='))
            print(min_numar(lst,cif))
        elif cmd=='4':
           pass
        elif cmd=='5':
            pass
        elif cmd == '6':
            print(lst)
        elif cmd == 'x':
            break
        else:
            print("Invalid command")
def run_tests():
    test_numere_negative()
    test_min_numar()
    run_tests()

main()
