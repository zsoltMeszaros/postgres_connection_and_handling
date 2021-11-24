from database_common import query_with_return_value, query_without_return_value
from data_handler import delete_word, insert_word, summa
import unittest


class Test_TestDatabaseFunctions(unittest.TestCase):

    def test_insert_word(self):

        word = "testdata123"
        difficulty = "medium"

        # insert word using external function
        insert_word(word, difficulty)

        # get inserted row
        result = query_with_return_value(
            f"""
            SELECT * FROM words
            WHERE word='{word}'
            """
        )

        # delete inserted row
        query_with_return_value(
            f"""
            DELETE FROM words
            WHERE word='{word}'
            """
        )

        expected = [('testdata123', 'medium')]

        self.assertEqual(expected, result)


    def test_delete_word(self):

        word = "testdata123"
        difficulty = "medium"

        # insert to-delete test data
        query_without_return_value(
                f"""
                    INSERT INTO words
                    VALUES ('{word}', '{difficulty}')
                """)

        #delete word using external function
        delete_word(word)

        # check if word exists in database
        word_exists = query_with_return_value(
            f"SELECT EXISTS(SELECT 1 FROM words WHERE word='{word}')"
        )
        
        
        self.assertFalse(word_exists[0][0])

    
    def test_summa(self):

        test_number_1 = 5
        test_number_2 = 7

        expected = 12

        result = summa(test_number_1, test_number_2)

        self.assertEqual(expected, result)