from db import data
r=1
running=True
running_1=True
running_2=True
running_3=True
#score_points=0
s=''
#что-то вроде рандомайзера
r=1
a = 1664525
c = 1013904223
m = 2**32

def random(data):
    global r
    r= (a*r+c)%m
    return r % (len(data)) 


#join
def join(iterable, separator):
    result = ''
    for index, element in enumerate(iterable):
        result += str(element)
        if index < len(iterable) - 1:
            result += separator
    return result

while running == True:
    running_1=True
    print('')
    print('#####  МЕНЮ  #####')
    print('1. Отгадать новое слово')
    print('2. Счет')
    print('3. Выйти из игры\n')
    option=int(input('Выберите опцию:'))

    if option==1:
        print("Нажмите '3', чтобы вернуться в меню")

        '''#random 
        a = 1664525
        c = 1013904223
        m = 2**32
        r= (a*r+c)%m
        random = 0 + r % (len(data))
        '''

        #цикл первой опции
        while running_1:
            random_index=random(data)
            word_to_guess = data[random_index][0]#загаданное слово 
            hint = data[random_index][1]#определение загаданного слова

            guessed_word = ["*"]*len(word_to_guess)#неотгаданное слово в виде массива
            right_word = join(guessed_word,s)#неотгаданное слово

            #print(random(data))
            print("-- ", hint)
            print(right_word)

             #цикл отгадавания
            while '*' in guessed_word:
                letter = input("Введите букву или слово целиком:")

                #отгадали слово целиком
                if len(letter) >1:
                     if letter == word_to_guess:
                         print(word_to_guess)
                         print("Ура! победа!")
                         #print("+ 4 балла\n")
                         #score_points += 4
                         running_1 = False
                         break
                     else:
                         print("Неправильно, попробуйте снова!\n")
                         continue
                #ввели ничо, а надо чо
                elif len(letter)==0:
                    print("Введите букву или слово, а не пустоту\n")
                    continue
                #Возвращение в меню
                elif  letter == '3':
                    running_1 = False
                    break

                else:
                     if  letter in word_to_guess:
                         for i in range(len(word_to_guess)):
                             if letter == word_to_guess[i]:
                                 guessed_word[i]=letter
                                 #score_points+=1
                         print(join(guessed_word,s),'\n')

                     else:
                         print("Этой буквы нет в загаданном слове.\n")
    # if option == 2:
    #     print("Ваш счёт:", score_points)

    if option == 3:
        print("До новых встреч!")
        running=False

