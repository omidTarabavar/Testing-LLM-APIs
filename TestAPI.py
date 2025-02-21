import os
from openai import OpenAI


def saveResponse(model_name, response_content):
    # Determine the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the path for the output file
    output_file_path = os.path.join(script_directory, f"{model_name}.txt")

    # Write the response content to the file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(response_content)
    print(f"Response saved to {output_file_path}")


def test_model(model):
    # Initialize the OpenAI client
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    # Define the model identifier
    model_identifier = model

    # Create a chat completion request
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>",      # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model=model_identifier,
        messages=[
            {
                "role": "user",
                "content": "میتونی راجب زبان برنامه نویسی پایتون بهم توضیح بدی؟ فارسی بگو"
            }
        ]
    )
    # Extract the response content
    response_content = completion.choices[0].message.content

    # Extract the model name from the identifier
    # Replace slashes and colons to make it a valid filename
    model_name = model_identifier.split('/')[-1].replace(':', '_')

    saveResponse(model_name, response_content)

models = [
    "cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    "cognitivecomputations/dolphin3.0-mistral-24b:free",
    "mistralai/mistral-small-24b-instruct-2501:free",
    "deepseek/deepseek-r1-distill-llama-70b:free",
    "deepseek/deepseek-r1:free",
    "sophosympatheia/rogue-rose-103b-v0.2:free",
    "deepseek/deepseek-chat:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "nvidia/llama-3.1-nemotron-70b-instruct:free",
    "meta-llama/llama-3.2-1b-instruct:free",
    "meta-llama/llama-3.1-8b-instruct:free",
    #"mistralai/mistral-nemo:free",
    "google/gemma-2-9b-it:free",
    "mistralai/mistral-7b-instruct:free",
    "microsoft/phi-3-mini-128k-instruct:free",
    "microsoft/phi-3-medium-128k-instruct:free",
    "meta-llama/llama-3-8b-instruct:free",
    "openchat/openchat-7b:free",
    "undi95/toppy-m-7b:free",
    "huggingfaceh4/zephyr-7b-beta:free",
    "gryphe/mythomax-l2-13b:free"
]

#for i in range(len(models)):
#    test_model(models[i])