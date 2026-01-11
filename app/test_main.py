import datetime
from unittest.mock import MagicMock

import app.main as main
from app.main import outdated_products


class TestOutdatedProducts:
    @staticmethod
    def mock_today(monkeypatch: MagicMock, fake_today: datetime.date) -> None:

        mock_date = MagicMock(wraps=datetime.date)
        mock_date.today.return_value = fake_today
        monkeypatch.setattr(main.datetime, "date", mock_date)

    def test_no_outdated_products(self, monkeypatch: MagicMock) -> None:
        fake_today = datetime.date(2026, 1, 9)
        self.mock_today(monkeypatch, fake_today)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2026, 2, 10)},
            {"name": "chicken", "expiration_date": datetime.date(2026, 2, 5)},
        ]

        assert outdated_products(products) == []

    def test_one_outdated_product(self, monkeypatch: MagicMock) -> None:
        fake_today = datetime.date(2026, 1, 9)
        self.mock_today(monkeypatch, fake_today)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2026, 1, 8)},
            {"name": "chicken", "expiration_date": datetime.date(2026, 2, 5)},
        ]

        assert outdated_products(products) == ["salmon"]

    def test_two_outdated_products(self, monkeypatch: MagicMock) -> None:
        fake_today = datetime.date(2026, 1, 9)
        self.mock_today(monkeypatch, fake_today)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2026, 1, 5)},
            {"name": "chicken", "expiration_date": datetime.date(2026, 1, 3)},
        ]

        assert outdated_products(products) == ["salmon", "chicken"]

    def test_expiration_date_today_not_outdated(
            self,
            monkeypatch: MagicMock
    ) -> None:
        fake_today = datetime.date(2026, 1, 9)
        self.mock_today(monkeypatch, fake_today)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2026, 1, 9)},
            {"name": "chicken", "expiration_date": datetime.date(2026, 1, 9)},
        ]

        assert outdated_products(products) == []

    def test_expiration_date_yesterday_outdated(
            self,
            monkeypatch: MagicMock
    ) -> None:
        fake_today = datetime.date(2026, 1, 9)
        self.mock_today(monkeypatch, fake_today)

        products = [
            {"name": "salmon", "expiration_date": datetime.date(2026, 1, 8)},
            {"name": "chicken", "expiration_date": datetime.date(2026, 1, 9)},
        ]

        assert outdated_products(products) == ["salmon"]
