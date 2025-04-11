from calorie_app import create_app, calculator


def main():
    app = create_app()
    app.register_blueprint(calculator.bp)

    app.run(debug=True)


if __name__=='__main__':
    main()