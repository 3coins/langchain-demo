from sys import argv
from langchain import PromptTemplate
from langchain.llms import Bedrock
from langchain.retrievers import AmazonKendraRetriever
from langchain.chains import RetrievalQA

def main(query: str):
    prompt_template = """{context}
    
    Please answer the question \"{question}\" based on the text above. Be descriptive, but not overly long. Don't add anything that's not included in the text above. If the answer to the question is not contained in the above text, respond "I don't know the answer based on the text provided".
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    kendra_index_id = "<kendra-index-id>"
    retriever = AmazonKendraRetriever(
        index_id=kendra_index_id
    )

    llm = Bedrock(
        model_id="amazon.titan-tg1-large",
        verbose=True
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        verbose=True,
        chain_type_kwargs={
            "prompt": PROMPT
        }
    )

    return chain(query)

if __name__ == "__main__":
    response = main(argv[1:][0])
    if response.get("result"):
        print(response["result"])
    else:
        print("Could not answer the question based on provided text.")