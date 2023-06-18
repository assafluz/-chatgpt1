import os
import openai
from config import setup_openai_api, max_tokens, temperature
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

# Set up the OpenAI API
setup_openai_api()


def generate_story():
    prompt = 'Write a basic test plan on https://www.opencampus.xyz/ and making sure all buttons are ' \
             'clickable  using python 3 and selenium...'
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    story = response.choices[0].text.strip()
    return story


if __name__ == '__main__':
    story = generate_story()
    print("Generated Story:")
    print(story)

    # Create the directory if it doesn't exist
    directory = "myenv/Tests_Suites/tests"
    os.makedirs(directory, exist_ok=True)

    # Save the output as a Python file
    file_path = os.path.join(directory, "home_page_test_plan.py")
    with open(file_path, "w") as file:
        file.write(story)

    print(f"Saved the generated story as {file_path}")

