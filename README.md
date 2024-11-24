# Decisify

Decisify is a Python package that leverages generative AI to explain decisions made by optimization models. 

## Introduction

Mathematical optimization is a critical tool in operations research, enabling businesses to make data-driven decisions that maximize efficiency and minimize costs. However, the complexity of these models often makes it difficult for stakeholders to understand and trust the decisions being made. 

Decisify addresses this challenge by using generative AI to provide clear, understandable explanations for the decisions produced by optimization models. By enhancing transparency and trust, Decisify aims to drive greater adoption of optimization techniques across diverse industries.

## Features

- Explain optimization model decisions using generative AI
- Improve transparency and trust in operations research
- Facilitate the adoption of optimization techniques in various industries

## Installation

You can install Decisify using pip:

```bash
pip install decisify
```

## Usage

Here's a simple example of how to use Decisify:

```python
import decisify

# Your optimization model code here
(1) Just define the Pydantic Models for (a) Input (b) Output
(2) Concrete implementation of optimization model
(3) A method to read, the solution
```

Now, you are read to use decisify, its simple from this point onwards


```python
# Generate explanations for the model's decisions
trnsprt_model = TransportationModel()
solution = trnsprt_model.get_solution(input_data)
print(solution.model_dump_json())
interrogator = GurobiInterrogator(trnsprt_model, input_data)
answer = interrogator.answer("What is the optimal solution for the transportation problem?")
print(answer)
answer = interrogator.answer("How many factories and how many distribution centers are there?")
print(answer)
#Now, lets assume the user wants to change the supply at warehouse W1 to 20
answer = interrogator.what_if("the courier company just doubled the transportation costs, how does this affect the total cost?")
print(answer)
answer = interrogator.what_if("The demand at customer C1 has increased by 100 times, how does this affect the total cost?")
print(answer)
```

## Contributing

We welcome contributions to Decisify! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact us at support@decisify.ai.
