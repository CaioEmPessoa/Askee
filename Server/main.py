from dotenv import load_dotenv
from flask_openapi3 import OpenAPI, Info, Contact
from controllers import apis, blueprints

load_dotenv()

info = Info(
    title="Askee API",
    version="1.0.0",
    description="API do forum Askee",
    contact=Contact(name="Askee Team")
)

app = OpenAPI(__name__, info=info)

for api in apis:
    app.register_api(api)

for bp in blueprints:
    app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
