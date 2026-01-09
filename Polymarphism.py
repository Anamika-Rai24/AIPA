class Police:
    def work(self):
        print("Control Law & Order")
class Doctor:
    def work(self):
        print("Treatment of Patient")
class Teacher:
    def work(self):
        print("Teach Students")
xyz = [Police(),Doctor(),Teacher()]
for i in xyz:
    i.work() 
    
                          