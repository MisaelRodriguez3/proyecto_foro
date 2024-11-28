from src.models import Example
from src.service import createExample

examples = [
    {
        "titulo": "Calculadora de números primos",
        "descripcion": "Código en Python para identificar si un número ingresado por el usuario es primo.",
        "tema": "python",
        "usuario_Id": 1,
        "codigo": """
            def es_primo(numero):
                if numero < 2:
                    return False
                for i in range(2, int(numero ** 0.5) + 1):
                    if numero % i == 0:
                        return False
                return True

            numero = int(input('Ingresa un número: '))
            if es_primo(numero):
                print(f'{numero} es un número primo.')
            else:
                print(f'{numero} no es un número primo.')
        """
    },    
    {
        "titulo": "Gestión de archivos JSON",
        "descripcion": "Código en Python que lee y escribe datos en un archivo JSON.",
        "tema": "python",
        "usuario_Id": 1,
        "codigo": """
            import json

            data = {"nombre": "John", "edad": 30, "ciudad": "New York"}

            # Guardar datos en un archivo JSON
            with open("datos.json", "w") as archivo:
                json.dump(data, archivo)

            # Leer datos de un archivo JSON
            with open("datos.json", "r") as archivo:
                contenido = json.load(archivo)
                print(contenido)
        """
    },
    {
        "titulo": "Programa para calcular el área de un círculo",
        "descripcion": "Código en Java que solicita el radio de un círculo y calcula su área.",
        "tema": "java",
        "usuario_Id": 1,
        "codigo": """
            import java.util.Scanner;

            public class AreaCirculo {
                public static void main(String[] args) {
                    Scanner scanner = new Scanner(System.in);
                    System.out.print("Ingresa el radio del círculo: ");
                    double radio = scanner.nextDouble();
                    double area = Math.PI * Math.pow(radio, 2);
                    System.out.println("El área del círculo es: " + area);
                }
            }
        """
    },
    {
        "titulo": "Conversión de Celsius a Fahrenheit",
        "descripcion": "Código en Java para convertir temperaturas de grados Celsius a Fahrenheit.",
        "tema": "java",
        "usuario_Id": 1,
        "codigo": """
            import java.util.Scanner;

            public class CelsiusAFahrenheit {
                public static void main(String[] args) {
                    Scanner scanner = new Scanner(System.in);
                    System.out.print("Ingresa la temperatura en Celsius: ");
                    double celsius = scanner.nextDouble();
                    double fahrenheit = (celsius * 9/5) + 32;
                    System.out.println("La temperatura en Fahrenheit es: " + fahrenheit);
                }
            }
        """
    },
    {
        "titulo": "Validación de correos electrónicos",
        "descripcion": "Código en JavaScript que valida si un correo electrónico tiene un formato correcto.",
        "tema": "javascript",
        "usuario_Id": 1,
        "codigo": """
            function validarCorreo(correo) {
                const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return regex.test(correo);
            }

            const correo = "ejemplo@dominio.com";
            console.log(validarCorreo(correo) ? "Correo válido" : "Correo no válido");
        """
    },
    {
        "titulo": "Contador regresivo dinámico",
        "descripcion": "Código en JavaScript que muestra un contador regresivo en la consola.",
        "tema": "javascript",
        "usuario_Id": 1,
        "codigo": """
            function contadorRegresivo(segundos) {
                let contador = segundos;
                const intervalo = setInterval(() => {
                    console.log(contador);
                    contador--;
                    if (contador < 0) {
                        clearInterval(intervalo);
                        console.log("¡Tiempo terminado!");
                    }
                }, 1000);
            }

            contadorRegresivo(10);
        """
    },
    {
        "titulo": "Formulario de contacto",
        "descripcion": "Ejemplo de un formulario HTML para enviar mensajes de contacto.",
        "tema": "html",
        "usuario_Id": 1,
        "codigo": """
            <form action="/submit" method="post">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required>
                
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="mensaje" required></textarea>
                
                <button type="submit">Enviar</button>
            </form>
        """
    },
    {
        "titulo": "Tabla de precios",
        "descripcion": "Código en HTML que muestra una tabla con los precios de productos.",
        "tema": "html",
        "usuario_Id": 1,
        "codigo": """
            <table>
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Precio</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Manzana</td>
                        <td>$1.00</td>
                    </tr>
                    <tr>
                        <td>Banana</td>
                        <td>$0.50</td>
                    </tr>
                </tbody>
            </table>
        """
    },
    {
        "titulo": "Botón con efecto hover",
        "descripcion": "Código CSS que crea un efecto al pasar el cursor sobre un botón.",
        "tema": "css",
        "usuario_Id": 1,
        "codigo": """
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                cursor: pointer;
            }

            button:hover {
                background-color: #45a049;
            }
        """
    },
    {
        "titulo": "Efecto gradiente en fondo",
        "descripcion": "Código CSS para aplicar un degradado como fondo de una página.",
        "tema": "css",
        "usuario_Id": 1,
        "codigo": """
            body {
                background: linear-gradient(to right, #ff7e5f, #feb47b);
                height: 100vh;
                margin: 0;
            }
        """
    }    
]

def insertExamples():
    _examples = Example.query.all()
    if not _examples:
        for example in examples:
            new_example = createExample(
                titulo=example["titulo"],
                descripcion=example["descripcion"],
                tema=example["tema"],
                usuario_Id=example["usuario_Id"],
                codigo=example["codigo"]
            )
            print(f"Ejemplo {new_example.ejemplo_Id} creado")
        print("ejemplos creados")