from app import app


def get_client():
    return app.test_client()


def test_health():
    response = get_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_products_api():
    response = get_client().get("/api/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 5
    assert all("price" in product for product in data)


def test_home_page():
    response = get_client().get("/")
    assert response.status_code == 200
    assert b"Candle Store" in response.data
