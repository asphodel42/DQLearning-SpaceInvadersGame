from database import (create_connection, fetch_data_to_dataframe, createScatterMatrix,
                       createCorrelationMatrix, getDuration, create3DGraph)
import pandas as pd

# durationDataFrame = pd.DataFrame('Alpha', 'Gamma', 'Duration')

duration_df = pd.DataFrame(columns=['alpha', 'gamma', 'duration'])

# Connection parameters
host = 'localhost'
user = 'root'
password = '0000'
database = 'dql_data'
table = 'game_dat_099_00001'

connection = create_connection(host, user, password, database)
duration_df = getDuration(connection, 'game_dat_02_02', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_04_02', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_06_00001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_06_02', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_07_00001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_07_02', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_08_00001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_08_01', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_08_02', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_08_04', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_08_06', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_099_00001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_099_0001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_099_0001_128_256', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_099_0001_256_128', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_09_000001', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_09_01', duration_df)
connection = create_connection(host, user, password, database)

duration_df = getDuration(connection, 'game_dat_test_099_0001', duration_df)

print(duration_df)

create3DGraph(duration_df)
# df = df.tail(5000)
# df_statisitc = df.loc[:, ['score', 'record', 'mean', 'episode', 'epsilon', 'duration']]

# createScatterMatrix(df_statisitc, 'statistics\scatter-matrix\scatter5000.jpg', True)
# createCorrelationMatrix(df_statisitc, 'statistics\correlation-Matrix\correlation.png')