# grab the uploaded pdf and parse into chunks

from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain


# TODO: Add support for batch uploads
# NOTE: might break if PDF is scanned image - fix later


def summarize_pdf(pdf_path, simulate=False):
    if simulate:
        return "📝 Simulated summary: Neural networks process info through layers of perceptrons..."

    # real LangChain pipeline
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Load summarize chain (GPT required below)
    chain = load_summarize_chain(OpenAI(temperature=0), chain_type="map_reduce")
    summary = chain.run(documents)

    return summary

if __name__ == "__main__":
    print(summarize_pdf("sample_notes.pdf", simulate=True))
