import web

from controllers.index import fila_normal, fila_prioritaria

render = web.template.render("views")


class Cancelar:

    def GET(self):
        return render.cancelar()

    def POST(self):

        datos = web.input()
        numero = datos.numero

        for pedido in fila_prioritaria:
            if pedido["numero"] == numero:
                fila_prioritaria.remove(pedido)
                raise web.seeother("/")

        for pedido in fila_normal:
            if pedido["numero"] == numero:
                fila_normal.remove(pedido)
                raise web.seeother("/")

        raise web.seeother("/")