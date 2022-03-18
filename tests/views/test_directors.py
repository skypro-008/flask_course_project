class TestDirectorsView:
    def test_many(self, client, director):
        response = client.get("/directors/")
        assert response.status_code == 200
        assert response.json == [{"id": director.id, "name": director.name}]

    def test_director_pages(self, client, director):
        response = client.get("/directors/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/directors/?page=2")
        assert response.status_code == 404

    def test_director(self, client, director):
        response = client.get("/directors/1/")
        assert response.status_code == 200
        assert response.json == {"id": director.id, "name": director.name}

    def test_director_not_found(self, client, director):
        response = client.get("/directors/2/")
        assert response.status_code == 404
