import json


class TestGetNotes:
    def test_returns_html(self, client):
        response = client.get("/notes/")
        assert response.status_code == 200
        assert b"Brak notatek" in response.data


class TestCreateNote:
    def test_creates_note(self, client):
        response = client.post(
            "/notes/",
            data=json.dumps({"title": "Test", "content": "Treść"}),
            content_type="application/json",
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data["id"] == 1
        assert data["title"] == "Test"

    def test_missing_title_returns_400(self, client):
        response = client.post(
            "/notes/",
            data=json.dumps({"content": "Brak tytułu"}),
            content_type="application/json",
        )
        assert response.status_code == 400


class TestGetNote:
    def test_get_existing_note(self, client):
        client.post(
            "/notes/",
            data=json.dumps({"title": "Notatka", "content": "Treść"}),
            content_type="application/json",
        )
        response = client.get("/notes/1")
        assert response.status_code == 200
        assert response.get_json()["title"] == "Notatka"

    def test_get_nonexistent_note_returns_404(self, client):
        response = client.get("/notes/999")
        assert response.status_code == 404