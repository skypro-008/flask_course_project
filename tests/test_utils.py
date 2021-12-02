import pytest

from project.utils.utils import get_limit_and_offset


@pytest.mark.parametrize(
    "page, result",
    [
        (None, (3, 0)),
        (1, (3, 0)),
        (-1, (3, 0)),
        (2, (3, 3)),
    ],
)
def test_get_limit_and_offset(app, page, result):
    app.config["ITEMS_PER_PAGE"] = 3
    assert get_limit_and_offset(page) == result
