import web

render = web.template.render("views")

fila_normal = []
fila_prioritaria = []
preparados = 0


class Index:

    def GET(self):

        total = len(fila_normal) + len(fila_prioritaria)

        return render.index(
            fila_normal,
            fila_prioritaria,
            total,
            preparados
        )