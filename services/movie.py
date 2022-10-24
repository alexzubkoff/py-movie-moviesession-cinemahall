from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        return Movie.objects.all()

    if genres_ids and actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids).\
            filter(actors__id__in=actors_ids)

    if genres_ids and not actors_ids:
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids and not genres_ids:
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> QuerySet:
    if movie_id:
        if Movie.objects.filter(id=movie_id):
            return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str, movie_description: str,
                 genres_ids: list[int] = None,
                 actors_ids: list[int] = None) -> None:
    if movie_title and movie_description:
        movie = Movie.objects.create(title=movie_title,
                                     description=movie_description)

    if genres_ids:
        for genre_id in genres_ids:
            movie.genres.add(genre_id)

    if actors_ids:
        for actor_id in actors_ids:
            movie.actors.add(actor_id)