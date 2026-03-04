import json

with open("data/technical_docs.json") as f:
    DOCS = json.load(f)


def normalize(text):
    if not text:
        return ""
    return text.strip().lower()


def retrieve_sop(product, issue):
    product = normalize(product)
    issue = normalize(issue)

    for doc_product in DOCS:
        if product in doc_product.lower():

            for doc_issue in DOCS[doc_product]:
                if issue in doc_issue.lower() or doc_issue.lower() in issue:
                    return DOCS[doc_product][doc_issue]

    return None