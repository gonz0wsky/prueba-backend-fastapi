""" db """
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

def init_routes(app: FastAPI) -> None:
    """ Initialize routes """

    @app.get("/graphql", response_class=HTMLResponse)
    async def sandbox(request: Request):
        return templates.TemplateResponse("sandbox.html", {"request": request})
