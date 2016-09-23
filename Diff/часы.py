#http://informatics.mccme.ru/mod/statements/view3.php?id=3309&chapterid=3481#1
#В часах села батарейка, и они стали идти вдвое медленнее. Когда на часах было x1 часов y1 минут, правильное время было
#  a1 часов b1 минут. Сколько времени будет на самом деле, когда часы в следующий раз покажут x2 часов y2 минут?


x1 = int(input())
y1 = int(input())
a1 = int(input())
b1 = int(input())
x2 = int(input())
y2 = int(input())


minut_output_1 = x1*60 + y1
)
minut_output_2 = x2*60 + y2

delta_output = minut_output_2 - minut_output_1

delta_output_real = 2 * delta_output


minut_real_1 = a1*60 + b1
minut_real_2 = minut_real_1 + delta_output_real

hour_real_2 = minut_real_2 // 60
mi_real_2 = minut_real_2 % 60

print(hour_real_2, mi_real_2)
