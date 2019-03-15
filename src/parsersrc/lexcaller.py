import socket
import subprocess
import time


class LexCaller:
    def __init__(self):
        # sets up server to communicate between JVM and python code
        SERVER = "localhost"
        PORT = 8888

        # compiles all the java code
        # make sure you're setting up your enviromental variables up so javac is reconized in your path
        subprocess.check_call(['javac', '*.java'])
        subprocess.check_call(['javac', './lex/*.java'])
        # opens up LexServer class that interpreter will be reading from
        p = subprocess.Popen(["java", "lex/LexServer"])
        # waits a bit to let things process
        time.sleep(1)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("client: Socket created")

        self.s.connect((SERVER, PORT))
        print("client: connection complete")

    def get_line(self, lineNo):
        self.s.send("g {}\n".format(lineNo).encode())
        result = self.s.recv(1024)
        return result.decode().split()

    def get_all_data(self):
        self.s.send("a\n".encode())
        result = self.s.recv(1024)
        result = result.decode().split()

        def to_matrix(l, n):
            # beautiful code found on https://stackoverflow.com/questions/14681609/create-a-2d-list-out-of-1d-list
            return [l[i:i + n] for i in range(0, len(l), n)]

        return to_matrix(result, 2)

    def change_file(self, file):
        self.s.send("c {}\n".format(file).encode())
        result = self.s.recv(1024)
        return result.decode()

    def close_server(self):
        self.s.send("Quit\n".encode())
        result = self.s.recv(1024)
        self.s.close()
        return result.decode()


if __name__ == "__main__":
    lex = LexCaller()
    print(lex.get_all_data())
    time.sleep(10)
    lex.close_server()

