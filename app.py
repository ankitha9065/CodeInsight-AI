import re
import streamlit as st

st.set_page_config(
    page_title="CodeInsight AI",
    page_icon="🤖",
    layout="wide"
)

# ---------- HEADER ----------

st.title("🤖 CodeInsight AI")
st.caption("AI-assisted Python code review and developer insights")

st.divider()


# ---------- CODE REVIEW ----------

def review_python(source: str):
    findings = []

    if not source.strip():
        return [
            {
                "severity": "INFO",
                "category": "Input",
                "message": "Paste some Python code to start the review."
            }
        ]

    # Security checks
    if "eval(" in source:
        findings.append({
            "severity": "HIGH",
            "category": "Security",
            "message": "Avoid eval() with untrusted input."
        })

    if "exec(" in source:
        findings.append({
            "severity": "HIGH",
            "category": "Security",
            "message": "Avoid exec() with untrusted input."
        })

    # Reliability checks
    if re.search(r"except\s*:", source):
        findings.append({
            "severity": "MEDIUM",
            "category": "Reliability",
            "message": "Use specific exception types instead of a bare except."
        })

    # Maintainability checks
    if "print(" in source:
        findings.append({
            "severity": "LOW",
            "category": "Maintainability",
            "message": "Consider using logging instead of print() in production code."
        })

    # Readability checks
    if re.search(r"for\s+\w+\s+in\s+range\(len\(", source):
        findings.append({
            "severity": "LOW",
            "category": "Readability",
            "message": "Consider enumerate() when looping through indexes."
        })

    # Long code check
    if len(source.splitlines()) > 80:
        findings.append({
            "severity": "LOW",
            "category": "Maintainability",
            "message": "Consider splitting long code into smaller functions."
        })

    # Structure check
    if not re.search(r"def\s+\w+\(", source) and len(source.splitlines()) > 15:
        findings.append({
            "severity": "LOW",
            "category": "Structure",
            "message": "Consider moving repeated logic into functions."
        })

    if not findings:
        findings.append({
            "severity": "GOOD",
            "category": "Code Quality",
            "message": "No basic issues detected by the current review rules."
        })

    return findings


# ---------- CODE INPUT ----------

st.subheader("📝 Python Code")

code = st.text_area(
    "Paste your Python code below",
    height=320,
    placeholder="""def divide(a, b):
    try:
        return eval(a) / b
    except:
        print("Error")"""
)


# ---------- REVIEW ----------

if st.button("🔍 Review Code", type="primary"):

    findings = review_python(code)

    st.divider()
    st.subheader("📊 Review Summary")

    high = sum(1 for x in findings if x["severity"] == "HIGH")
    medium = sum(1 for x in findings if x["severity"] == "MEDIUM")
    low = sum(1 for x in findings if x["severity"] == "LOW")
    good = sum(1 for x in findings if x["severity"] == "GOOD")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🔴 High", high)
    col2.metric("🟠 Medium", medium)
    col3.metric("🟡 Low", low)
    col4.metric("🟢 Good", good)

    st.divider()

    st.subheader("🔎 Detailed Findings")

    for finding in findings:

        severity = finding["severity"]
        category = finding["category"]
        message = finding["message"]

        if severity == "HIGH":
            st.error(f"🔴 **{category}** — {message}")

        elif severity == "MEDIUM":
            st.warning(f"🟠 **{category}** — {message}")

        elif severity == "LOW":
            st.info(f"🟡 **{category}** — {message}")

        elif severity == "GOOD":
            st.success(f"🟢 **{category}** — {message}")

        else:
            st.write(f"ℹ️ **{category}** — {message}")


# ---------- ABOUT ----------

st.divider()

with st.expander("ℹ️ About CodeInsight AI"):

    st.write(
        """
        CodeInsight AI is a Python code review assistant that identifies
        common security, reliability, readability, and maintainability
        issues.

        The project demonstrates Python programming, Streamlit application
        development, automated code analysis, and AI-assisted developer
        tooling.
        """
    )