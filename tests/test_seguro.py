# tests/test_seguro.py

def test_detalle_seguro():
    seguro = {
        "nombre": "Plan Estudiantil Full",
        "cobertura": ["Enfermedad", "Accidente", "Repatriación"]
    }

    assert seguro["nombre"] == "Plan Estudiantil Full"
    assert "Accidente" in seguro["cobertura"]
