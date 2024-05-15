def add(a, b):
    return a + b
 
 
import unittest
 
 
class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 1), 3)
    # Task 1 :add unit testcase for negative numbers
    def test_neg(self):
        self.assertEqual(add(-1,-1),-2)
    # Task 2 :add unit testcase for decimal numbers
    def test_dec(self):
        self.assertEqual(add(0.10,0.23),0.33)
class TestInterestModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        print("Setup Ran...")
        self.accounts = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "johndoe@example.com",
                "isActive": True,
                "balance": 150.75,
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "janesmith@example.com",
                "isActive": True,
                "balance": 500.50,
            },
            {
                "id": 3,
                "name": "Emily Jones",
                "email": "emilyjones@example.com",
                "isActive": True,
                "balance": 0.00,
            },
        ]
 
    def tearDown(self):
        print("TearDown : Clear cursor")
 
    def test_interest_rate_for_active_user(self):
        # Act
        output = adds_interest(self.accounts, 0.1)
        print("Test 1")
        # Assert
        self.assertEqual(add(1.2, 3.2), 4.4)
 
    def test_interest_rate_for_non_active_user(self):
        output = adds_interest(self.accounts, 0.1)
        print("Test 2")
        # self.assertEqual(output[1]["balance"], 500.5)
 
import unittest
from DAO import MovieService
from Entity import Movie
 
 
class TestMovieServiceModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        self.movie_service = MovieService()
 
    def test_add_movie(self):
        title = "Leo"
        year = 2023
        director_id = 6
        new_movie = Movie(title, year, director_id)
        created_movie = self.movie_service.create_movie(new_movie)
        self.assertTrue(created_movie)
 

 
if __name__ == "__main__":
    unittest.main()
