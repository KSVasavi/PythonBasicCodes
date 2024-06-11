class Faculty:
    def __init__(self, name, dept, id):
        self.f_name=name
        self.depart=dept
        self.f_id=id
    def print_info(self):
        print("Faculty info.=",self.f_name,self.depart,self.f_id)
chalk=Faculty("SONU SOOD","AERONAUTICAL",404)
chalk.print_info()
class Aero_Fac(Faculty):
    pass
chalk1 = Aero_Fac("Albert Einstien","Aero_naut",10000)
chalk1.print_info()