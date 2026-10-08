class InvalidPacketError(Exception):
    pass


def parse(packet):
    return packet["id"], packet["payload"]


def handle(packet):
    try:
        result = parse(packet)
    except KeyError as e:
        raise InvalidPacketError(f"Missing field in packet: {e}") from e
    return result


handle({"id": 7})
