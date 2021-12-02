from http import HTTPStatus


class TestDirectorsView:
    def test_many(self, client, director):
        response = client.get("/directors/")
        assert response.status_code == HTTPStatus.OK
        assert response.json == [{"id": director.id, "name": director.name}]

    def test_director_pages(self, client, director):
        response = client.get("/directors/?page=1")
        assert response.status_code == HTTPStatus.OK
        assert len(response.json) == 1

        response = client.get("/directors/?page=2")
        assert response.status_code == HTTPStatus.OK
        assert len(response.json) == 0

    def test_director(self, client, director):
        response = client.get("/directors/1")
        assert response.status_code == HTTPStatus.OK
        assert response.json == {"id": director.id, "name": director.name}

    def test_director_not_found(self, client, director):
        response = client.get("/directors/2")
        assert response.status_code == HTTPStatus.NOT_FOUND
