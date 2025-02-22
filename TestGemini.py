from google import genai
import os

client = genai.Client(api_key="AIzaSyBV4raaOvmKKWqbXLTRv0ny9RO0rdUHQlc")
response = client.models.generate_content(
    model="gemini-2.0-pro-exp-02-05", contents="میتونی راجب زبان برنامه نویسی پایتون بهم توضیح بدی؟ فارسی بگو"
)
print(response.text)

model = "gemini-2.0-pro-exp-02-05"
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path for the output file
output_file_path = os.path.join(script_directory, f"{model}.txt")

# Write the response content to the file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(response.text)
print(f"Response saved to {output_file_path}")