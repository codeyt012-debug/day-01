from lumaai import LumaAI
import base64

# Initialize Luma client
client = LumaAI(api_key="YOUR_API_KEY_HERE")

# Send text prompt to Luma AI
response = client.generations.create(
    prompt="Hello! This is my Day 1 voice agent speaking."
)

# Print the result
print(response)
