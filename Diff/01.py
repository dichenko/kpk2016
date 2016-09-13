#http://informatics.mccme.ru/mod/statements/view3.php?id=18087&chapterid=113016#1

#Андрей готовился к ЕГЭ по информатике и встретил в демо-версии ЕГЭ 2015 года такую задачу:
#Автомат получает на вход четырёхзначное число. По этому числу строится новое число по следующим правилам.
#1. Складываются первая и вторая, а также третья и четвёртая цифры исходного числа.
#2. Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
#Пример. Исходное число: 3165. Суммы: 3+1 = 4; 6+5 = 11. Результат: 114.
#Укажите наименьшее число, в результате обработки которого автомат выдаст число 1311.
#Андрей решил, что для самопроверки он напишет программу, которая решает подобную задачу. Мы думаем, что вы тоже с этим справитесь.
#Программа получает на вход некоторое натуральное число N, которое может содержать две, три или четыре цифры.
#Программа должна вывести такое наименьшее целое четырёхзначное число K, после применения к которому описанного выше алгоритма
#получается число N. Если же такого числа не существует, программа должна вывести число 0.




def upto_4_numbers(x):
    """
    принимаем строку длиной от 1 до 4 знаков и дописываем нулями спереди до 4х знаков
    :param x:
    :return:   строка из 4х знаков
    """
    x = str(x)
    for i in range(4-len(x)):
        x = "0" + x
    return str(x)



def avtomat_run(a):
    """
    принимаем число (в формате str) и выполняем инстукции автомата
    :param x:
    :return: полученное число
    """
    s = [a[0], a[1], a[2], a[3]]
    res1_1 = int(a[0]) + int(a[1])
    res1_2 = int(a[2]) + int(a[3])
    return int(str(max(res1_1, res1_2)) + str(min(res1_1, res1_2)))




for i in range(1,10000):
    if avtomat_run(upto_4_numbers(i)) == 1311:
        print(i)
        break

