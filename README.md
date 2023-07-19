# langchain-demo
Demo LLM application using LangChain, Bedrock and Kendra

## Installation
We recommend to use Conda to make sure you run this in an isolated environment. 

```bash
conda deactivate
conda env create -f environment.yml
conda activate langchain-aws-demo
```

## Running the sample
The sample uses boto3 to connect with the Bedrock and Kendra service. Please ensure that your AWS credentials are setup 
and your default profile have access to both Bedrock and Kendra services. Also, have the Kendra Index Id from the AWS
Kendra console handy and update it in the `app.py` file.

```bash
python app.py "What is Amazon Kendra?"
```
