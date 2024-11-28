from flask import Blueprint, render_template, request
from flask_login import current_user
from src.service import getTopics, getAllPosts, getAllPostByTopic, getAllChallengesByTopic, getAllExamplesByTopic, getAllMaterialsByTopic, getPost, getMaterial, getChallenge, getExample, getCommentsByPost, searchContent
from src.utils.format_responses import format_responses

other = Blueprint("other", __name__)

materialDidactico = [
  {
    "titulo": "Introducción a python",
    "descripcion": "Un curso en línea que cubre los fundamentos de python.",
    "tecnologia": "python",
    "fecha": "2024-10-16",
    "id": 1,
    "usuario": "user2"
  },
  {
    "titulo": "python Crash Course",
    "descripcion": "Un libro que ofrece una introducción práctica a la programación en python.",
    "tecnologia": "python",
    "fecha": "2024-10-16",
    "id": 2,
    "usuario": "user2"
  },
  {
    "titulo": "Automate the Boring Stuff with python",
    "descripcion": "Un libro que enseña a automatizar tareas cotidianas con python.",
    "tecnologia": "python",
    "fecha": "2024-10-16",
    "id": 3,
    "usuario": "user2"
  },
  {
    "titulo": "Data Science Handbook",
    "descripcion": "Una guía completa para la ciencia de datos con python.",
    "tecnologia": "python",
    "fecha": "2024-10-16",
    "id": 4,
    "usuario": "user2"
  },
  {
    "titulo": "Flask Web Development",
    "descripcion": "Un libro que cubre el desarrollo web usando Flask y python.",
    "tecnologia": "python",
    "fecha": "2024-10-16",
    "id": 5,
    "usuario": "user2"
  },
  
  {
    "titulo": "javascript: The Good Parts",
    "descripcion": "Un libro que destaca las mejores características de javascript.",
    "tecnologia": "javascript",
    "fecha": "2024-10-16",
    "id": 6,
    "usuario": "user2"
  },
  {
    "titulo": "You Don't Know JS",
    "descripcion": "Una serie de libros que profundiza en conceptos avanzados de javascript.",
    "tecnologia": "javascript",
    "fecha": "2024-10-16",
    "id": 7,
    "usuario": "user2"
  },
  {
    "titulo": "Eloquent javascript",
    "descripcion": "Un libro que introduce conceptos avanzados de javascript.",
    "tecnologia": "javascript",
    "fecha": "2024-10-16",
    "id": 8,
    "usuario": "user2"
  },
  {
    "titulo": "javascript for Kids",
    "descripcion": "Un libro que enseña javascript de manera sencilla y divertida.",
    "tecnologia": "javascript",
    "fecha": "2024-10-16",
    "id": 9,
    "usuario": "user2"
  },
  {
    "titulo": "Learning javascript Data Structures and Algorithms",
    "descripcion": "Un libro que enseña estructuras de datos y algoritmos en javascript.",
    "tecnologia": "javascript",
    "fecha": "2024-10-16",
    "id": 10,
    "usuario": "user2"
  },

  {
    "titulo": "html & css: Design and Build Websites",
    "descripcion": "Un libro que enseña los fundamentos del diseño web con html y css.",
    "tecnologia": "css",
    "fecha": "2024-10-16",
    "id": 11,
    "usuario": "user2"
  },
  {
    "titulo": "Learning Web Design",
    "descripcion": "Un libro que cubre los fundamentos de html, css y diseño web.",
    "tecnologia": "html",
    "fecha": "2024-10-16",
    "id": 12,
    "usuario": "user2"
  },
  {
    "titulo": "html5: Up and Running",
    "descripcion": "Una guía rápida sobre html5 y sus nuevas características.",
    "tecnologia": "html",
    "fecha": "2024-10-16",
    "id": 13,
    "usuario": "user2"
  },
  {
    "titulo": "css Secrets",
    "descripcion": "Un libro que presenta técnicas avanzadas para el diseño con css.",
    "tecnologia": "css",
    "fecha": "2024-10-16",
    "id": 14,
    "usuario": "user2"
  },
  {
    "titulo": "Responsive Web Design with html5 and css",
    "descripcion": "Un libro que enseña a crear sitios web responsivos con html5 y css.",
    "tecnologia": "html",
    "fecha": "2024-10-16",
    "id": 15,
    "usuario": "user2"
  },

  {
    "titulo": "java para principiantes",
    "descripcion": "Un curso básico que cubre la programación orientada a objetos en java.",
    "tecnologia": "java",
    "fecha": "2024-10-16",
    "id": 16,
    "usuario": "user2"
  },
  {
    "titulo": "Effective java",
    "descripcion": "Un libro que ofrece mejores prácticas para programar en java.",
    "tecnologia": "java",
    "fecha": "2024-10-16",
    "id": 17,
    "usuario": "user2"
  },
  {
    "titulo": "java Concurrency in Practice",
    "descripcion": "Un libro que cubre la programación concurrente en java.",
    "tecnologia": "java",
    "fecha": "2024-10-16",
    "id": 18,
    "usuario": "user2"
  },
  {
    "titulo": "Head First java",
    "descripcion": "Un enfoque visual y divertido para aprender java.",
    "tecnologia": "java",
    "fecha": "2024-10-16",
    "id": 19,
    "usuario": "user2"
  },
  {
    "titulo": "java: A Beginner's Guide",
    "descripcion": "Un libro que ofrece una guía completa para principiantes en java.",
    "tecnologia": "java",
    "fecha": "2024-10-16",
    "id": 20,
    "usuario": "user2"
  }
]

sections = ["foro", "retos", "ejemplos-de-codigo"]

@other.route("/")
def home_page():
    return render_template("home.html", showSideBar = True, topics = getTopics(), posts=getAllPosts(), logged=current_user.is_authenticated)

@other.route("/<string:topic>/<string:section>")
def section_page(topic, section):
    if (section in sections):
      if (section == "foro"):
          return render_template(f"sections/{section}.html", showSideBar=True, topics=getTopics(), topic=topic, section=section, logged=current_user.is_authenticated, posts=getAllPostByTopic(tema=topic))
      elif (section == "retos"):
          return render_template(f"sections/{section}.html", showSideBar = True, topics=getTopics(), topic=topic, section=section, logged=current_user.is_authenticated, challenges=getAllChallengesByTopic(tema=topic))
      #elif (section == "material-didactico"):
      #    data = [item for item in materialDidactico if item["tecnologia"] == topic]
      #    return render_template(f"sections/{section}.html", showSideBar = True, topics=getTopics(), topic=topic, section=section, logged=current_user.is_authenticated, materials=data)
      elif (section == "ejemplos-de-codigo"):
          return render_template(f"sections/{section}.html", showSideBar = True, topics=getTopics(), topic=topic, section=section, logged=current_user.is_authenticated, examples=getAllExamplesByTopic(tema=topic))

@other.route("/<string:topic>/<string:section>/<int:id>")
def section_specific_content(topic, section, id):
    if (section in sections):
      if (section == "foro"):
          post = getPost(id)
          _responses = getCommentsByPost(id)
          responses = format_responses(_responses)
          is_author = current_user.is_authenticated and (current_user.usuario_Id == post.usuario_Id)
          return render_template("/content/post.html", showSideBar=True, topics=getTopics(), post=post, logged=current_user.is_authenticated, is_author=is_author, responses=responses)
      elif (section == "retos"):
          challenge = getChallenge(id)
          is_author = current_user.is_authenticated and (current_user.usuario_Id == challenge.usuario_Id)
          return render_template("/content/challenge.html", showSideBar=True, topics=getTopics(), challenge=challenge, logged=current_user.is_authenticated, is_author=is_author)
      #elif (section == "material-didactico"):
      #    material = getMaterial(id)
      #    is_author = current_user.is_authenticated and (current_user.usuario_Id == material.usuario_Id)
      #    return render_template("/content/material.html", showSideBar=True, topics=getTopics(), material=material, logged=current_user.is_authenticated, is_author=is_author)
      elif (section == "ejemplos-de-codigo"):
          example = getExample(id)
          is_author = current_user.is_authenticated and (current_user.usuario_Id == example.usuario_Id)
          return render_template("/content/example.html", showSideBar=True, topics=getTopics(), example=example, logged=current_user.is_authenticated, is_author=is_author)
      
@other.route("/search")
def search_content():
  text = request.args.get("search")
  results = searchContent(text=text)
  return render_template("search.html", showSideBar=True, topics=getTopics(), logged=current_user.is_authenticated, results=results)
