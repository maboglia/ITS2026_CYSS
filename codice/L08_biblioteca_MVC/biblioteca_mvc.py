from libro import Libro
from libro_dao import LibroDAO

dao = LibroDAO()

with open("biblioteca.html", "w") as f:
    f.write(f"""
            <html>
            <head><title>Biblioteca</title>
            <link
                        rel='stylesheet'
                        href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css'
                        >
                                    </head>
            <body>
            <div class='container'>
            """)
    for libro in dao.trova_libri():
        f.write(libro.toHtml())
    f.write("</div></body></html>")
