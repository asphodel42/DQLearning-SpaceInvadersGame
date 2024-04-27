import pymysql
import pandas as pd
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

def create_table(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS game_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    episode INT,
                    score INT,
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


def insert_data(connection, episode, score, record, epsilon, gamma, alpha, duration):
    # gammaAlpha = gamma / alpha
    # alphaGamma = alpha / gamma
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO game_data (episode, score, record, epsilon, 
                           gamma, alpha, gammaAlpha, alphaGamma, duration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (episode, score, record, epsilon, gamma, alpha,
                  gamma/alpha, alpha/gamma, duration))
        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print("Error:", e)

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

def createPlot(filename, episode, score, mean):
    # Створення графіка
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