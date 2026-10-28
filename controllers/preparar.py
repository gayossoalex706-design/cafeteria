import web

from controllers.index import fila_normal, fila_prioritaria
from controllers import index

render = web.template.render("views")


class Preparar:

    def GET(self):

        if len(fila_prioritaria) > 0:
            siguiente = fila_prioritaria[0]

        elif len(fila_normal) > 0:
            siguiente = fila_normal[0]

        else:
            siguiente = None

        return render.preparar(siguiente)

    def POST(self):

        if len(fila_prioritaria) > 0:
            fila_prioritaria.pop(0)
            index.preparados += 1

        elif len(fila_normal) > 0:
            fila_normal.pop(0)
            index.preparados += 1

        if len(fila_prioritaria) > 0:
            siguiente = fila_prioritaria[0]

        elif len(fila_normal) > 0:
            siguiente = fila_normal[0]

        else:
            siguiente = None

        return render.preparar(siguiente)