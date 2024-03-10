
class Curso:
    nombre:None
    semestre:None
    students:None
    codigo_curso:None
    def __init__(self,nombre,semestre):
        self.nombre=nombre
        self.semestre=semestre
        self.codigo_curso=self.generarCodigo()
        self.students=[]
        print("se registro el curso",self.nombre)
    def generarCodigo(self):
        return (self.nombre[:3]+"-"+str(self.semestre)).upper()

    def agregarStudent(self,student):
        self.students.append(student)

    def verStudents(self):
        for item in self.students:
            print(item)

    def __str__(self):
        return f"curso {self.nombre} con codigo {self.codigo_curso}"

class Student:
    nombre:None
    nivel:None
    correo:None
    codigo_stdudent:None
    notas:None
    cursos:None
    def __init__(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo
        self.nivel=0
        self.codigo_stdudent=self.generarCodigo()
        self.cursos=[]
        self.notas=[]
        print("el estudiante fue registrad@")
    def __str__(self):
        return f"estudiante {self.nombre} con correo {self.correo} con codigo {self.codigo_stdudent}"

    def generarCodigo(self):
        return '20244979A'

    def inscribirseCurso(self,curso):
        self.cursos.append(curso)
        pass

    def verCursosInscritos(self):
        for (item,key) in enumerate(self.cursos):
            print(f"{key}-{item}")

    def verNotas(self):
        for item in self.notas:
            print(item)


class Profesor:
    nombre:None
    Cursos:None
    def __init__(self,nombre):
        self.nombre=nombre
        self.cursos=[]

    def agregarCurso(self,curso):
        self.cursos.append(curso)
    
    def asignarNotas(self):
        for item in self.cursos:
            for item2 in item.students:
                while True:
                    try:
                        nota=float(input("ingrese la nota:"))
                    except Exception as e:
                        print(e)
                    else:
                        if nota>0 and nota<=20:
                            item2.nota=nota
                            break
                        else:
                            print("ingresar una nota mayor a 0 y menor a 20")
                            continue

student1=Student('Joauqin chunga','jchung@gmail.com')
student2=Student('Daniel Cajo','dcajo@gmail.com')

#print(student1)
#print(student2) 


curso1=Curso("Python",202402)
#print(curso1)
curso2=Curso("SQL",202401)
#print(curso2)


student1.inscribirseCurso(curso1)
curso1.agregarStudent(student1)

student1.verCursosInscritos()
curso1.verStudents()

profesor1=Profesor('profesorx')
profesor1.agregarCurso(curso1)

profesor1.asignarNotas()
