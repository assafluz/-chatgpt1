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
    prompt = 'do you think there going to be WW3?'
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


def get_last_response_prompt():
    directory = "responses"
    prompt_file = os.path.basename(__file__)
    prompt_filename = os.path.splitext(prompt_file)[0]
    last_response_file = f"{prompt_filename}_response_{response_counter - 1}.txt"
    last_response_path = os.path.join(directory, last_response_file)
    if os.path.exists(last_response_path):
        with open(last_response_path, "r") as file:
            last_response = file.read()
        last_response_lines = last_response.strip().split('\n')
        if len(last_response_lines) > 1:
            last_prompt = last_response_lines[1].strip()
            return last_prompt
    return None


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
    filename = f"{prompt_filename}_response_{response_counter}.txt"

    # Check if the prompt text has changed
    last_prompt = get_last_response_prompt()

    if last_prompt is not None and last_prompt == prompt:
        # Update the last response file
        filename = f"{prompt_filename}_response_{response_counter - 1}.txt"
    else:
        # Increment the response counter
        response_counter += 1
        filename = f"{prompt_filename}_response_{response_counter}.txt"

    # Save the story in the responses directory
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as file:
        file.write(story)

    print(f"Saved the generated story as {file_path}")
