# cs3950-project
 
Each CSV file contains a list of each prompt, temperature, and the responses.

chatmachine.py contains a set of functions that can be used to generate responses to a prompt.

graphing.ipynb and additional_graphing.ipynb contain code to call the functions in chatmachine.py and generate graphs of the results. Note that not all of the graphs are included in the paper, and that some of the notebook outputs may be from older versions of the code, so certain variables may not be defined.

misc_files contains csvs of failed attempts at generating responses.

## How to run
In your .env, set OPENAI_API_KEY to your OpenAI API key. You should be able to run graphing.ipynb and additional_graphing.ipynb without any issues.