import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="YOUR API KEY")

# Use recommended model
model_name = "gemini-1.5-flash"
print(f"Using model: {model_name}")

# Set up the model
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(
    model_name=model_name,
    generation_config=generation_config,
    safety_settings=safety_settings
)

def generate_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"I encountered an error: {str(e)}. Please try again later."
