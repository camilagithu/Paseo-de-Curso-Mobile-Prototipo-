# tests/test_estado_cuenta.py

def test_estado_cuenta_alumno():
    alumno = {
        "nombre": "Camila Vera",
        "aportes": [10000, 20000, 15000],
        "meta": 100000
    }

    total_aportado = sum(alumno["aportes"])
    saldo_restante = alumno["meta"] - total_aportado

    assert total_aportado == 45000
    assert saldo_restante == 55000
