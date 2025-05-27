import streamlit as st
import re

st.set_page_config(page_title="Code2Visuals", layout="wide")
st.title("🧠 Code2Visuals — Turn Code Into Mnemonics with Images")

st.markdown("""
Paste your code snippet below. We'll extract keywords and show fun + professional icons to help you **remember it visually**.
""")

# --- Sample visual dictionary ---
visual_dict = {
    # Existing entries
    "class":      ("🏫", "Think of a class as a classroom"),
    "def":        ("🔧", "Function is a tool"),
    "encode":     ("🔐", "Encoding means securing"),
    "decode":     ("🔓", "Decoding means unlocking"),
    "List":       ("📋", "List of items or checklist"),
    "str":        ("🧵", "Thread = string"),
    "sizes":      ("📏", "Sizes like using a ruler"),
    "res":        ("📦", "Result stored in a box"),
    "for":        ("🔁", "Loop through values"),
    "return":     ("🔙", "Return to caller"),
    "if":         ("🔀", "Conditional branch"),
    "cloud":      ("☁️", "Cloud like OneDrive"),
    "file":       ("🗂️", "Documents or folders"),
    "auto":       ("🛺", "Auto-rickshaw"),
    "optimize":   ("⚙️", "Optimize = tuning"),
    "compact":    ("📦", "Compact = compressed box"),
    "stream":     ("🌊", "Data stream"),
    "delta":      ("🔺", "Delta symbol"),
    "checkpoint": ("🚩", "Checkpoint flag"),

    # Additional Python keywords
    "and":        ("🤝", "Logical AND"),
    "or":         ("🔀", "Logical OR"),
    "not":        ("🚫", "Logical NOT"),
    "in":         ("📍", "Value exists in collection"),
    "is":         ("🆔", "Identity comparison"),
    "lambda":     ("🧮", "Anonymous function"),
    "with":       ("🤝", "Context manager"),
    "try":        ("🧪", "Attempt block"),
    "except":     ("❗", "Exception handler"),
    "finally":    ("🔚", "Final block"),
    "while":      ("🔁", "Loop while condition is true"),
    "break":      ("🛑", "Exit loop"),
    "continue":   ("⏭️", "Skip to next iteration"),
    "pass":       ("⏸️", "Do nothing"),
    "yield":      ("🍃", "Yield value from generator"),
    "global":     ("🌐", "Global scope"),
    "nonlocal":   ("🏘️", "Non-local scope"),
    "assert":     ("✅", "Assert condition"),
    "del":        ("🗑️", "Delete object"),
    "import":     ("📦", "Import module"),
    "from":       ("📤", "Import from module"),
    "as":         ("🎭", "Alias for module"),
    "raise":      ("⚠️", "Raise exception"),
    "async":      ("⏳", "Asynchronous function"),
    "await":      ("⏱️", "Await result"),

    # Common C/C++/Java keywords
    "int":        ("🔢", "Integer type"),
    "float":      ("🌊", "Floating-point number"),
    "double":     ("💧", "Double precision float"),
    "char":       ("🔤", "Character type"),
    "void":       ("🕳️", "No return value"),
    "static":     ("📌", "Static variable or method"),
    "public":     ("🌐", "Public access modifier"),
    "private":    ("🔒", "Private access modifier"),
    "protected":  ("🛡️", "Protected access modifier"),
    "new":        ("✨", "Instantiate new object"),
    "delete":     ("❌", "Delete object"),
    "this":       ("👈", "Current object reference"),
    "super":      ("🦸", "Superclass reference"),
    "switch":     ("🔄", "Switch statement"),
    "case":       ("📂", "Case in switch"),
    "default":    ("🔧", "Default case"),
    "do":         ("▶️", "Do loop"),
    "enum":       ("🔢", "Enumeration type"),
    "struct":     ("🏗️", "Structure"),
    "union":      ("🔗", "Union of types"),
    "typedef":    ("📝", "Type definition"),
    "sizeof":     ("📏", "Size of type"),
    "goto":       ("➡️", "Go to label"),
    "const":      ("🔒", "Constant value"),
    "volatile":   ("⚡", "Volatile variable"),
    "register":   ("🗃️", "Register storage"),
    "extern":     ("🌍", "External linkage"),
    "inline":     ("📎", "Inline function"),
    "break":      ("🛑", "Break loop"),
    "continue":   ("⏭️", "Continue loop"),
    "return":     ("🔙", "Return from function"),
    "try":        ("🧪", "Try block"),
    "catch":      ("🎣", "Catch exception"),
    "finally":    ("🔚", "Finally block"),
    "throw":      ("🎯", "Throw exception"),
    "throws":     ("🎯", "Throws exception"),
    "interface":  ("🔌", "Interface definition"),
    "implements": ("🛠️", "Implements interface"),
    "extends":    ("📏", "Extends class"),
    "package":    ("📦", "Package declaration"),
    "import":     ("📥", "Import package"),
    "instanceof": ("🔍", "Instance check"),
    "abstract":   ("🧩", "Abstract class or method"),
    "synchronized": ("🔒", "Synchronized block"),
    "transient":  ("🚫", "Transient field"),
    "final":      ("🏁", "Final variable or method"),
    "native":     ("🌐", "Native method"),
    "strictfp":   ("📐", "Strict floating point"),
    "super":      ("🦸", "Superclass reference"),
    "this":       ("👈", "Current object reference"),
    "void":       ("🕳️", "No return value"),
    "volatile":   ("⚡", "Volatile variable"),
    "assert":     ("✅", "Assert condition"),
    "enum":       ("🔢", "Enumeration type"),
    "instanceof": ("🔍", "Instance check"),
    "goto":       ("➡️", "Go to label"),
    "const":      ("🔒", "Constant value"),
    "null":       ("🚫", "Null reference"),
    "true":       ("✔️", "Boolean true"),
    "false":      ("❌", "Boolean false"),
}


# --- Step 1: Input box for code ---
code_input = st.text_area("📥 Paste your code here:", height=300, placeholder="Paste Python / Spark / SQL snippet...")

# --- Step 2: Extract keywords ---
def extract_keywords(text):
    tokens = re.findall(r"[a-zA-Z_]+", text)
    return list(set(tokens))  # unique keywords

if code_input:
    keywords = extract_keywords(code_input)

    st.subheader("🧠 Visual Memory Aids")
    found = False

    cols = st.columns(4)
    i = 0

    for word in keywords:
        if word in visual_dict:
            emoji, hint = visual_dict[word]
            with cols[i % 4]:
                st.markdown(f"### {emoji} `{word}`")
                st.caption(hint)
            i += 1
            found = True

    if not found:
        st.warning("❌ No known keywords found. Try adding words like `auto`, `cloud`, `def`, `delta` etc.")

---

## ✅ `requirements.txt`

```txt
streamlit
