from config import Config
from src import run_server

server = run_server(Config)

if __name__ == "__main__":
    server.run()