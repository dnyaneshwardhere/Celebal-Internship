# prepare.py
from langchain_core.documents import Document
from load import load_loan_data

def create_documents():
    df = load_loan_data()
    documents = []

    for _, row in df.iterrows():
        content = (
            f"Loan_ID: {row['Loan_ID']}, Gender: {row['Gender']}, Married: {row['Married']}, "
            f"Dependents: {row['Dependents']}, Education: {row['Education']}, "
            f"Self_Employed: {row['Self_Employed']}, ApplicantIncome: {row['ApplicantIncome']}, "
            f"CoapplicantIncome: {row['CoapplicantIncome']}, LoanAmount: {row['LoanAmount']}, "
            f"Loan_Amount_Term: {row['Loan_Amount_Term']}, Credit_History: {row['Credit_History']}, "
            f"Property_Area: {row['Property_Area']}, Loan_Status: {row['Loan_Status']}"
        )
        documents.append(Document(page_content=content))

    return documents
