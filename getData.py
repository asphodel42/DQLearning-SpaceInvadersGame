from database import create_connection, fetch_data_to_dataframe, createScatterMatrix, createCorrelationMatrix

# Connection parameters
host = 'localhost'
user = 'root'
password = '0000'
database = 'dql_data'
table = 'game_dat_test_099_0001'

connection = create_connection(host, user, password, database)

df = fetch_data_to_dataframe(connection, table)
df_statisitc = df.loc[:, ['score','episode']]

createScatterMatrix(df_statisitc, 'statistics\scatter-matrix\scatterTest1.jpg', True)
# createCorrelationMatrix(df_statisitc, 'statistics\correlation-Matrix\correlationTest.jpg')