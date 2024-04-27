import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


def insert_data(connection, table, episode, score, record, epsilon, gamma, alpha, duration):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
                INSERT INTO {table} (episode, score, record, epsilon, 
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

# def createPlot(x, scores, mean, filename, lines=None):
#     fig=plt.figure()
#     ax=fig.add_subplot(111, label="1")
#     ax2=fig.add_subplot(111, label="2", frame_on=False)

#     ax.plot(x, scores, color="C0")
#     ax.set_xlabel("Game", color="C0")
#     ax.set_ylabel("Score", color="C0")
#     ax.tick_params(axis='x', colors="C0")
#     ax.tick_params(axis='y', colors="C0")

#     # N = len(scores)
#     # running_avg = np.empty(N)
#     # for t in range(N):
#     #     running_avg[t] = np.mean(scores[max(0, t-20):(t+1)])

#     ax2.plot(x, mean, color="C1")
#     #ax2.xaxis.tick_top()
#     ax2.axes.get_xaxis().set_visible(False)
#     ax2.yaxis.tick_right()
#     #ax2.set_xlabel('x label 2', color="C1")
#     ax2.set_ylabel('Mean', color="C1")
#     #ax2.xaxis.set_label_position('top')
#     ax2.yaxis.set_label_position('right')
#     #ax2.tick_params(axis='x', colors="C1")
#     ax2.tick_params(axis='y', colors="C1")

#     if lines is not None:
#         for line in lines:
#             plt.axvline(x=line)

#     plt.savefig(filename)
#     plt.close()
