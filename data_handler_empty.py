from database_common import query_with_return_value, query_without_return_value


def check_word_exists(word):
    result = query_with_return_value(f"""
                                    SELECT word FROM words
                                    WHERE word='{word}';
                                    """)
    
    # print(len(result) != 0)

    if len(result) == 1:
        return(True)
    else:
        return(False)


def get_words_table():
    rows = query_with_return_value("""
                                    SELECT * FROM words
                                    """)
    
    return rows


def get_random_word(difficulty):

    word = query_with_return_value(f"""
                                    SELECT word FROM words
                                    WHERE word_difficulty='{difficulty}'
                                    ORDER BY random()
                                    LIMIT 1
                                    """)

    return word


def insert_word(word, difficulty):
    
    query_without_return_value(f"""
                                INSERT INTO words (word, word_difficulty)
                                VALUES ('{word}', '{difficulty}')
                                """)

    if check_word_exists(word): #belekerült-e
        print(f"Word inserted into the \"words\" table with the value: {word}")
    else:
        print("Word not inserted into table")


def delete_word(word):
    
    if check_word_exists(word):

        query_without_return_value(f"""
                                    DELETE FROM words
                                    WHERE word='{word}'
                                    """)

        if check_word_exists(word): #törölve lett-e
            print(f"Word not deleted: {word}")
        else:
            print(f"Word deleted from table: {word}")
    else:
        print(f"Word not in table: {word}")


delete_word("szó")
#check_word_exists("nincsbenne")
# check_word_exists("nice")
# insert_word_into_table("removethis", "medium")
# print_words_table()
# print_random_easy_word()
