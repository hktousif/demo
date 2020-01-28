from html.parser import HTMLParser
from pip._vendor.distlib.compat import raw_input


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for e in attrs:
            print("-> " + e[0] + " > " + str(e[1]))

    def handle_endtag(self, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for e in attrs:
            print("-> " + e[0] + " > " + str(e[1]))


parser = MyHTMLParser()
for _ in range(int(raw_input())):
    parser.feed(raw_input())
