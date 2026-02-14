class Film:
    def __init__(self, judul, gendre, negara):
        self.judul = judul
        self.gendre = gendre
        self.negara = negara

    def intro(self):
        print("happy watching")

    def end(self):
        print("thank you")

p1 = Film("the first frost", "romance", "china")
p2 = Film("drawing closer", "sad romance", "jepang")
p3 = Film("peninsula", "thriller", "korea")

print(p1.judul)
print(p2.negara)
print(p3.gendre)

p2.gendre = "action"

    

    


