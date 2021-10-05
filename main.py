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

def main():
    while True:
        print('1.Numar palindrom.')
        print('2.Patrate perfecte din intervalul [a,b]')
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
        elif optiune == 'x' :
            break
        else :
            print('Optiune nevalida.') 


main()