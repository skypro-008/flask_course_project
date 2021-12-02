from http import HTTPStatus

import pytest

from project.models import Director, Genre, Movie


class TestMoviesView:

    @pytest.fixture
    def movies(self, db, genre, director):
        movies_list = []
        for i in range(10):
            obj = Movie(
                title=f'title_{i}',
                description=f'description_{i}',
                year=2000 + i,
                genre_id=genre.id,
                director_id=director.id
            )
            db.session.add(obj)
            db.session.flush()
            movies_list.append(obj)
        db.session.commit()
        return movies_list

    def test_invalid_state(self, client):
        response = client.get('/movies/?state=old')
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @pytest.mark.parametrize('page, resp_length', [
        (1, 3),
        (4, 1),
        (5, 0)
    ])
    def test_pages(self, app, client, movies, page, resp_length):
        app.config['ITEMS_PER_PAGE'] = 3
        response = client.get(f'/movies/?page={page}')
        assert response.status_code == HTTPStatus.OK
        assert len(response.json) == resp_length

    def test_success_state(self, client, movies):
        response_1 = client.get('/movies/?state=new')
        response_2 = client.get('/movies/')
        assert response_1.json[0]['year'] > response_2.json[0]['year']

    def test_no_pages(self, app, client, movies):
        app.config['ITEMS_PER_PAGE'] = 3
        response_1 = client.get(f'/movies/')
        assert response_1.status_code == HTTPStatus.OK
        assert len(response_1.json) == len(movies)

        response_2 = client.get(f'/movies/?state=new')
        assert response_2.status_code == HTTPStatus.OK
        assert len(response_2.json) == len(movies)
