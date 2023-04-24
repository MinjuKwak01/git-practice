def do_fizzbuzz(num:int):

    for i in range(1,num+1):
        if i%3==0:
            print('fizz')
        elif:
            print('buzz')
        else:
            print(f'{i}')
    print('hello')

    """
    fizzbuzz: print fizz buzz fizzbuzz
    3: fizz
    5: buzz
    15: fizzbuzz
    etc: num
    """

if __name__=='__main__':
    do_fizzbuzz(16)
