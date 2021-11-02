from socket import socket

OFFSET_X = 8
OFFSET_Y = 0


class Lamp:
    def __init__(self, sock: socket, addr: tuple):
        self._sock = sock
        self._addr = addr

        self._buff = list()
        for i in range(16):
            tmp = list()
            for j in range(16):
                tmp.append(0)
            self._buff.append(tmp)

    def send(self, cmd: str) -> None:
        self._sock.sendto(cmd.encode(), self._addr)

    def clear(self) -> None:
        self.send("CLR")

    def draw_matrix(self, matrix, clear=False) -> None:
        if clear:
            self.clear()

        
