import pandas as pd

# Чтение данных
df = pd.read_csv('train.csv')

# Основная информация о датасете
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Процент выживаемости для каждого класса пассажиров
survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
print(survival_rate)

# Самое популярное мужское и женское имя
popular_male_name = df[df['Sex'] == 'male']['Name'].mode()[0]
popular_female_name = df[df['Sex'] == 'female']['Name'].mode()[0]
print(popular_male_name, popular_female_name)

# Самое популярное мужское и женское имя в каждом классе
popular_names_by_class = df.groupby(['Pclass', 'Sex'])['Name'].apply(lambda x: x.mode()[0])
print(popular_names_by_class)

# Пассажиры старше 44 лет
older_passengers = df[df['Age'] > 44]
print(older_passengers)

# Мужчины младше 44 лет
young_males = df[(df['Age'] < 44) & (df['Sex'] == 'male')]
print(young_males)

# Количество n-местных кабин
cabin_counts = df['Cabin'].value_counts()
print(cabin_counts)
