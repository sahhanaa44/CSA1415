const codeInput = document.getElementById("codeInput");
const compileBtn = document.getElementById("compileBtn");
const clearBtn = document.getElementById("clearBtn");
const downloadBtn = document.getElementById("downloadBtn");

const lineNumbers = document.getElementById("lineNumbers");
const charCount = document.getElementById("charCount");

const resultSummary = document.getElementById("resultSummary");
const resultTitle = document.getElementById("resultTitle");
const resultMessage = document.getElementById("resultMessage");

const tokenCount = document.getElementById("tokenCount");
const tokenTableBody = document.getElementById("tokenTableBody");

const parseTree = document.getElementById("parseTree");
const diagnosticsList = document.getElementById("diagnosticsList");


/* --------------------------------------------------
   TEST CASES
-------------------------------------------------- */

const testCases = [

    {
        id: "TC1",
        type: "Valid",
        description: "Simple assignment",
        code: `heartRate = 125;`
    },

    {
        id: "TC2",
        type: "Valid",
        description: "Conditional rule",
        code: `if temperature >= 38 then
alert = 1;
else
alert = 0;`
    },

    {
        id: "TC3",
        type: "Invalid",
        description: "Missing expression",
        code: `heartRate = ;`
    },

    {
        id: "TC4",
        type: "Invalid",
        description: "Invalid symbol",
        code: `heartRate = 125 @ 5;`
    },

    {
        id: "TC5",
        type: "Invalid",
        description: "Incomplete condition",
        code: `if temperature >= then
alert = 1;
else
alert = 0;`
    },

    {
        id: "TC6",
        type: "Invalid",
        description: "Missing semicolon",
        code: `if heartRate > 120 then
alert = 1
else
alert = 0;`
    },

    {
        id: "TC7",
        type: "Valid",
        description: "Arithmetic expression",
        code: `oxygenLevel = heartRate + 5 * 2;`
    },

    {
        id: "TC8",
        type: "Valid",
        description: "Parenthesized expression",
        code: `temperature = (38 + 2) * 2;`
    }

];


/* --------------------------------------------------
   INITIAL STATE
-------------------------------------------------- */

let lastResult = null;

updateEditorInfo();
renderTestCases();


/* --------------------------------------------------
   EDITOR
-------------------------------------------------- */

codeInput.addEventListener("input", updateEditorInfo);

codeInput.addEventListener("scroll", () => {

    lineNumbers.scrollTop = codeInput.scrollTop;

});


function updateEditorInfo() {

    const text = codeInput.value;

    charCount.textContent =
        `${text.length} characters`;

    const lines =
        text.split("\n").length;

    let numbers = "";

    for (let i = 1; i <= lines; i++) {

        numbers += i;

        if (i < lines) {
            numbers += "\n";
        }

    }

    lineNumbers.textContent = numbers;
}


/* --------------------------------------------------
   COMPILE
-------------------------------------------------- */

compileBtn.addEventListener(
    "click",
    compileCode
);


async function compileCode() {

    const source = codeInput.value;

    if (!source.trim()) {

        showInputError(
            "Please enter a PMRL rule before compiling."
        );

        return;
    }


    compileBtn.disabled = true;

    compileBtn.innerHTML =
        `Compiling <span>...</span>`;


    try {

        const response = await fetch(
            "/compile",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    source: source
                })
            }
        );


        const result =
            await response.json();


        lastResult = result;

        renderResult(result);

    }

    catch (error) {

        showInputError(
            "Unable to connect to the compiler backend."
        );

    }

    finally {

        compileBtn.disabled = false;

        compileBtn.innerHTML =
            `Compile Rule <span>→</span>`;
    }
}


/* --------------------------------------------------
   RESULT
-------------------------------------------------- */

function renderResult(result) {

    resultSummary.classList.remove(
        "neutral",
        "success",
        "error"
    );


    if (result.success) {

        resultSummary.classList.add(
            "success"
        );

        document.querySelector(
            ".result-icon"
        ).textContent = "✓";

        resultTitle.textContent =
            "Rule accepted";

        resultMessage.textContent =
            `${result.token_count} tokens generated. Syntax analysis completed successfully.`;

    }

    else {

        resultSummary.classList.add(
            "error"
        );

        document.querySelector(
            ".result-icon"
        ).textContent = "!";

        resultTitle.textContent =
            `${result.error_type || "Compilation Error"}`;

        resultMessage.textContent =
            result.errors &&
            result.errors.length
                ? result.errors[0].message
                : "The rule could not be compiled.";
    }


    renderTokens(result.tokens || []);

    renderParseTree(result.tree);

    renderDiagnostics(result.errors || []);

}


/* --------------------------------------------------
   TOKENS
-------------------------------------------------- */

function renderTokens(tokens) {

    tokenCount.textContent =
        `${tokens.length} token${tokens.length === 1 ? "" : "s"}`;


    if (!tokens.length) {

        tokenTableBody.innerHTML = `
            <tr class="empty-row">
                <td colspan="4">
                    No tokens generated.
                </td>
            </tr>
        `;

        return;
    }


    tokenTableBody.innerHTML =
        tokens.map(
            (token, index) => `

            <tr>

                <td>${index + 1}</td>

                <td>${escapeHtml(
                    token.type
                )}</td>

                <td>${escapeHtml(
                    token.value || "—"
                )}</td>

                <td>${token.position}</td>

            </tr>

        `
        ).join("");
}


/* --------------------------------------------------
   PARSE TREE
-------------------------------------------------- */

function renderParseTree(tree) {

    if (!tree) {

        parseTree.innerHTML = `
            <div class="empty-analysis">
                Parse tree unavailable.
            </div>
        `;

        return;
    }


    parseTree.innerHTML =
        renderTreeNode(
            tree,
            "",
            true,
            true
        );
}


function renderTreeNode(
    node,
    prefix,
    isLast,
    isRoot
) {

    const connector =
        isRoot
            ? ""
            : isLast
                ? "└── "
                : "├── ";


    const nodeClass =
        isRoot
            ? "tree-root"
            : "tree-label";


    let html = `

        <div class="tree-node">

            <span class="tree-branch">
                ${escapeHtml(prefix + connector)}
            </span>

            <span class="${nodeClass}">
                ${escapeHtml(node.name)}
            </span>

        </div>
    `;


    const children =
        node.children || [];


    children.forEach(
        (child, index) => {

            const childIsLast =
                index === children.length - 1;

            const childPrefix =
                isRoot
                    ? ""
                    : prefix +
                      (
                          isLast
                              ? "    "
                              : "│   "
                      );


            html += renderTreeNode(
                child,
                childPrefix,
                childIsLast,
                false
            );

        }
    );


    return html;
}


/* --------------------------------------------------
   DIAGNOSTICS
-------------------------------------------------- */

function renderDiagnostics(errors) {

    if (!errors.length) {

        diagnosticsList.innerHTML = `

            <div class="diagnostics-success">
                ✓ No lexical or syntax errors detected.
                The PMRL rule passed front-end validation.
            </div>

        `;

        return;
    }


    diagnosticsList.innerHTML =
        errors.map(
            error => `

            <div class="diagnostic">

                <div class="diagnostic-header">

                    <span class="diagnostic-type">
                        ${escapeHtml(
                            error.type
                        )}
                    </span>

                    <span class="diagnostic-position">
                        Position ${error.position}
                    </span>

                </div>

                <div class="diagnostic-message">
                    ${escapeHtml(
                        error.message
                    )}
                </div>

            </div>

        `
        ).join("");
}


/* --------------------------------------------------
   INPUT ERROR
-------------------------------------------------- */

function showInputError(message) {

    resultSummary.classList.remove(
        "neutral",
        "success"
    );

    resultSummary.classList.add(
        "error"
    );

    document.querySelector(
        ".result-icon"
    ).textContent = "!";

    resultTitle.textContent =
        "Input Error";

    resultMessage.textContent =
        message;
}


/* --------------------------------------------------
   CLEAR
-------------------------------------------------- */

clearBtn.addEventListener(
    "click",
    () => {

        codeInput.value = "";

        lastResult = null;

        updateEditorInfo();

        resultSummary.classList.remove(
            "success",
            "error"
        );

        resultSummary.classList.add(
            "neutral"
        );

        document.querySelector(
            ".result-icon"
        ).textContent = "—";

        resultTitle.textContent =
            "Awaiting compilation";

        resultMessage.textContent =
            "Run the compiler to analyze this rule.";


        tokenCount.textContent =
            "0 tokens";

        tokenTableBody.innerHTML = `
            <tr class="empty-row">
                <td colspan="4">
                    No tokens generated yet.
                </td>
            </tr>
        `;


        parseTree.innerHTML = `
            <div class="empty-analysis">
                Parse tree will appear after compilation.
            </div>
        `;


        diagnosticsList.innerHTML = `
            <div class="empty-analysis">
                No diagnostics available.
            </div>
        `;

    }
);


/* --------------------------------------------------
   DOWNLOAD REPORT
-------------------------------------------------- */

downloadBtn.addEventListener(
    "click",
    async () => {

        if (!lastResult) {

            showInputError(
                "Compile a rule before downloading the report."
            );

            return;
        }


        try {

            const response = await fetch(
                "/download-report",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        source:
                            codeInput.value,

                        result:
                            lastResult

                    })
                }
            );


            const blob =
                await response.blob();


            const url =
                window.URL.createObjectURL(blob);


            const link =
                document.createElement("a");

            link.href = url;

            link.download =
                "PMRL_Compiler_Report.txt";

            document.body.appendChild(link);

            link.click();

            link.remove();

            window.URL.revokeObjectURL(url);

        }

        catch (error) {

            showInputError(
                "Unable to generate the compilation report."
            );

        }

    }
);


/* --------------------------------------------------
   ANALYSIS TABS
-------------------------------------------------- */

document
    .querySelectorAll(".analysis-tab")
    .forEach(tab => {

        tab.addEventListener(
            "click",
            () => {

                const target =
                    tab.dataset.analysisTab;


                document
                    .querySelectorAll(".analysis-tab")
                    .forEach(item => {

                        item.classList.remove(
                            "active"
                        );

                    });


                document
                    .querySelectorAll(".analysis-content")
                    .forEach(panel => {

                        panel.classList.remove(
                            "active"
                        );

                    });


                tab.classList.add(
                    "active"
                );


                document
                    .getElementById(
                        target + "Panel"
                    )
                    .classList.add(
                        "active"
                    );

            }
        );

    });


/* --------------------------------------------------
   SIDEBAR NAVIGATION
-------------------------------------------------- */

document
    .querySelectorAll(".nav-item")
    .forEach(item => {

        item.addEventListener(
            "click",
            () => {

                const section =
                    item.dataset.section;

                const tab =
                    item.dataset.tab;


                document
                    .querySelectorAll(".nav-item")
                    .forEach(nav => {

                        nav.classList.remove(
                            "active"
                        );

                    });


                item.classList.add(
                    "active"
                );


                if (section) {

                    showSection(section);

                }


                if (tab) {

                    showSection("editor");

                    const analysisTab =
                        document.querySelector(
                            `[data-analysis-tab="${tab}"]`
                        );

                    if (analysisTab) {
                        analysisTab.click();
                    }

                }

            }
        );

    });


function showSection(section) {

    const sections = {

        editor:
            document.getElementById(
                "editorSection"
            ),

        tests:
            document.getElementById(
                "testsSection"
            ),

        grammar:
            document.getElementById(
                "grammarSection"
            ),

        operators:
            document.getElementById(
                "operatorsSection"
            )

    };


    Object.values(sections).forEach(
        element => {

            element.classList.add(
                "hidden"
            );

        }
    );


    if (sections[section]) {

        sections[section].classList.remove(
            "hidden"
        );

    }

}


/* --------------------------------------------------
   TEST CASES
-------------------------------------------------- */

function renderTestCases() {

    const grid =
        document.getElementById(
            "testCaseGrid"
        );


    grid.innerHTML =
        testCases.map(
            test => `

            <div class="test-card">

                <div class="test-card-header">

                    <span class="test-name">
                        ${test.id} · ${test.description}
                    </span>

                    <span class="test-type">
                        ${test.type}
                    </span>

                </div>

                <div class="test-code">${escapeHtml(
                    test.code
                )}</div>

                <button
                    onclick="loadTestCase('${test.id}')">
                    Load into editor
                </button>

            </div>

        `
        ).join("");
}


function loadTestCase(id) {

    const test =
        testCases.find(
            item => item.id === id
        );


    if (!test) {
        return;
    }


    codeInput.value =
        test.code;


    updateEditorInfo();

    showSection("editor");


    document
        .querySelectorAll(".nav-item")
        .forEach(nav => {

            nav.classList.remove(
                "active"
            );

        });


    document
        .querySelector(
            '[data-section="editor"]'
        )
        .classList.add(
            "active"
        );


    codeInput.focus();

}


/* --------------------------------------------------
   HTML SAFETY
-------------------------------------------------- */

function escapeHtml(value) {

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}
