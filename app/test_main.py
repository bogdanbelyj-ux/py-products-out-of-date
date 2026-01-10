import datetime
from unittest import mock

from app.main import outdated_products


def test_no_outdated_products() -> None:
    fake_today = datetime.date(2026, 1, 9)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 2, 10),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 2, 5),
            "price": 120,
        },
    ]

    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = fake_today

        result = outdated_products(products)

        assert result == []


def test_with_one_outdated_product() -> None:
    fake_today = datetime.date(2026, 1, 9)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 1, 8),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 2, 5),
            "price": 120,
        },
    ]

    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = fake_today

        result = outdated_products(products)

        assert result == ["salmon"]


def test_with_two_outdated_products() -> None:
    fake_today = datetime.date(2026, 1, 9)

    products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2026, 1, 5),
            "price": 600,
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2026, 1, 3),
            "price": 120,
        },
    ]

    with mock.patch("app.main.datetime") as mocked_date:
        mocked_date.date.today.return_value = fake_today

        result = outdated_products(products)

        assert result == ["salmon", "chicken"]
