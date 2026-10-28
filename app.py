import web

urls = (
    '/', 'controllers.index.Index',
    '/registrar', 'controllers.registrar.Registrar',
    '/preparar', 'controllers.preparar.Preparar',
    '/cancelar', 'controllers.cancelar.Cancelar'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()