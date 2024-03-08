class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price}, {self.description}, {self.quantity}"

    def __repr__(self):
        return (f"{type(self).__name__}(name ={self.name}, price={self.price},"
                f" description={self.description}, quantity={self.quantity})")

    def addProduct(self):
        with open("prodotti.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(", ")[0] == self.name:
                    self.quantity = self.quantity + int(line.split(", ")[4])
                    lines.pop(lines.index(line))
                    break
        with open("prodotti.txt", "w", encoding='utf-8') as file:
            output = []
            for line in lines:
                output.append(line)
            output.append(f"{self.__str__()}\n")
            for line in output:
                file.write(line)

    def modifyProduct(self, price, description, quantity):
        with open("prodotti.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(", ")[0] == self.name:
                    self.quantity = self.quantity + int(line.split(", ")[4])
                    lines.pop(lines.index(line))
                    break
        self.price = price
        self.description = description
        self.quantity = quantity
        with open("prodotti.txt", "w", encoding='utf-8') as file:
            output = []
            for line in lines:
                output.append(line)
            output.append(f"{self.__str__()}\n")
            for line in output:
                file.write(line)


class Client:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.email}, {self.address}"

    def __repr__(self):
        return f"{type(self).__name__}(name = {self.name}, email = {self.email}, address = {self.address})"

    def addClient(self):
        client_control = False
        with open("clienti.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(", ")[0] == self.name and line.split(", ")[1] == self.email:
                    client_control = True
        if client_control is False:
            with open("clienti.txt", "w", encoding='utf-8') as file:
                output = []
                for line in lines:
                    output.append(line)
                output.append(f"{self.__str__()}\n")
                for line in output:
                    file.write(line)

    def removeClient(self):
        with open("clienti.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.split(", ")[0] == self.name and line.split(", ")[1] == self.email:
                    lines.remove(line)
                    break
        with open("clienti.txt", "w", encoding='utf-8') as file:
            for line in lines:
                file.write(line)

    def modifyClient(self, name, email, address):
        self.removeClient()
        self.name = name
        self.email = email
        self.address = address
        self.addClient()
