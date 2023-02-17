from django.shortcuts import render, HttpResponse

html_base = """

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Camilo León - Fullstack Developer</title>
  </head>
  <style>

    .main-nav {
    width: 50%;
    height: 50px;
    display: inline-block;
    margin-right: 10px; /* establece un margen de 10px a la derecha para separar los elementos */
    }


    .nav-list {
    list-style: none; /* quita los puntos/bolitas de la lista */
    margin: 0;
    padding: 0;
    }

    .nav-list li {
    display: inline-block; /* muestra los elementos de la lista en línea horizontal */
    }
  </style>
  <body>
  <main>
    <nav class="main-nav">
      <ul class="nav-list">
        <li><a href="/">Home</a></li>
        <li><a href="/biography">Biography</a></li>
        <li><a href="/portfolio">Portfolio</a></li>
        <li><a href="/education">Education</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>

    <h1>Mi web personal</h1> 
"""


def home(request):
    html_response = html_base + """
            <h2>Portada</h2>
        </main>
        </body>
    </html>
    """

    return HttpResponse(html_response)


def portfolio(request):
    html_response = html_base + """
            <h2>Mis proyectos</h2>
            <p>Aqui algunos de mis proyectos...</p>
            </main>
        </body>
    </html>
    """
    return HttpResponse(html_response)


def contact(request):
    html_response = html_base + """
            <h2>Contactame</h2>
            <p>Por favor un email al correo <a href="mailto:leon971010@gmail.com"/>leon971010@gmail.com</p>
            </main>
        </body>
    </html>
    """
    return HttpResponse(html_response)

# Create your views here.
