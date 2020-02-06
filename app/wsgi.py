from app import create_app

import app.const as const


application = create_app()

if __name__ == "__main__":
# def main():
    application.run(host=const.HOST,
                    port=const.PORT,
                    debug=True)
