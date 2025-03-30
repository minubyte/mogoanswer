import os
import PIL
from google import genai
from api_key import key

client = genai.Client(api_key=key)

filenames = os.listdir("ans/img")
# start = filenames.index("20240430.png")
# for filename in filenames[start+1:]:
for filename in filenames:
    img = PIL.Image.open(f"ans/img/{filename}")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=["이 이미지에서 문항 번호와 정답을 '번호,정답' 형식으로 대답해줘. 내가 요구한것 이외의 대답은 하지 말고, 만약 정답이 동그라미 안에 숫자가 써있다면 그냥 숫자만 대답.", img]
    )
    with open(f"ans/txt/{filename[:-4]}.txt", "w") as file:
        file.write(response.text)
    print(f"done: {filename}")