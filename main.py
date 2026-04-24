#1-misol
class Salom:
    def hello(self):
        print("Salom")

    def how_are_you(self):
        self.hello()
        print("Qalaysiz")

    def bye(self):
        self.how_are_you()
        print("Xayr")

s1 = Salom()
s1.bye()


#2-misol
class Sonlar():
    def bir(self):
        print(1)

    def ikki(self):
        self.bir()
        print(2)

    def uch(self):
        self.ikki()
        print(3)

s = Sonlar()
s.uch()

#3-misol
class Hayvon:
    def ovqat(self):
        print("Hayvon ovqat yeydi")

    def uxla(self):
        self.ovqat()
        print("Hayvon uxlaydi")

    def yur(self):
        self.uxla()
        print("Hayvon yuradi")

h = Hayvon()
h.uxla()


#4-misol
class Talaba:
    def ism(self):
        print("Menini ismim Ali")

    def yosh(self):
        self.ism()
        print("Men 20 yoshdaman")

    def kurs(self):
        self.yosh()
        print("Men 2-kursman")

t = Talaba()
t.ism()


#5-misol
class Moshina:
    def start(self):
        print("Mashina ishga tushdi")

    def drive(self):
        self.start()
        print("Moshina harakatlandi")

    def stop(self):
        self.drive()
        print("Moshina to'xtadi")

m = Moshina()
m.drive()
