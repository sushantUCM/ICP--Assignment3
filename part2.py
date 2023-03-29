import matplotlib.pyplot as plt

programmingLanguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
dictionary = dict(zip(programmingLanguages, popularity))
dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(dictionary.values(), labels=dictionary.keys(), explode=explode, autopct='%1.1f%%', shadow=True, startangle=135)
plt.axis('equal')
plt.show()
