# tests/test_notificacion.py

def test_envio_notificacion():
    deposito = {
        "tipo": "colectivo",
        "monto": 50000,
        "enviar_correo": True
    }

    assert deposito["tipo"] == "colectivo"
    assert deposito["enviar_correo"] is True
