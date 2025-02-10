def commands(binary_str: str):

    actions = ["jump", "close your eyes", "double blink", "wink"]

    secret_handshake = []
    for index, bit in enumerate(binary_str[1:]):
        if bit == "1":
            secret_handshake.append(actions[index])

    if list(binary_str)[0] == "0":
        secret_handshake.reverse()

    return secret_handshake
