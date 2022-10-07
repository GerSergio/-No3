print("Ведите количество лет")
number_of_years=int(input())
time=5
exp_in_day=96
year=365
exp_in_year=exp_in_day*year
ans=number_of_years*exp_in_year
s=ans+(exp_in_day*(number_of_years//4))#Проверка на високосный год
print(s,"экспонатов будет просмотрено одним человеком")



print("Введите количество экспонатов")
exp_count=int(input())
exp1=5
how_min=exp_count*exp1
print("колииество минут :",how_min)

