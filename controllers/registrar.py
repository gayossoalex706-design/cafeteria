import web

from controllers.index import fila_normal, fila_prioritaria

render = web.template.render("views")


class Registrar:

    def GET(self):
        return render.registrar()

    def POST(self):

        datos = web.input()

        pedido = {
            "numero": datos.numero,
            "cliente": datos.cliente,
            "producto": datos.producto,
            "cantidad": datos.cantidad,
            "prioridad": datos.prioridad,
            "tiempo": datos.tiempo
        }

        if datos.prioridad == "Prioritario":
            fila_prioritaria.append(pedido)
        else:
            fila_normal.append(pedido)

        raise web.seeother("/")