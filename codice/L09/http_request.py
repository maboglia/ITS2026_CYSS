import requests

URL = 'https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/best-free-yt-movies-rt.json'

response = requests.get(URL)


risposta = response.json()

# f.write(type(risposta))

with open("film.html", "w") as f:

    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>Film migliori su YouTube</title>\n")
    f.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" >\n')
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<div class='container'>\n")

    f.write("<h1>Film migliori su YouTube</h1>\n")

    f.write("<table>\n")

    f.write("<tr><th>Title</th><th>Year</th><th>Rating</th></tr>\n")

    for film in risposta:
        f.write("<tr>")
        for chiave, valore in film.items():
            if chiave == "titolo":
                f.write(f"<td><a target='_blank' href='https://www.google.com/search?q=youtube+{valore}'>{valore}</a></td>")
            else:
                f.write(f"<td>{valore}</td>")
        f.write("</tr>\n")

    f.write("</table>\n")
    f.write("</div>\n")
    f.write("</body>\n")
    f.write("</html>\n")
    # f.write(response.status_code)
    # f.write(response.text)

print("File film.html creato con successo!")