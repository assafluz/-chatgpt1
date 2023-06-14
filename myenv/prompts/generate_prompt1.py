import openai
import os
from config import setup_openai_api, max_tokens, temperature
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

# Set up the OpenAI API
setup_openai_api()


def generate_story():
    prompt = 'Write a story on 2 friends...'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    story = response.choices[0].message.content.strip()
    return story


if __name__ == '__main__':
    story = generate_story()
    print("Generated Story:")
    print(story)

    # Create the directory if it doesn't exist
    directory = "myenv/responses"
    os.makedirs(directory, exist_ok=True)

    # Generate a unique filename using a UUID
    filename = f"response_{os.urandom(16).hex()}.txt"

    # Save the story in the responses directory
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
        file.write(story)

    print(f"Saved the generated story as {file_path}")
