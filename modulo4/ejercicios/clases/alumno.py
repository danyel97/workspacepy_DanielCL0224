from datetime import datetime as dt
class Alumno:
    def __init__(self,nombre,dni,nivel,especialidad) -> None:
        self.nombre=nombre
        self.dni=dni
        self.nivel=nivel
        self.especialidad=especialidad
        self.codigo=self.generarCodigo()
        pass
    def generarCodigo(self):
        now=dt.now()
        semestre=None
        year=now.year
        month=now.month
        if month<7:
            semestre=1
        else:
            semestre=2
        codigo=str(year)+str(semestre)+self.dni
        return codigo
    def __str__(self) -> str:
        return f'{self.codigo},{self.nombre},{self.nivel},{self.especialidad}\n'