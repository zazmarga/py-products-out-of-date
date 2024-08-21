# import datetime
from datetime import date
import pytest
from unittest.mock import patch

from app.main import outdated_products


@pytest.fixture()
def products_template() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


def test_outdated_products(products_template: list[dict]) -> None:

    check_options = [
        (date(2022, 2, 2), ["duck"]),
        (date(2022, 2, 6), ["chicken", "duck"]),
        (date(2022, 2, 11), ["salmon", "chicken", "duck"]),
        (date(2022, 1, 10), []),
        (date(2022, 2, 1), [])
    ]

    for option in check_options:

        with patch("datetime.date") as mocked_date:
            mocked_date.today.return_value, expected_list = option
            assert outdated_products(products_template) == expected_list
