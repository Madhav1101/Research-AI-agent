from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from tools import wiki_tool , save_to_txt
import textwrap

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


def format_research_output(res: ResearchResponse) -> str:
    wrapped_summary = textwrap.fill(res.summary, width=80)
    return f"""

Topic:
{res.topic}

Summary:
{wrapped_summary}
""".strip()

llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("human", "{query}"),
        ("human", "Wikipedia Content:\n{wiki_content}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

query = input("What can i help you with research? ")

wiki_content = wiki_tool.run(query)

response = chain.invoke({"query": query, "wiki_content": wiki_content})
print(response)

formatted_text = format_research_output(response)
save_to_txt.run(formatted_text)