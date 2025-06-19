from fastapi import FastAPI


def initialize_database():
    from src.database.database import Database
    Database.initialize()


def initialize_magneto_component():
    from src.magneto.magneto import Magneto
    Magneto.initialize()


def initialize_api() -> FastAPI:
    from src.api.api import API
    return API.initialize()


# initialize_database()
initialize_magneto_component()
app = initialize_api()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8194)
