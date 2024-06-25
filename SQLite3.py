# Here, you use the to_sql() function to convert the pandas dataframe to an SQL table.

# The table_name and sql_connection arguments specify the name of the required table and the database to which you should load the dataframe.

# The if_exists parameter can take any one of three possible values:
# 'fail': This denies the creation of a table if one with the same name exists in the database already.
# 'replace': This overwrites the existing table with the same name.
# 'append': This adds information to the existing table with the same name.

# Keep the index parameter set to True only if the index of the data being sent holds some informational value. Otherwise, keep it as False.


df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

df = pandas.read_sql(query_statement, sql_connection)
