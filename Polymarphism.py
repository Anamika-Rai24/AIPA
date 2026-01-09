class Police:
    def work(self):
        print("Control Law & Order")
class Doctor:
    def work(self):
        print("Treatment of Patient")
class Teacher:
    def work(self):
        print("Teach Students")
pqr = [Police(),Doctor(),Teacher()]
for i in pqr:
    i.work() 
    

                          
