from database import create_connection, fetch_data_to_dataframe, createScatterMatrix, createCorrelationMatrix

# Connection parameters
host = 'localhost'
user = 'root'
password = '0000'
database = 'dql_data'
table = 'game_dat_test2'

connection = create_connection(host, user, password, database)

df = fetch_data_to_dataframe(connection, table)
df_statisitc = df.loc[:, ['episode', 'score', 'record', 'epsilon', 'duration']]

createScatterMatrix(df_statisitc, 'statistics\scatter-matrix\scatterTest.jpg')
createCorrelationMatrix(df_statisitc, 'statistics\correlation-Matrix\correlationTest.jpg')