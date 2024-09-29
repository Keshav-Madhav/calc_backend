from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post("")
async def run(image_data: ImageData):
    img = base64.b64decode(image_data.image.split(",")[1])
    img_bytes = BytesIO(img)
    image = Image.open(img_bytes)
    responses = analyze_image(image, dict_of_vars=image_data.dict_of_vars)
    data = []
    for response in responses:
      data.append(response)

    print(response)
    return {
      "message": "Image processed successfully.",
      "type": "success",
      "data": data
    }