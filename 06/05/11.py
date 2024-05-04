class HtmlTag:
    lvl = -1
    def __init__(self, tag, inline=False):
        self.tag, self.inline = tag, inline
    def __enter__(self):
        if self.inline:
            self._end = ''
        else:
            self._end = '\n'
        HtmlTag.lvl += 1
        print('  '*HtmlTag.lvl + f'<{self.tag}>', end=self._end)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if HtmlTag.lvl == 0:
        if self.inline:
            t = f'</{self.tag}>'
        else:
            t = '  '*HtmlTag.lvl + f'</{self.tag}>'
        print(t)
        HtmlTag.lvl -= 1

    def print(self, text):
        if not self.inline:
            print('  '*(self.lvl)+'  '+text, end=self._end)
        else:
            print(f'{text}', end=self._end)


# TEST_5:
with HtmlTag('table') as _:
    with HtmlTag('tr') as paragraph:
        with HtmlTag('th', True) as field:
            field.print('текст заголовка')
        with HtmlTag('td') as data:
            with HtmlTag('ul'):
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')
                with HtmlTag('li', True) as marked_list:
                    marked_list.print('данные')