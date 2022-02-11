#!/usr/bin/env python3
import sys
import sqlite3
import jinja2


def main():
    file = sys.argv[1]
    conn = sqlite3.connect(file)
    sql = "SELECT VolumeID, Text, Annotation FROM bookmark"
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    books = {}
    for vol, text, note in res:
        if text is None:
            continue
        title = vol.split("/")[-1].split(".kepub")[0].split(".epub")[0]
        if title in books:
            books[title].append((text, note))
        else:
            books[title] = [(text, note)]
    output = jinja2.Environment(loader=jinja2.FileSystemLoader("./")).get_template('template.html').render(annotations=books)
    with open('output.html', 'w') as f:
        f.write(output)
    print("Ready! Your annotations have been exported as output.html")
    conn.close()


if __name__ == "__main__":
    main()
