from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
from fastapi.staticfiles import StaticFiles









app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/images", StaticFiles(directory="images"), name="images")
IMAGES_FOLDER = "images"
image_filenames = os.listdir(IMAGES_FOLDER)
initial_image_filename = "img1.jpg"
current_image_index = 0

@app.get("/")
async def button(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "button": ""})



@app.post("/process_walk")
async def process_walk():
    global current_image_index

    if not image_filenames:
        raise HTTPException(status_code=500, detail="No images found")
    current_image_filename = image_filenames[current_image_index]
    current_image_index = (current_image_index + 1) % len(image_filenames)
    return JSONResponse(content={"initial_image_filename": initial_image_filename, "current_image_filename": current_image_filename})



@app.post("/process_left")
async def process_left():
    global IMAGES_FOLDER, IMAGES_FOLDER2

    # Toggle between images and images2 folders
    if IMAGES_FOLDER == "images":

        IMAGES_FOLDER = "images2"

        app.mount("/images", StaticFiles(directory=IMAGES_FOLDER), name="images")
        app.mount("/images2", StaticFiles(directory="images2"), name="images2")
    else:
        IMAGES_FOLDER = "images"
        app.mount("/images", StaticFiles(directory="images"), name="images")
        app.mount("/images2", StaticFiles(directory=IMAGES_FOLDER), name="images2")
    print("Left button clicked!")
    return JSONResponse(content={"message": "Left button clicked successfully"})




@app.post("/process_right")
async def process_punch():
    print("right button clicked!")
    return JSONResponse(content={"message": "right button clicked successfully"})

@app.post("/process_punch")
async def process_punch():
    print("punch button clicked!")
    return JSONResponse(content={"message": "punch button clicked successfully"})

@app.post("/process_togglewalk")
async def process_togglewalk():
    print("togglewalk button clicked!")
    return JSONResponse(content={"message": "togglewalk button clicked successfully"})

@app.post("/process_piss")
async def process_piss():
    print("piss button clicked!")
    return JSONResponse(content={"message": "piss button clicked successfully"})