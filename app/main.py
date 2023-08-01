import uvicorn

from mangum import Mangum

from init_app import create_app


app = create_app()
handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run(app, env_file='.env')

