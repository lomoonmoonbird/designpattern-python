#!/usr/local/bin/python
# --*-- coding:utf-8 --*--

class TextTag(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldText(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return "<b>{text}</b>".format(text=self._text.render())

class ItalitText(object):
    def __init__(self,text):
        self._text = text

    def render(self):
        return "<i>{text}</i>".format(text=self._text.render())


def main():
    text = TextTag('hello')
    text2 = BoldText(ItalitText(text))
    print(text2.render())

if __name__ == '__main__':
    main()