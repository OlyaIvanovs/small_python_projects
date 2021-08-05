import caesar_cipher


def test_message_encrypting():
    step = 4
    message = "Meet me by the rose bushes tonight."
    new_message = caesar_cipher.get_chipher(message, step)
    assert new_message == "QIIX QI FC XLI VSWI FYWLIW XSRMKLX."


def test_message_decrypting():
    step = -4
    message = "QIIX QI FC XLI VSWI FYWLIW XSRMKLX."
    new_message = caesar_cipher.get_chipher(message, step)
    assert new_message == "MEET ME BY THE ROSE BUSHES TONIGHT."
