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
        nuevoEntorno = Entorno("If", entorno)
        condicion = self.condidcion.traducir(nuevoEntorno, C3D)
        print(f'traducir_if: {condicion.valor}')
        print(f'traducir_if: {self.codigo.sentencias}')
        print(f'traducir_else: {self.instruccion_else}')

        l_true = C3D.getNuevoL()
        l_false = C3D.getNuevoL()
        l_salida = C3D.getNuevoL()
        #if condicion.valor and self.codigo.sentencias is not None:
        C3D.agregarTraduccion(f'if ({condicion.valor}) goto L{l_true};')
        C3D.agregarTraduccion(f'goto L{l_false};')
        C3D.agregarTraduccion(f'L{l_true}:')
        self.codigo.traducir(nuevoEntorno, C3D)
        C3D.agregarTraduccion(f'goto L{l_salida};')
        #else:
        if self.instruccion_else:
            C3D.agregarTraduccion(f'L{l_false}:')
            self.instruccion_else.traducir(nuevoEntorno, C3D)
        else:
            C3D.agregarTraduccion(f'L{l_false}:')
        C3D.agregarTraduccion(f'L{l_salida}:')