import webbrowser as wb

def webPath():
    firefox = '/bin/firefox'
    wurls = ('https://start.fedoraproject.org/', 'https://www.netflix.com/browse', 'https://www.coursera.org/')
    for pages in wurls:
        wb.get(firefox).open(pages)

webPath()
