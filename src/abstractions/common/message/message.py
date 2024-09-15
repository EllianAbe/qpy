from .headers import MessageHeaders


class Message():
    def __init__(self, content: dict, headers: MessageHeaders):
        self.content = content
        self.headers = headers
