from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Entorno import Entorno
from Simbolo.Tipo import TIPO_DATO


class If(Instruccion):
    def __init__(self, fila, columna, condicion, codigo, instruccion_else=None):
        super().__init__(fila, columna)
        self.condidcion = condicion
        self.codigo = codigo
        self.instruccion_else = instruccion_else

    def ejecutar(self, entorno):
        nuevoEntorno = Entorno("If", entorno)
        condicion = self.condidcion.ejecutar(nuevoEntorno)
        # print(f'If_ejec -> {condicion}, valor: {condicion.valor}, tipo: {condicion.tipo}')
        if condicion.tipo != TIPO_DATO.BOOL:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'La condicion no es booleana'))
            print(f'Error_If: La condición no es booleana, fila: {self.fila}, columna: {self.columna}')

        # print(f'if_eject_cond_valor: {self.codigo.sentencias}')
        print(f'ejecutar_if: {condicion.valor}')
        print(f'ejecutar_if_sent: {self.codigo.sentencias}')
        print(f'ejecutar_else: {self.instruccion_else}')
        if condicion.valor and self.codigo.sentencias is not None:
            return self.codigo.ejecutar(nuevoEntorno)
        else:
            if self.instruccion_else:
                return self.instruccion_else.ejecutar(nuevoEntorno)

    def traducir(self, entorno, C3D):
        C3D.comentario(f"Inicio If")
        resultado = None
        nuevoEntorno = Entorno("If", entorno)
        condicion = self.condidcion.traducir(nuevoEntorno, C3D)

        print(f'If: {condicion.valor} true: {condicion.true_label} false: {condicion.false_label}')

        salida = C3D.nuevo_label()
        C3D.agregar_label(condicion.true_label)
        resultado = self.codigo.traducir(nuevoEntorno, C3D)
        print(f'if resultado {resultado}')
        C3D.agregar_goto(salida)
        C3D.agregar_label(condicion.false_label)
        if self.instruccion_else:
            resultado = self.instruccion_else.traducir(nuevoEntorno, C3D)
        C3D.agregar_label(salida)
        C3D.comentario(f"Fin If")
        return None
