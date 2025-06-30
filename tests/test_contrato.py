def test_visualizacion_contrato():
    contrato = {
        "curso": "4to Medio A",
        "destino": "Bariloche",
        "servicios": ["Hotel", "Transporte", "Seguro"]
    }

    assert contrato["destino"] == "Bariloche"
    assert "Hotel" in contrato["servicios"]
    assert "Seguro" in contrato["servicios"]
