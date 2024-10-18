class CustomButton:
    text = ""

    def __init__(self, text):
        self.text = text


class CustomUrlButton(CustomButton):
    url = ""

    def __init__(self, text, url):
        super().__init__(text)
        self.url = url


class CustomCallbackButton(CustomButton):
    callbackFilter = None

    def __init__(self, text, filter):
        super().__init__(text)
        self.callbackFilter = filter


class KeyboardConfig:
    buttons: list[CustomButton]
    adjust: list[int]

    def __init__(self, buttons: list[CustomButton], adjust: list[list[int]]) -> None:
        self.buttons = buttons
        self.adjust = adjust
