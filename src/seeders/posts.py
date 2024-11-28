from src.models import Post
from src.service import createPost

posts = [
    {
        "titulo": "¿Cómo manejar excepciones anidadas en Python?", 
        "descripcion": "Estoy trabajando en un programa donde necesito manejar diferentes tipos de excepciones en distintos niveles de anidación. ¿Cuál sería la mejor manera de implementar esto sin hacer el código difícil de leer?", 
        "tema": "python", "usuario_Id": 1, 
        "codigo": """
            try:
                x = int(input("Ingrese un número: "))
                try:
                    result = 10 / x
                except ZeroDivisionError:
                    print("No se puede dividir entre cero.")
                else:
                    print("Resultado:", result)
            except ValueError:
                print("Debe ingresar un número válido.")

        """
    },
    {
        "titulo": "¿Cómo usar generadores para manejar grandes volúmenes de datos?", 
        "descripcion": "Estoy procesando un archivo de texto muy grande en Python, y se me recomendó usar generadores para manejar mejor la memoria. ¿Alguien podría explicar cómo funcionan y proporcionar un ejemplo práctico?", 
        "tema": "python", "usuario_Id": 1, 
        "codigo": """
            def leer_lineas(archivo):
                with open(archivo, 'r') as f:
                    for linea in f:
                        yield linea.strip()

            for linea in leer_lineas('archivo_grande.txt'):
                print(linea) 
        """
    },   
    {
        "titulo": "¿Cómo implementar patrones de diseño con clases abstractas en Java?", 
        "descripcion": "Estoy tratando de entender cómo usar clases abstractas en Java para implementar el patrón de diseño Factory. ¿Podrían proporcionar un ejemplo sencillo?", 
        "tema": "java", "usuario_Id": 1, 
        "codigo": """
            abstract class Producto {
                abstract void crear();
            }

            class ProductoA extends Producto {
                void crear() {
                    System.out.println("Producto A creado");
                }
            }

            class ProductoB extends Producto {
                void crear() {
                    System.out.println("Producto B creado");
                }
            }

            class Fabrica {
                static Producto crearProducto(String tipo) {
                    if (tipo.equals("A")) return new ProductoA();
                    if (tipo.equals("B")) return new ProductoB();
                    return null;
                }
            }

            public class Main {
                public static void main(String[] args) {
                    Producto p = Fabrica.crearProducto("A");
                    p.crear();
                }
            }
        """
    },
    {
        "titulo": "¿Cómo manejar múltiples hilos con sincronización en Java?", 
        "descripcion": "Estoy desarrollando un programa multihilo en Java y necesito sincronizar recursos compartidos entre los hilos. ¿Cuál es la forma más eficiente de hacerlo utilizando synchronized o clases del paquete java.util.concurrent?", 
        "tema": "java", "usuario_Id": 1, 
        "codigo": """
            class Contador {
                private int count = 0;

                public synchronized void incrementar() {
                    count++;
                }

                public synchronized int getCount() {
                    return count;
                }
            }

            public class Main {
                public static void main(String[] args) throws InterruptedException {
                    Contador contador = new Contador();

                    Thread t1 = new Thread(() -> {
                        for (int i = 0; i < 1000; i++) contador.incrementar();
                    });

                    Thread t2 = new Thread(() -> {
                        for (int i = 0; i < 1000; i++) contador.incrementar();
                    });

                    t1.start();
                    t2.start();
                    t1.join();
                    t2.join();

                    System.out.println("Conteo final: " + contador.getCount());
                }
            }
        """
    },
    {
        "titulo": "¿Cómo manejar Promesas anidadas en JavaScript?", 
        "descripcion": "Estoy enfrentando dificultades para manejar promesas anidadas sin que el código se vuelva difícil de leer. ¿Cómo puedo encadenar promesas correctamente y mantener un código limpio?", 
        "tema": "javascript", "usuario_Id": 1, 
        "codigo": """
            fetch('https://api.example.com/datos')
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    return fetch('https://api.example.com/mas-datos');
                })
                .then(masDatos => masDatos.json())
                .then(result => console.log(result))
                .catch(error => console.error(error));
        """
    },
    {
        "titulo": "¿Cómo implementar un debounce para mejorar el rendimiento en JavaScript?", 
        "descripcion": "Quiero limitar la cantidad de veces que una función se ejecuta en respuesta a un evento (como scroll o input). Me recomendaron usar un debounce, pero no estoy seguro de cómo implementarlo. ¿Podrían ayudarme?", 
        "tema": "javascript", "usuario_Id": 1, 
        "codigo": """
            function debounce(func, delay) {
                let timeoutId;
                return (...args) => {
                    clearTimeout(timeoutId);
                    timeoutId = setTimeout(() => func(...args), delay);
                };
            }

            const onInput = debounce(() => {
                console.log('Evento procesado');
            }, 300);

            document.getElementById('miInput').addEventListener('input', onInput);
        """
    },
    {
        "titulo": "¿Cómo usar etiquetas semánticas correctamente en HTML5?", 
        "descripcion": "Estoy aprendiendo HTML5 y me gustaría entender la importancia de las etiquetas semánticas como <article>, <section>, y <aside>. ¿Cómo ayudan al SEO y a la accesibilidad?", 
        "tema": "html", "usuario_Id": 1, 
        "codigo": """
        
        """
    },
    {
        "titulo": "¿Cómo agregar metaetiquetas para mejorar el SEO en una página HTML?", 
        "descripcion": "Estoy creando un sitio web y quiero optimizarlo para motores de búsqueda. ¿Cuáles son las metaetiquetas esenciales que debería incluir y cómo configurarlas correctamente?", 
        "tema": "html", "usuario_Id": 1, 
        "codigo": """
        
        """
    },
    {
        "titulo": "¿Cómo implementar un diseño de grilla flexible con CSS Grid?", 
        "descripcion": "Estoy intentando usar CSS Grid para crear un diseño de cuadrícula que sea responsive y se adapte a diferentes tamaños de pantalla. ¿Qué propiedades son esenciales para lograrlo?", 
        "tema": "css", "usuario_Id": 1, 
        "codigo": """
            .contenedor {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 10px;
            }        
        """
    },
    {
        "titulo": "¿Cómo implementar animaciones suaves con @keyframes en CSS?", 
        "descripcion": "Estoy buscando maneras de agregar animaciones suaves a mi página web utilizando la regla @keyframes. ¿Podrían dar un ejemplo básico de cómo hacerlo correctamente?", 
        "tema": "css", "usuario_Id": 1, 
        "codigo": """
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }

            .elemento {
                animation: fadeIn 2s ease-in-out;
            }
        """
    }
]

def insertPosts():
    _posts = Post.query.all()
    if not _posts:
        for post in posts:
            post_data = {
                "titulo": post["titulo"],
                "descripcion": post["descripcion"],
                "tema": post["tema"],
                "usuario_Id": post["usuario_Id"]
            }
            if post["codigo"] != "":
                post_data["codigo"] = post["codigo"]

            new_post = createPost(**post_data)
            print(f"Post {new_post.post_Id} creado")
        print("Posts creados")
