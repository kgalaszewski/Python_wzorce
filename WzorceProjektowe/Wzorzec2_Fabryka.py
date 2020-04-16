class TagHtmlowy(object):
    html = ""

    def get_html(self):
        return self.html


class Tagzdjecie(TagHtmlowy):
    html = "<img></img>"


class Taginput(TagHtmlowy):
    html = "<input></input>"


class FabrykaTagow():
    def create_button(self, typ):
        targetclass = typ.capitalize()
        return globals()[targetclass]()


fabryka = FabrykaTagow()
tagi = ['Tagzdjecie', 'Taginput']
for b in tagi:
    print(fabryka.create_button(b).get_html())
