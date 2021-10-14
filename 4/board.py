class Board:

    _state = ""

    def __init__(self, msg):
        self._state = self._state + " " + msg

    def append_msg(self, msg):
        self._state = self._state + " " + msg

    def fetch_msg(self):
        return self._state
