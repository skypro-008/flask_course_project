from http import HTTPStatus


class TestGenresView:

    def test_many(self, client, genre):
        response = client.get('/genres/')
        assert response.status_code == HTTPStatus.OK
        assert response.json == [{
            'id': genre.id,
            'name': genre.name
        }]

    def test_genre_pages(self, client, genre):
        response = client.get('/genres/?page=1')
        assert response.status_code == HTTPStatus.OK
        assert len(response.json) == 1

        response = client.get('/genres/?page=2')
        assert response.status_code == HTTPStatus.OK
        assert len(response.json) == 0

    def test_genre(self, client, genre):
        response = client.get('/genres/1')
        assert response.status_code == HTTPStatus.OK
        assert response.json == {
            'id': genre.id,
            'name': genre.name
        }

    def test_director_not_found(self, client, director):
        response = client.get('/directors/2')
        assert response.status_code == HTTPStatus.NOT_FOUND
