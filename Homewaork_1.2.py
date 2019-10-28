seconds = int(input("Введите целое число - "))
second = seconds // 60
minutes = second // 60
hours = minutes // 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}' )

