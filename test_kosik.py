import pytest
from kosik import pridej, odeber, celkem_bez_slevy, celkem_se_slevou


@pytest.fixture
def kosik():
    k = {}
    return k

@pytest.fixture
def kosik_plny():
    k = {"chleba":2, "maslo":1, "rohlik":10}
    return k

@pytest.fixture
def cenik():
    return {
    "maslo": (55, 0),
    "chleba": (20, 5),
    "vajcka6": (30, 10),
    "rohlik": (2, 0),
    "vanocka": (25, 25),
    "parek": (13, 0),
    "tvahor": (32, 1)
    }


def test_pridej(kosik):
    kosik = pridej(kosik, "chleba")
    kosik = pridej(kosik, "chleba")
    kosik = pridej(kosik, "maslo")
    assert kosik == {"chleba":2, "maslo":1}

def test_odeber(kosik_plny):
    kosik_plny = odeber(kosik_plny, "chleba")
    kosik_plny = odeber(kosik_plny, "maslo")
    assert kosik_plny == {"chleba":1, "rohlik":10}

def test_celkem(kosik_plny, cenik):
    assert 115. == celkem_bez_slevy(kosik_plny, cenik)

def test_celkem_se_slevou(kosik_plny, cenik):
    assert 113. == celkem_se_slevou(kosik_plny, cenik)