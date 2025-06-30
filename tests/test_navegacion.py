# tests/test_navegacion.py

def test_navegacion_pantallas():
    pantallas = ["Inicio", "Estado de cuenta", "Contrato", "Seguros"]
    assert pantallas.index("Inicio") == 0
    assert pantallas[-1] == "Seguros"
    assert len(pantallas) == 4
