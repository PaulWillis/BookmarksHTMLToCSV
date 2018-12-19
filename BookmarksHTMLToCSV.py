import codecs
import argparse
import time
from bs4 import BeautifulSoup

class Bookmark():
    """docstring for Bookmark"""
    def __init__(self, title, url, tag, date):
        self.title = title
        self.url = url
        self.tag = '' + tag + ' '
        self.date = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(float(date)))
        self.date = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(float(date)))
        self.content = '''<a href="%(url)s">%(title)s</a>''' % {'title': self.title, 'url': self.url}

    def printCsvLine(self):
        output = """%(tag)s , %(title)s , %(content)s  \n""" % {'title': self.title, 'content': self.content, 'tag': self.tag,} 
		
		
		
        return output.replace('&', ' ')

    def __str__(self):
        return unicode(self.title + " " + self.url + " " + self.tag)
def main():
    

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("html_file", help="the file that contains the bookmarks in html")
        args = parser.parse_args()
        soup = BeautifulSoup(codecs.open(args.html_file, encoding='utf-8'))

        html_tags = soup.findAll(['h3', 'a'])

        en_tag = ''

        bookmarks = []

        for tag in html_tags:
            if tag.name == 'h3':
                en_tag = tag.string
            if tag.name == 'a':
                new_bm = Bookmark(tag.string, tag['href'], en_tag, tag['add_date'])
                bookmarks.append(new_bm)

        print "Total bookmarks: " + str(len(bookmarks)) 

        output_file = args.html_file.split('.')[0] + ".csv"
        out = codecs.open(output_file, 'w', encoding='utf-8')

        #out.write("""note\n""") #put column names here if you want
        for n in bookmarks:
            out.write(n.printCsvLine())
            #out.write("/n") #/n if you want double spaced

        out.write(" ")
        out.close()

        print "Output file: " + output_file
    except Exception as e:
        print "Error!"
        print type(e)
        print e.args


if __name__ == '__main__':
    main()