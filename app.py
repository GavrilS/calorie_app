import uuid
from calorie_app import create_app, calculator

from elasticapm.contrib.flask import ElasticAPM


def main():
    app = create_app()
    app.register_blueprint(calculator.bp)

    secret_uuid = uuid.uuid4().hex
    app.secret_key = secret_uuid

    apm = ElasticAPM(app, service_name='calorie_app', debug=True)

    app.run(debug=True)


if __name__=='__main__':
    main()