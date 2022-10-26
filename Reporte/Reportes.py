lsimbolos = []
lerrores = []

lsimbolosc3d = []

loptimizacion = []


def generarReporteSimbolos():
    html = """<!doctype html>
    <html lang='es-es'>
    <head>
    	<meta charset="UTF-8">
    	<title>HTML5 Template</title>
    	<link rel="stylesheet" href="style.css">
    </head>
    <body>
    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-baqh{text-align:center;vertical-align:top}
    .tg .tg-cw9i{font-size:28px;text-align:center;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
    </style>
    <table class="tg">
    <thead>
      <tr>
        <th class="tg-cw9i" colspan="6"><span style="font-weight:bold">TABLA DE SÍMBOLOS</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="tg-amwm">Nombre</td>
        <td class="tg-amwm">Tipo Símbolo</td>
        <td class="tg-amwm">Tipo de Dato</td>
        <td class="tg-amwm">Ámbito</td>
        <td class="tg-amwm">Fila</td>
        <td class="tg-amwm">Columna</td>
      </tr>
    """

    html2 = """
    </tbody>
    </table>
    </body>
    </html>"""

    c = 1
    contenido = ""
    for simbolo in lsimbolos:
        contenido += f"""
            <tr>
        <td class="tg-baqh">{simbolo[0]}</td>
        <td class="tg-baqh">{simbolo[1]}</td>
        <td class="tg-baqh">{simbolo[2]}</td>
        <td class="tg-baqh">{simbolo[3]}</td>
        <td class="tg-baqh">{simbolo[4]}</td>
        <td class="tg-baqh">{simbolo[5]}</td>
      </tr>
    """

    data = html + contenido + html2
    with open('reporte_simbolos.html', 'w', encoding='utf-8') as f:
        f.write(data)
    lsimbolos.clear()




def generarReporteErrores():
    html = """<!doctype html>
<html lang='es-es'>
<head>
	<meta charset="UTF-8">
	<title>HTML5 Template</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-cw9i{font-size:28px;text-align:center;vertical-align:top}
.tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-cw9i" colspan="6"><span style="font-weight:bold">TABLA DE ERRORES</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-amwm">No.</td>
    <td class="tg-amwm">Descripcion</td>
    <td class="tg-amwm">Ámbito</td>
    <td class="tg-amwm">Fila</td>
    <td class="tg-amwm">Columna</td>
    <td class="tg-amwm">Fecha y Hora</td>
  </tr>
"""

    html2 = """
    </tbody>
    </table>
    </body>
    </html>"""

    c = 1
    contenido = ""
    for error in lerrores:
        contenido += f"""
        <tr>
    <td class="tg-baqh">{c}</td>
    <td class="tg-baqh">{error.mensaje}</td>
    <td class="tg-baqh">{error.ambito}</td>
    <td class="tg-baqh">{error.linea}</td>
    <td class="tg-baqh">{error.columna}</td>
    <td class="tg-baqh">{error.fechahora}</td>
  </tr>
"""

    data = html + contenido + html2
    with open('reporte_errores.html', 'w', encoding='utf-8') as f:
        f.write(data)
    lerrores.clear()


def generarReporteSimbolosC3D():
    html = """<!doctype html>
    <html lang='es-es'>
    <head>
    	<meta charset="UTF-8">
    	<title>HTML5 Template</title>
    	<link rel="stylesheet" href="style.css">
    </head>
    <body>
    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-baqh{text-align:center;vertical-align:top}
    .tg .tg-cw9i{font-size:28px;text-align:center;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
    </style>
    <table class="tg">
    <thead>
      <tr>
        <th class="tg-cw9i" colspan="6"><span style="font-weight:bold">TABLA DE SÍMBOLOS C3D</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="tg-amwm">Nombre</td>
        <td class="tg-amwm">Tipo Símbolo</td>
        <td class="tg-amwm">Tipo de Dato</td>
        <td class="tg-amwm">Ámbito</td>
        <td class="tg-amwm">Fila</td>
        <td class="tg-amwm">Columna</td>
      </tr>
    """

    html2 = """
    </tbody>
    </table>
    </body>
    </html>"""

    c = 1
    contenido = ""
    for simbolo in lsimbolosc3d:
        contenido += f"""
            <tr>
        <td class="tg-baqh">{simbolo[0]}</td>
        <td class="tg-baqh">{simbolo[1]}</td>
        <td class="tg-baqh">{simbolo[2]}</td>
        <td class="tg-baqh">{simbolo[3]}</td>
        <td class="tg-baqh">{simbolo[4]}</td>
        <td class="tg-baqh">{simbolo[5]}</td>
      </tr>
    """

    data = html + contenido + html2
    with open('reporte_simbolos_c3d.html', 'w', encoding='utf-8') as f:
        f.write(data)
    lsimbolosc3d.clear()


def generarReporteOptimizacionC3D():
    html = """<!doctype html>
    <html lang='es-es'>
    <head>
    	<meta charset="UTF-8">
    	<title>HTML5 Template</title>
    	<link rel="stylesheet" href="style.css">
    </head>
    <body>
    <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-baqh{text-align:center;vertical-align:top}
    .tg .tg-cw9i{font-size:28px;text-align:center;vertical-align:top}
    .tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
    </style>
    <table class="tg">
    <thead>
      <tr>
        <th class="tg-cw9i" colspan="6"><span style="font-weight:bold">OPTIMIZACIÓN</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="tg-amwm">Tipo de Optimizacion</td>
        <td class="tg-amwm">Regla Aplicada</td>
        <td class="tg-amwm">Expresion Original</td>
        <td class="tg-amwm">Expresion Optimizada</td>
        <td class="tg-amwm">Fila</td>
      </tr>
    """

    html2 = """
    </tbody>
    </table>
    </body>
    </html>"""

    c = 1
    contenido = ""
    for simbolo in loptimizacion:
        contenido += f"""
            <tr>
        <td class="tg-baqh">{simbolo[0]}</td>
        <td class="tg-baqh">{simbolo[1]}</td>
        <td class="tg-baqh">{simbolo[2]}</td>
        <td class="tg-baqh">{simbolo[3]}</td>
        <td class="tg-baqh">{simbolo[4]}</td>
      </tr>
    """

    data = html + contenido + html2
    with open('reporte_optimizacion_c3d.html', 'w', encoding='utf-8') as f:
        f.write(data)
    loptimizacion.clear()
