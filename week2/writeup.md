# Week 2 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **신범수** \
SUNet ID: **ShinBeomsoo** ㅏ
Citations: **None**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

## IDE

Antigravity: Gemini 3 Flash

### Exercise 1: Scaffold a New Feature
가상환경 설정 안하니까 LLM이 글로벌로 설치함.
페르소나 설정, 목표 설정, 외부 링크 참조

Prompt: 
```
role: You are a senior developer who analyzes the extract_action_items() function in @extract.py and performs its goals.
goal: Implement extract_action_items_llm(), an LLM-based construct that performs action item extraction via LLM by leveraging Ollama.
refer URL: https://ollama.com/blog/structured-outputs
use model: ollama's "mistral-nemo:12b"

Here is an example of Ollama's data extraction python code:
<code_snippet>
from ollama import chat
from pydantic import BaseModel

class Pet(BaseModel):
  name: str
  animal: str
  age: int
  color: str | None
  favorite_toy: str | None

class PetList(BaseModel):
  pets: list[Pet]

response = chat(
  messages=[
    {
      'role': 'user',
      'content': '''
        I have two pets.
        A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
        I also have a 2 year old black cat named Loki who loves tennis balls.
      ''',
    }
  ],
  model='llama3.1',
  format=PetList.model_json_schema(),
)

pets = PetList.model_validate_json(response.message.content)
print(pets)
</code_snippet>

The results of the execution are as follows.
"""
pets=[
  Pet(name='Luna', animal='cat', age=5, color='grey', favorite_toy='yarn'), 
  Pet(name='Loki', animal='cat', age=2, color='black', favorite_toy='tennis balls')
]
"""
Please refer to the URL I gave you and achieve your goal.

``` 

```
I use conda python virual environment. use conda activate cs146s. 
```

Generated Code Snippets:
```
week2/app/services/extract.py
```

### Exercise 2: Add Unit Tests
Prompt: 
```
Role: Forget about the roles you were given before. Now you're a senior developer who writes test code.
Goal: Write unit tests for `extract_action_items_llm()` covering multiple inputs (e.g., bullet lists, keyword-prefixed lines, empty input) in  @test_extract.py . Write the tests in the `@test_extract.py` file. Write them based on the inferences you made.
reasoning: What is unitest, which covers even edge cases?, How should a senior developer write unit tests?

Achieve your goals.
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```

### Exercise 3: Refactor Existing Code for Clarity
Prompt: 
```
TODO
``` 

Generated/Modified Code Snippets:
```
TODO: List all modified code files with the relevant line numbers. (We anticipate there may be multiple scattered changes here – just produce as comprehensive of a list as you can.)
```


### Exercise 4: Use Agentic Mode to Automate a Small Task
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


### Exercise 5: Generate a README from the Codebase
Prompt: 
```
TODO
``` 

Generated Code Snippets:
```
TODO: List all modified code files with the relevant line numbers.
```


## SUBMISSION INSTRUCTIONS
1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields. 
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope. 