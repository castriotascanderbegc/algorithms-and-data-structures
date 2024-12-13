"""
    Deisgn a Movie Recommendation System

    Basics
        Users can rate movies on a scale of 1 to 5
        Recommend movies based on other users who have rated movies similar to the user's rated movies
            If there is a tie, recommend any movie from the top movies
            If a user has not rated any movies, recommend the top rated movie

"""
        
# Movie class to encapsulate movie information
# Movie has id and title
class Movie:
    def __init__(self, id, title):
        self._id    = id
        self._title = title
    
    def getId(self):
        return self._id
    
    def getTitle(self):
        return self._title

# User class to encapsulate user information
# User has id and name
class User:
    def __init__(self, id, name):
        self._id    = id
        self._name = name
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name

# MovieRating enum to represent the rating scale
from enum import Enum
class MovieRating(Enum):
    NOT_RATED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


# RatingRegister class stores the ratings of movies by users
# along with a mapping of users to movies they have rates

class RatingRegister:
    def __init__(self):
        self._userMovies = {}       # we map UserId -> List<Movie>
        self._movieRatings = {}     # we map movieId -> Map<UserId -> Rating>

        self._movies = []           # list of Movie
        self._users = []            # list of User

    # add a rating to a Movie
    def addRating(self, user, movie, rating):
        if movie.getId() not in self._movieRatings:
            self._movieRatings[movie.getId()] = {}
            self._movies.append(movie)
        
        if user.getId() not in self._userMovies:
            self._userMovies[user.getId()] = []
            self._users.append(movie)
        
        self._userMovies[user.getId()].append(movie)
        self._movieRatings[movie.getId()][user.getId()] = rating
    
    # get the average rating for a Movie
    def getAverageRating(self, movie):
        if movie.getId() not in self._movieRatings:
            return MovieRating.NOT_RATED
        ratings = self._movieRatings[movie.getId()].values()
        vals = [rating.value for rating in ratings]
        return sum(vals) / len(ratings)

    def getUsers(self):
        return self._users
    
    def getMovies(self):
        return self._movies

    def getUserMovies(self, user):
        return self._userMovies.get(user.getId(), [])
    
    def getMovieRatings(self, movie):
        return self._movieRatings.get(movie.getId(), {})


# MovieRecommendation class has a reference to the RatingRegister. 
# It recommend movies to users
class MovieRecommendation:
    """
        If a user has not rated any movies, we recommend the top rated movie
        Otherwise, we recommend a movie based on the similarity score of the user with other users
            We compute the similarity score by comparing the ratings of movies rated by the user and other users
            We recommend an unwatched movie that has the highest similarity score 
    """
    def __init__(self, ratings):
        self._movieRatings = ratings
    
    def recommendMovie(self, user):
        if len(self._movieRatings.getUserMovies(user)) == 0:
            return self._recommendMovieNewUser()
        else:
            return self._recommendMovieExistingUser(user)
    
    def _recommendMovieNewUser(self):
        best_movie = None
        best_rating = 0
        for movie in self._movieRatings.getMovies():
            rating = self._movieRatings.getAverageRating(movie)
            if rating > best_rating:
                best_rating = rating
                best_movie = movie
        return best_movie.getTitle() if best_movie else None
    
    def _recommendMovieExistingUser(self, user):
        best_movie = None
        similarity_score = float('inf') # lower score is better

        for reviewer in self._movieRatings.getUsers():
            if reviewer.getId() == user.getId():
                continue
            score = self._getSimilarityScore(reviewer, user)
            if score < similarity_score:
                similarity_score = score
                recommend_movie = self._recommendUnwatchedMovie(user, reviewer)
                best_movie = recommend_movie if recommend_movie else best_movie
        
        return best_movie.getTitle() if best_movie else None
    
    def _getSimilarityScore(self, user1, user2):
        user1_id = user1.getId()
        user2_id = user2.getId()
        user2_movies = self._movieRatings.getUserMovies(user2)

        score = float('inf') # lower is better

        for movie in user2_movies:
            curr_movie_ratings = self._movieRatings.getMovieRatings(movie)
            if user1_id in curr_movie_ratings:
                score = 0 if score == float('inf') else score
                score += abs(curr_movie_ratings[user1_id].value - curr_movie_ratings[user2_id].value)
            
        return score
        
    
    def _recommendUnwatchedMovie(self, user, reviewer):
        user_id = user.getId()
        reviewer_id = reviewer.getId()
        best_movie = None
        best_rating = 0

        reviewer_movies = self._movieRatings.getUserMovies(reviewer)
        for movie in reviewer_movies:
            curr_movie_ratings = self._movieRatings.getMovieRatings(movie)
            if user_id not in curr_movie_ratings and curr_movie_ratings[reviewer_id].value > best_rating:
                best_movie = movie
                best_rating = curr_movie_ratings[reviewer_id].value
        return best_movie
    


"""
    An example of how to use the classes:
        User 1 and User 2 have similar tastes, so we recommend them an unwatched movie from each other
        User 3 has not rated any movies, so we recommend them the top rated movie

"""


user1 = User(1, 'User 1')
user2 = User(2, 'User 2')
user3 = User(3, 'User 3')

movie1 = Movie(1, 'Batman Begins')
movie2 = Movie(2, 'Liar Liar')
movie3 = Movie(3, 'The Godfather')

ratings = RatingRegister()
ratings.addRating(user1, movie1, MovieRating.FIVE)
ratings.addRating(user1, movie2, MovieRating.TWO)
ratings.addRating(user2, movie2, MovieRating.TWO)
ratings.addRating(user2, movie3, MovieRating.FOUR)

recommender = MovieRecommendation(ratings)

print(recommender.recommendMovie(user1)) # The Godfather
print(recommender.recommendMovie(user2)) # Batman Begins
print(recommender.recommendMovie(user3)) # Batman Begins
