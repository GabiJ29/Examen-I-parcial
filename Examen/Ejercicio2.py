#Implementación para gestionar una lista de contactos
class Contacto:
    def __init__(self, nombre,numero_telefono):
        self.nombre = nombre
        self.numero_telefono = numero_telefono

class listadecontacto:
    def __init__(self):
        self.contacto = []

    def add_contacto(self, contacto):
        self.contacto.append(contacto)

    def find_contacto(self, nombre):
        for contacto in self.contacto:
            if contacto == nombre:
                return contacto
        return None

    def display_contacto(self):
        for contacto in self.contacto:
            print(f"nombre: {contacto.nombre}, numero telefono: {contacto.numero_telefono}")

# Example usage:
listadecontacto = listadecontacto()
listadecontacto.add_contacto(Contacto("Alex Huete", "85886153"))
listadecontacto.add_contacto(Contacto("Osvaldo Corrales", "78547049"))

Contacto = listadecontacto.find_contacto("Alex Huete")
if Contacto:
    print(f"Contacto found: {Contacto.nombre}, {Contacto.numero_telefono}")
else:
    print("Contacto not found")

listadecontacto.display_contacto()