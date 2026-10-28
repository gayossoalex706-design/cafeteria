import web

urls = (
    '/', 'controllers.index.Index',
    '/registrar', 'controllers.registrar.Registrar',
    '/preparar', 'controllers.preparar.Preparar',
    '/cancelar', 'controllers.cancelar.Cancelar',
    '/static/(.*)', 'Static'
)

app = web.application(urls, globals())

class Static:
    def GET(self, archivo):
        try:
            with open("static/" + archivo, "rb") as f:
                return f.read()
        except FileNotFoundError:
            raise web.notfound()

if __name__ == "__main__":
    app.run()