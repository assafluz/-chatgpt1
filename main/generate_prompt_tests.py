import os
import warnings
import openai
from urllib3.exceptions import InsecureRequestWarning
from config import setup_openai_api, temperature, max_tokens

warnings.simplefilter('ignore', InsecureRequestWarning)

# Set up the OpenAI API
setup_openai_api()

# Counter for response filenames
response_counter = 1


def generate_story():
    prompt = 'write a python test plan that goes to https://www.opencampus.xyz/ and verify it ...'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None
    )
    story = response.choices[0].text.strip()
    return story


if __name__ == '__main__':
    story = generate_story()
    # print("Generated Story:")
    # print(story)

    # Create the directory if it doesn't exist
    directory = "responses"
    os.makedirs(directory, exist_ok=True)

    # Get the name of the prompt file
    prompt_file = os.path.basename(__file__)
    prompt_filename = os.path.splitext(prompt_file)[0]

    # Generate a unique filename using the prompt name and the response counter
    filename = f"{prompt_filename}_response_{response_counter}.py"

    # Increment the response counter
    response_counter += 1

    # Save the story in the responses directory
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
        file.write(story)

    print(f"Saved the generated story as {file_path}")
