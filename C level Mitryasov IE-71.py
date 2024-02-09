#First zadanie
import pandas as pd
data = pd.read_csv('random_data.csv', delimiter=';', names=['Name', 'Age', 'City', 'wheight'])
print("Датасет сейчас:")
print(data)
print("\nДоступные столбцы:")
print(data.columns.tolist())
column_name = input("Введите название столбца в котором нужно изменить текст: ")
row_index = int(input("Введите номер строки в которой нужно изменить текст нумерация с 0: "))
new_text = input("Введите новый текст: ")
data.at[row_index, column_name] = new_text
print("\nновый датасет:")
print(data)
data.to_csv('random_data.csv', sep=';', index=False, header=False)
#Second zadanie
data = pd.DataFrame({
     'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eric'],
     'Age': [22, 29, 31, 25, 31],
     'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
     'wheight': [55, 52, 74, 100, 33]})
print(data)
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
plt.hist(data['Age'], bins=10, color='red')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.title('Возроста пользователей')
plt.figure(figsize=(6, 6))
plt.pie(data['Age'], labels=data['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Кружок возрастов пользователей')
plt.figure(figsize=(6, 4))
plt.boxplot(data['Age'])
plt.ylabel('Возраст')
plt.title('Ящик с усами')
plt.show()
plt.show()
plt.show()