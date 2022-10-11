import socket
import json
from postgres_api import PostgresApi

con = PostgresApi()

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8086))
    server.listen(12)
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode("utf-8")
        request = data.split(" ")[1]
        print(con.get_data(1))

        if "/put" in request:
            data = request.split(":")
            con.put_data(data[1])
            content = f"done!, string: {data[1]}, added".encode("utf-8")
        if "/list" in request:
            data = con.list_data()
            data_string = json.dumps(data)
            content = data_string.encode("utf-8")
        if "/get" in request:
            id = request.split(":")
            data = con.get_data(int(id[1]))
            data_string = json.dumps(data)
            content = data_string.encode("utf-8")


        HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")

        client_socket.send(HDRS + content)

        client_socket.shutdown(socket.SHUT_WR)




except KeyboardInterrupt:
    print("server shutdown")
    server.close()


# def request_page (request_data):
    # HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    # HDRS_404 = "HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    # response = ""

    # try:
    #     con.put_data("webtest")
    #     # with open("views"+path, "rb") as file:
    # #     with open("./views/index.html", "rb") as file:
    # #         response = file.read()
    # #     return HDRS.encode("utf-8") + response
    # except FileNotFoundError:
    #      return (HDRS_404).encode("utf-8")

if __name__ == "__main__":
    start_server()
