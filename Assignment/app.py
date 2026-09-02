from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    make_response
)

from compiler.lexer import Lexer
from compiler.parser import Parser


app = Flask(__name__)


# ============================================================
# COMPILER
# ============================================================

def compile_rule(source):

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Remove EOF for browser display
    visible_tokens = [
        token.to_dict()
        for token in tokens
        if token.type != "EOF"
    ]

    # Lexical error
    if lexer.errors:

        return {
            "success": False,
            "tokens": visible_tokens,
            "tree": None,
            "errors": lexer.errors,
            "error_type": "Lexical Error",
            "token_count": len(visible_tokens)
        }

    # Syntax analysis
    parser = Parser(tokens)
    tree = parser.parse()

    # Syntax error
    if parser.errors:

        return {
            "success": False,
            "tokens": visible_tokens,
            "tree": tree.to_dict(),
            "errors": parser.errors,
            "error_type": "Syntax Error",
            "token_count": len(visible_tokens)
        }

    # Successful compilation
    return {
        "success": True,
        "tokens": visible_tokens,
        "tree": tree.to_dict(),
        "errors": [],
        "error_type": None,
        "token_count": len(visible_tokens)
    }


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# COMPILE
# ============================================================

@app.route("/compile", methods=["POST"])
def compile_endpoint():

    data = request.get_json()

    if not data or "source" not in data:

        return jsonify({
            "success": False,
            "errors": [{
                "type": "Input Error",
                "message": "No PMRL rule was provided.",
                "position": 0
            }]
        }), 400

    source = data["source"]

    if not source.strip():

        return jsonify({
            "success": False,
            "errors": [{
                "type": "Input Error",
                "message": "Please enter a PMRL rule.",
                "position": 0
            }]
        }), 400

    result = compile_rule(source)

    return jsonify(result)


# ============================================================
# DOWNLOAD REPORT
# ============================================================

@app.route("/download-report", methods=["POST"])
def download_report():

    data = request.get_json()

    source = data.get("source", "")
    result = data.get("result", {})

    report = generate_report(source, result)

    response = make_response(report)

    response.headers["Content-Type"] = (
        "text/plain; charset=utf-8"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=PMRL_Compiler_Report.txt"
    )

    return response


# ============================================================
# REPORT GENERATOR
# ============================================================

def generate_report(source, result):

    lines = []

    lines.append(
        "PMRL COMPILER FRONT-END ANALYSIS REPORT"
    )

    lines.append(
        "Patient Monitoring Rule Language"
    )

    lines.append("")
    lines.append("-" * 60)

    lines.append("SOURCE RULE")
    lines.append("-" * 60)
    lines.append(source)

    lines.append("")
    lines.append("LEXICAL ANALYSIS")
    lines.append("-" * 60)

    for token in result.get("tokens", []):

        lines.append(
            f"{token['type']:<15} -> {token['value']}"
        )

    lines.append("")
    lines.append("SYNTAX ANALYSIS")
    lines.append("-" * 60)

    if result.get("success"):
        lines.append("Status: ACCEPTED")
    else:
        lines.append(
            f"Status: REJECTED "
            f"({result.get('error_type', 'Error')})"
        )

    lines.append("")
    lines.append("PARSE TREE")
    lines.append("-" * 60)

    tree = result.get("tree")

    if tree:
        add_tree_to_report(
            tree,
            lines,
            "",
            True
        )
    else:
        lines.append("Parse tree unavailable.")

    errors = result.get("errors", [])

    if errors:

        lines.append("")
        lines.append("ERRORS")
        lines.append("-" * 60)

        for error in errors:

            lines.append(
                f"{error['type']}: "
                f"{error['message']} "
                f"(Position {error['position']})"
            )

    lines.append("")
    lines.append("-" * 60)

    if result.get("success"):
        lines.append(
            "FINAL RESULT: RULE ACCEPTED"
        )
    else:
        lines.append(
            "FINAL RESULT: RULE REJECTED"
        )

    lines.append("-" * 60)

    return "\n".join(lines)


def add_tree_to_report(
    node,
    lines,
    prefix,
    is_last
):

    connector = "└── " if is_last else "├── "

    lines.append(
        prefix + connector + node["name"]
    )

    children = node.get("children", [])

    new_prefix = prefix + (
        "    " if is_last else "│   "
    )

    for index, child in enumerate(children):

        last = index == len(children) - 1

        add_tree_to_report(
            child,
            lines,
            new_prefix,
            last
        )


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("PMRL Compiler Studio")
    print("Server running at http://127.0.0.1:5000")
    print()

    app.run(
        debug=True
    )