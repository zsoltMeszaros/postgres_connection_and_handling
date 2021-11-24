import psycopg2


def query_with_return_value(query):
    try:

        user_name = "postgres"
        password = "4566"
        host = "localhost"
        database_name = "hangman_words"

        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )

        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        return rows

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()


def query_without_return_value(query):
    try:

        user_name = "postgres"
        password = "4566"
        host = "localhost"
        database_name = "hangman_words"

        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )

        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(query)
        cursor.close()


    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()
