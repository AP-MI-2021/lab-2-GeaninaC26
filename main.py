def is_palindrome(n):
    '''
    Verificam daca numarul dat este palindrom
    Input:
    -x, numar natural, dat
    Output:
    -False, daca numarul nu este palindrom
    -True, daca numarul este palindrom
    '''
    temp = n
    reverse = 0
    while (n > 0):
        cifra = n % 10
        reverse = reverse * 10 + cifra
        n = n // 10
    if (temp == reverse):
        return True
    else:
        return False


def test_verif_palindrom():
    assert is_palindrome(0) == True
    assert is_palindrome(7) == True
    assert is_palindrome(676)== True
    assert is_palindrome(6788)==False


def get_perfect_squares(a, b):
    '''
    Cautam toate patratele perfecte din intervalul [a,b]
    Input:
    - a, b, intregi, capetele intervalului
    Output:
    -lst, lista patratlor perfecte
    '''
    radacina = int(a ** 0.5)
    lst = []

    if radacina*radacina < a :
        radacina = radacina + 1
    while radacina < b ** 0.5 :
        lst.append(radacina*radacina)
        radacina = radacina + 1
    return lst

def test_get_perfect_squares():
    assert get_perfect_squares(1, 10) == [1, 4, 9]
    assert get_perfect_squares(4, 20) == [4, 9, 16]

def is_prime(nr):
    '''
    Testam daca numarul nr este prim
    Input
    -nr, numar natural, dat
    Output
    -True, daca nr prim, False daca nr compus 
    '''
    if nr<2 :
        return False
    if nr == 2 :
        return True
    for i in range (2, nr) :
        if nr % i == 0 :
            return False
    return True
        
def is_superprime(nr) :
    '''
    Testam daca numarul nr este superprim
    Input
    -nr, numar natural, dat
    Output
    -True, daca nr superprim, False altfel 
    '''
    if nr == 0 :
        return False
    while nr > 0 :
        if is_prime(nr) == False :
            return False
        nr = nr // 10
    return True 

def test_is_superprime() :
    assert is_superprime(2) == True
    assert is_superprime(252) == False
    assert is_superprime(0) == False
    assert is_superprime(230) == False
    assert is_superprime(1) == False


def main():
    while True:
        print('1.Numar palindrom.')
        print('2.Patrate perfecte din intervalul [a,b].')
        print('3.Numar Superprim')
        print('x.Exit');
        optiune=input('Alegeti o optiune:')
        if optiune == '1' :
            n = int(input("Enter a number:"))
            test_verif_palindrom()
            if is_palindrome(n) == True :
                print("Numarul este palindrom.")
            else :
                print("Numarul nu este palindrom.")
        elif optiune == '2' :
                a = int(input("Dati capatul de inceput al intervalului: "))
                b = int(input("Dati capatul de inchidere al intervalului: "))
                test_get_perfect_squares()
                print(get_perfect_squares(a, b))
        elif optiune == '3' :
                nr = int(input("Enter a number: "))
                if is_superprime(nr) == True :
                    print('Numarul este superprim.')
                else :
                    print('Numarul nu este superprim.')
        elif optiune == 'x' :
            break
        else :
            print('Optiune nevalida.')

if __name__ == '__main__' :
    main()