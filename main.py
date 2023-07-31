from gradio_client import Client
import shutil
from fastapi import FastAPI,File
from fastapi.responses import FileResponse

app = FastAPI()

def genimg(prompt):
    client = Client("https://jbilcke-hf-image-server-1.hf.space/")
    result = client.predict(
        prompt,  # str in 'Prompt' Textbox component
        "Howdy!",  # str in 'Negative prompt' Textbox component
        "Howdy!",  # str in 'Prompt 2' Textbox component
        "Howdy!",  # str in 'Negative prompt 2' Textbox component
        False,  # bool in 'Use negative prompt' Checkbox component
        False,  # bool in 'Use prompt 2' Checkbox component
        False,  # bool in 'Use negative prompt 2' Checkbox component
        0,  # int | float (numeric value between 0 and 2147483647) in 'Seed' Slider component
        1024,  # int | float (numeric value between 256 and 1024) in 'Width' Slider component
        1024,  # int | float (numeric value between 256 and 1024) in 'Height' Slider component
        20,  # int | float (numeric value between 1 and 20) in 'Guidance scale for base' Slider component
        100,  # int | float (numeric value between 1 and 20) in 'Guidance scale for refiner' Slider component
        50,  # int | float (numeric value between 10 and 100) in 'Number of inference steps for base' Slider component
        100,  # int | float (numeric value between 10 and 100) in 'Number of inference steps for refiner' Slider component
        False,  # bool in 'Apply refiner' Checkbox component
        api_name="/run"
    )

    # Use the result directly as the image path
    image_path = result
    print(result)

    # Move the image to the current working directory
    shutil.move(image_path, "image/.")

    print("Image has been stored in the current folder.")
    separated_path = result.split("/")
    print(separated_path[4])
    return separated_path[4]

path = genimg("monkey in a jungle, cold color palette, muted colors, detailed, 8k")
print(path)

@app.get("/generate-image/")
def generate_image(prompt: str):
    image_filename = genimg(prompt)
    return {"image_filename": image_filename}

@app.get("/getimage/{file_name}")
def get_image(file_name: str):
    image_path = f"image/{file_name}"
    return FileResponse(image_path)
