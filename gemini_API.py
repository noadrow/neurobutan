from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

def send_content(response,new_obs):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=str(response)+str(new_obs))
    print(response.text)
    return response.text



