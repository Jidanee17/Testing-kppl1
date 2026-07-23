import pytest
from main import cek_ganjil_genap

def test_cek_ganjil_genap_even():
    assert cek_ganjil_genap(2) == "Genap"
    assert cek_ganjil_genap(0) == "Genap"
    assert cek_ganjil_genap(-4) == "Genap"

def test_cek_ganjil_genap_odd():
    assert cek_ganjil_genap(1) == "Ganjil"
    assert cek_ganjil_genap(-3) == "Ganjil"
    assert cek_ganjil_genap(99) == "Ganjil"

def test_cek_ganjil_genap_invalid_type():
    with pytest.raises(TypeError):
        cek_ganjil_genap("angka")  # type: ignore
    with pytest.raises(TypeError):
        cek_ganjil_genap(2.5)  # type: ignore
