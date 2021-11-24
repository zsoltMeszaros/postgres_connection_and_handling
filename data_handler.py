from database_common import query_with_return_value, query_without_return_value


def check_word_exists(word):
    word_exists = query_with_return_value(
            f"SELECT EXISTS(SELECT 1 FROM words WHERE word='{word}')"
        )
    return word_exists[0][0]


def get_words_table_content():
    
    query_string = "SELECT * FROM words"
    rows = query_with_return_value(query_string)

    return rows


def get_every_word():
    query_string = "SELECT word FROM words"

    rows = query_with_return_value(query_string)
    return rows


def get_random_word(difficulty):
    
    if difficulty in ["easy", "medium", "hard"]:
        query_string = f"""
                        SELECT word FROM words
                        WHERE word_difficulty='{difficulty}'
                        ORDER BY random()
                        LIMIT 1
                        """

        word = query_with_return_value(query_string)
        return word
    else:
        print("Invalid difficulty, only available: easy, medium, hard")


def insert_word(word, difficulty):

    #if difficulty in ["easy", "medium", "hard"]:
        
    word_exists = check_word_exists(word)

    if not word_exists:            
        query_string = f"""
                        INSERT INTO words
                        VALUES ('{word}', '{difficulty}')
                        """
        query_without_return_value(query_string)
        print(f"Row inserted into TABLE \"words\" with values: {word} - {difficulty}")
    #else:
     #   print("Invalid difficulty, only available: easy, medium, hard")


def delete_word(word):
    word_exists = check_word_exists(word)

    if word_exists:
        query_string = f"""
                        DELETE FROM words
                        WHERE word='{word}';
                        """
        
        query_without_return_value(query_string)
        print(f"Row deleted with word: {word}")
    else:
        print("Word is not in TABLE \"words\"")


def summa(a, b):
    return a+b
