#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request

    # req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as req:
        content = req.read()
    print("Body response:")
    print('\t - type: {}'.format(type(content)))
    print('\t - content: {}'.format(content))
    print('\t - utf8 content: {}'.format(content.decode('UTF8')))