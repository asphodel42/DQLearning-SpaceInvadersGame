import pymysql
import pandas as pd
from pandas.plotting import scatter_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def create_connection(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Exception as e:
        print("Error:", e)
        return None

def create_database(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print(f"Database {database} created successfully.")
        connection.close()
    except Exception as e:
        print("Error:", e)

def create_table(connection, table):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    episode INT,
                    score INT,
                    mean FLOAT,
                    record INT,
                    epsilon FLOAT,
                    gamma FLOAT,
                    alpha FLOAT,
                    gammaAlpha FLOAT,
                    alphaGamma FLOAT,
                    duration FLOAT
                )
            """)
        connection.commit()
        print("Table created successfully.")
    except Exception as e:
        print("Error:", e)


def insert_data(connection, table, episode, score, mean, record, epsilon, gamma, alpha, duration):
    if pd.isna(mean):
        mean = 0
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                INSERT INTO {table} (episode, score, mean, record, epsilon, 
                           gamma, alpha, gammaAlpha, alphaGamma, duration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (episode, score, mean, record, epsilon, gamma, alpha,
                  gamma/alpha, alpha/gamma, duration))
        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print("Error:", e)

def fetch_data_to_dataframe(connection, table):
    try:
        # Створення курсора
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Виконання SQL-запиту для вибору всіх даних з таблиці
            sql_query = f"SELECT * FROM {table}"
            cursor.execute(sql_query)
            # Отримання результатів запиту
            result = cursor.fetchall()
            # Створення pandas DataFrame з результатами запиту
            df = pd.DataFrame(result)
            return df
    except Exception as e:
        print("Error:", e)
    finally:
        # Закриття з'єднання з базою даних
        connection.close()

def addToDataFrame(df, episode, score, record, epsilon, gamma, alpha, duration):
        mean = df["Score"].mean()
        new_row = pd.DataFrame({
            'Episode': [episode],
            'Score': [score],
            'Mean': [mean],
            'Record': [record],
            'Epsilon': [epsilon],
            'Gamma': [gamma],
            'Alpha': [alpha],
            'Duration(s)': [duration]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        return df

def createPlot(episode, score, mean, filename):
    fig, ax1 = plt.subplots()

    # Побудова кривої для кількості набраних очок
    color = 'tab:red'
    ax1.set_xlabel('Games')
    ax1.set_ylabel('Score', color=color)
    ax1.plot(episode, score, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Створення другої осі для кривої epsilon
    ax2 = ax1.twinx()
    color = 'tab:orange'
    ax2.set_ylabel('Mean', color=color)
    ax2.plot(episode, mean, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    plt.savefig(filename)
    plt.close()

def createCorrelationMatrix(dataframe, filename, show=False):
    correlation_matrix = dataframe.corr() 
    plt.figure(figsize=(10, 8))
    # Побудова теплової карти
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    # Додавання заголовка до графіку
    plt.title('Correlation Matrix')
    # Відображення графіку
    plt.savefig(filename)
    if show: plt.show()

def createScatterMatrix(dataframe, filename, show=False):
    # pd.plotting.scatter_matrix(dataframe, figsize=(10, 10))
    # sns.pairplot(dataframe)
    # plt.title('Scatter Matrix')

    sns.scatterplot(x='episode', y='mean', alpha=0.6, data=dataframe)
    sns.regplot(x='episode', y='mean', data=dataframe, scatter=False, color='black')
    plt.xlabel('game')
    plt.ylabel('mean score')
    plt.title('Scatter Plot')
    plt.savefig(filename)

    if show: plt.show()
