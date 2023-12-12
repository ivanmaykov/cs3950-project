from textblob import TextBlob
from openai import OpenAI
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_chat_response(prompt, temperature=1, model="gpt-3.5-turbo"):
    """Returns a response from the openAI chat api.

    Args:
        prompt (str): A prompt you wish to get a response for
        temperature (int, optional): dictates how creative the AI will be. ranges from 0 to 2, numbers above 1.5 are messy. Defaults to 1.
        model (str, optional): The model you wish to use. Defaults to "gpt-3.5-turbo".

    Returns:
        response: a json-like response including the response, number of token used, etc.
    """
    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response

def run_array(prompt, temp_list=[0, 0.2, 0.5, 0.8, 1, 1.2, 1.5]):
    """Runs a prompt through the get_chat_response, with varying temperatures.

    Args:
        prompt (str): a prompt to the openAI chat API.
        temp_list (list, optional): A list of temperatures. Defaults to [0, 0.2, 0.5, 0.8, 1, 1.2, 1.5].

    Returns:
        response_list: a list of responses from the api
        temp_list: the temperatures used for each of the responses
    """
    response_list = []

    for temp in temp_list:
        response = get_chat_response(prompt, temp)
        response_list.append(response.choices[0].message.content)
    
    return response_list, temp_list


def build_prompt(prompt, **kwargs):
    """Generates a list of modified prompts by replacing placeholders in the base prompt with provided replacements.

    Args:
        prompt (str): the base promp string, containing placeholders for the kwargs.
        **kwargs: Keyword arguments where each key is a placeholder in the base prompt and its value is a list of strings to replace the placeholder.


    Returns:
        list: A list of strings, where each string is a variation of the base prompt. 

    Example:
        base_prompt = "I like to eat <food> and <drink>."
        replacements = {"<food>": ["apples", "bananas"], "<drink>": ["water", "juice"]}
        prompts = build_prompt(base_prompt, **replacements)
        # Result: ["I like to eat apples and water.", "I like to eat apples and juice.",
        #         "I like to eat bananas and water.", "I like to eat bananas and juice."]
    """
    if not kwargs:
        return [prompt]

    prompts = [prompt]
    for key, replacements in kwargs.items():
        if key not in prompt:
            continue

        new_prompts = []
        for replacement in replacements:
            for p in prompts:
                new_prompts.append(p.replace(key, replacement))

        prompts = new_prompts

    return prompts


def analyze_sentiment(text):
    """Returns the sentiment, polarity, and subjectivity of thje given text

    Args:
        text (str): a string of which to analyze

    Returns:
        sentiment, polarity, subjectivity: the sentiment (positive, negative, neutral), the polarity score (-1: extremely negative, +1: extremely positive), and subjectivity (0: factual, 1: emotional)
    """
    blob = TextBlob(text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    return polarity, subjectivity

def batch_sentiment(response_list):
    """runs a list of reponses through the analyze_sentiment function

    Args:
        response_list (list): a list of responses, in strings.

    Returns:
        polarity_list, subjectivity_list: lists of the polarity.
    """
    polarity_list, subjectivity_list = [], []
    for response in response_list:
        polarity, subjectivity = analyze_sentiment(response)
        polarity_list.append(polarity)
        subjectivity_list.append(subjectivity)

    return polarity_list, subjectivity_list

def create_chart(df, title):
    """Creates a heatmap of the given dataframe, with x-axis as temperature, y-axis as prompt, and color as polarity.

    Args:
        df (DataFrame): A Dataframe containing the polarity of each prompt at each temperature.
        title (str): The title of the chart.
    """

    df.set_index('prompt', inplace=True)

    # Creating a heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, cmap='coolwarm')
    plt.title(f"Heatmap of {title} at Various Temperatures")
    plt.xlabel("Temperature")
    plt.ylabel("Prompt")
    plt.show()

