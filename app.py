import re
import streamlit as st

st.set_page_config(page_title="CodeInsight AI", page_icon="🤖", layout="wide")

st.title("🤖 CodeInsight AI")
st.caption("AI-assisted code review for beginners and developers")

code = st.text_area(
    "Paste Python code",
    height=360,
    placeholder="def add(a, b):\n    return a + b"
)

def review_python(source: str):
    findings = []

    if not source.strip():
        return ["Paste some Python code to start the review."]

    if "eval(" in source:
        findings.append("🔴 Security: Avoid eval() with untrusted input.")
    if "exec(" in source:
        findings.append("🔴 Security: Avoid exec() with untrusted input.")
    if re.search(r"except\s*:", source):
        findings.append("🟠 Reliability: Use specific exception types instead of bare except.")
    if "print(" in source:
        findings.append("🟡 Maintainability: Consider logging instead of print() in production code.")
    if re.search(r"for\s+\w+\s+in\s+range\(len\(", source):
        findings.append("🟡 Readability: Consider enumerate() for loops using indexes.")
    if len(source.splitlines()) > 80:
        findings.append("🟡 Maintainability: Consider splitting long code into smaller functions.")
    if not re.search(r"def\s+\w+\(", source) and len(source.splitlines()) > 15:
        findings.append("💡 Structure: Consider moving repeated logic into functions.")
    if not findings:
        findings.append("✅ No basic issues detected by the current review rules.")

    return findings

if st.button("Review Code", type="primary"):
    findings = review_python(code)
    st.subheader("Review Results")
    for item in findings:
        st.write(item)

st.divider()
st.subheader("Project")
st.write(
    "A portfolio project demonstrating Python, Streamlit, code-quality checks, "
    "prompt-oriented AI workflow design, and Git/GitHub project organization."
)
