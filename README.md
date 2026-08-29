# AI Friend or Foe?

## A Experimental Evaluation for LLM-Based Malware Classification Under Adversarial Payload Transformations

> **M.Tech Dissertation Research Project**

This repository contains the research materials, experimental payloads, transformation outputs, automation prototype, diagrams, documentation, and supporting files associated with the dissertation **"AI Friend or Foe? A Benchmarking Framework for Evaluating LLM-Based Malware Classification Under Adversarial Payload Transformations."**

The project evaluates how five Large Language Model (LLM) platforms respond to malware-like payloads when their visibility is progressively reduced through **identifier renaming, Base92 encoding, and AES encryption**. The study also includes a **benign AES control** to examine false-positive behaviour.

---

# ⚠️ IMPORTANT SECURITY AND RESPONSIBLE USE DISCLAIMER

## READ THIS BEFORE USING OR DOWNLOADING ANY PAYLOAD

**THE FILES IN THIS REPOSITORY MAY CONTAIN MALWARE-LIKE CODE, MALICIOUS CODE SAMPLES, OBFUSCATED CONTENT, ENCODED PAYLOADS, ENCRYPTED PAYLOADS, OR OTHER SECURITY-RELEVANT MATERIAL.**

These materials were prepared and collected **strictly for controlled academic cybersecurity research and malware-classification experiments**.

### DO NOT:

* ❌ Execute any payload on a personal, production, or institutional system.
* ❌ Deploy any payload against systems, networks, devices, accounts, or services that you do not own or have explicit authorization to test.
* ❌ Use the payloads to obtain unauthorized access.
* ❌ Use the materials to damage systems, steal information, deploy malware, disrupt services, or conduct unauthorized security testing.
* ❌ Remove, weaken, or bypass security controls for malicious purposes.
* ❌ Modify the samples for deployment against real targets.
* ❌ Treat these samples as safe software simply because they are included in an academic repository.

### RECOMMENDED RESEARCH ENVIRONMENT

If you need to inspect or reproduce any experiment involving the payloads, use an **isolated and controlled laboratory environment** with appropriate security precautions.

Researchers should understand the behaviour of a sample before handling it and should avoid connecting experimental malware-like samples to production networks or systems containing sensitive information.

### PURPOSE OF THIS REPOSITORY

The payloads are provided to support:

* Academic research
* Malware-analysis research
* LLM evaluation
* Cybersecurity education
* Reproducibility of the dissertation experiments
* Future research into AI-assisted malware classification

**The repository is not intended to provide operational malware, attack infrastructure, or instructions for compromising real systems.**

By accessing or using the materials in this repository, you acknowledge that you are responsible for using them lawfully, ethically, and only within an environment where you have appropriate authorization.

---

# 📌 Project Overview

Generative AI has introduced new possibilities in cybersecurity. While AI systems can assist defenders with code analysis and malware classification, they may also be misused to assist in generating or modifying malicious code.

This research investigates the defensive side of this problem:

> **Can LLMs reliably classify malware-like payloads when the visibility of the underlying payload is progressively reduced?**

The experiment evaluates payloads under multiple visibility conditions:

```text
Plain Payload
      ↓
Identifier Renaming
      ↓
Base92 Encoding
      ↓
AES Encryption
```

The study compares the behaviour of five LLM platforms under different prompt conditions and examines both their final classifications and their explanations.

---

# 🔬 Research Scope

The project evaluates:

* **5 LLM platforms**

  * ChatGPT
  * Google Gemini
  * Perplexity
  * DeepSeek
  * BlackBox AI

* **Multiple malware-like payload categories**

* **Multiple programming languages**

  * Python
  * Java
  * C++
  * Shell scripting

* **3 prompt strategies**

  * Basic Classification Prompt
  * Security Analyst Context Prompt
  * MITRE ATT&CK Guided Prompt

* **4 main payload visibility conditions**

  * Plain
  * Obfuscated
  * Base92 Encoded
  * AES Encrypted

* **Benign AES Control**

  * Used to observe false-positive behaviour when encrypted content is non-malicious.

The dissertation describes the experimental methodology, test cases, evaluation criteria, results, limitations, and future enhancements in detail.

---

# 🧪 Experimental Methodology

The experimental workflow was:

```text
Payload Preparation
        ↓
Prompt Selection
        ↓
Payload Transformation
        ↓
LLM Submission
        ↓
Response Collection
        ↓
Classification
        ↓
Quantitative & Qualitative Analysis
        ↓
Comparison of LLM Behaviour
```

## The quantitative and qualitative evaluation approach was inspired by the work of **Owen Slubowski**. The prompt structure was also adapted from previous research and modified for the requirements of this experiment.

# 📁 Repository Contents

Every file associated with the research project is included in this repository where appropriate.

A typical repository structure is:

```text
AI-Friend-or-Foe/
│
├── README.md
│
├── Codes/
│     ├── AES_Key_Gen.py (AES_Key_Generator)
      ├── main.py ( Main Program )
      ├── obfuscation.py ( Identifier Renaming Program)
│
├── AES_Key.txt (Which contains key to decrypt the payloads {to verify})
│
├── Safe_Payloads_Used/
│   ├── Plain/
│   ├── Obfuscated/
│   ├── Base92/
│   ├── AES/
│ 
│
└── AI Friend or Foe Dissertation Paper (PDF)
```

> **Note:** The exact folders and filenames may differ depending on how the repository is organized. The purpose of this section is to make the research material easy for future researchers to navigate.

---

# 🤖 Automation Prototype

The project also includes an **automation prototype** developed to explore how the experimental workflow could eventually be automated.

The prototype was designed to:

1. Read payload files.
2. Select the required prompt.
3. Submit requests to supported LLM APIs.
4. Collect model responses.
5. Extract the initial verdict.
6. Assign a classification category.
7. Save results for further analysis.

The prototype was **not used to generate the final experimental results**. The final experiments were performed manually through the LLM platforms because of API costs, token limitations, request limits, model availability differences, and platform restrictions.

The prototype is therefore provided as a **research starting point for future development**, rather than as a fully validated automated benchmarking platform.

---

# 📊 Evaluation

The project records LLM responses using a classification notation consisting of:

| Classification | Meaning                           |
| -------------- | --------------------------------- |
| 🟢 Green       | Malicious                         |
| 🟡 Yellow      | Potentially malicious / dual-use  |
| 🔴 Red         | Not malicious                     |
| 🟠 Grey        | Refused, unclear, or inconclusive |

The study also examines qualitative characteristics such as:

* Explanation quality
* Suspicious behaviour identification
* Dual-use recognition
* Misclassification
* Refusal behaviour
* Indirect reasoning
* Reliance on encoded or encrypted structure
* Threat-intelligence-style reasoning

The evaluation framework was based on an approach inspired by previous research, particularly Owen Slubowski's work.

---

# 📚 Research Foundation

This project builds upon previous research in AI-assisted malware analysis.

In particular, the work of **Owen Slubowski** provided an important foundation for this dissertation. The present research extends that direction by examining additional payload categories, multiple LLM platforms, progressively concealed payloads, and additional experimental conditions.

The dissertation also incorporates existing security frameworks and techniques such as:

* MITRE ATT&CK
* Cyber Kill Chain
* Base92 encoding
* AES encryption
* CyberChef

These technologies and frameworks are used as part of the research methodology rather than being claimed as original inventions of this project.

---

# 🧑‍🔬 Contribution to Future Research

This repository is intended to make the project useful beyond the completion of the dissertation.

Researchers and students are encouraged to:

* Study the experimental methodology.
* Reproduce the experiments in a controlled environment.
* Improve the automation prototype.
* Add additional LLM platforms.
* Add additional payload categories.
* Add additional programming languages.
* Expand the benign control dataset.
* Improve the evaluation methodology.
* Add dynamic malware-analysis capabilities.
* Improve result collection and visualization.
* Investigate newer LLM versions.

## The dissertation itself identifies automated testing, larger datasets, additional LLM platforms, and integration with static and dynamic malware analysis as potential future directions.

# 🤝 Contributions

**Contributions are welcome.**

If you are a cybersecurity researcher, student, developer, or security enthusiast, you can contribute by improving the research framework or prototype.

Possible contributions include:

* Improving the Python automation prototype.
* Improving the n8n workflow.
* Adding support for additional LLM APIs.
* Improving error handling and rate-limit handling.
* Adding automated result collection.
* Improving CSV/Excel/database output.
* Adding additional test cases.
* Improving documentation.
* Adding reproducibility tools.
* Developing better visualization of experimental results.

When contributing, please ensure that all work remains focused on **authorized, defensive, and academic cybersecurity research**.

---

# ⚠️ Responsible Research

This repository should be treated as a **cybersecurity research laboratory resource**.

The presence of a payload in this repository does **not** imply that it is safe to execute.

Researchers should:

1. Work in an isolated laboratory.
2. Use systems dedicated to security research where possible.
3. Avoid exposing experimental samples to production networks.
4. Avoid using real credentials or sensitive information.
5. Obtain authorization before testing against any external system.
6. Follow applicable laws, institutional policies, and responsible disclosure practices.

---

# 📖 Dissertation

The complete dissertation contains the detailed methodology, experimental design, system analysis, system design, implementation discussion, testing results, evaluation, conclusion, and future enhancements.

The full dissertation is available in this repository for **academic and research reference**.

---

# 📄 Research Paper

The associated research paper is also included in the repository.

Please refer to the published paper for the condensed version of the research and the complete dissertation for the detailed experimental work.

---

# ⭐ For Future Researchers

This project is intended to be a **starting point**, not a finished solution.

LLMs evolve rapidly. Their capabilities, safety mechanisms, APIs, and classification behaviour can change over time. Therefore, experimental results obtained from one model version should not automatically be assumed to apply to future versions.

Future researchers are encouraged to reproduce the experiments with newer models and larger, more representative datasets.

---

# ⚖️ Legal and Ethical Notice

This repository is provided **for educational, academic, and authorized cybersecurity research purposes only**.

The author does not authorize or encourage the use of the materials contained in this repository for unauthorized access, disruption, data theft, malware deployment, evasion of security controls, or any other unlawful activity.

Users are solely responsible for ensuring that their use of this repository complies with applicable laws, regulations, institutional policies, and authorization requirements.

**Use responsibly. Research ethically. Test only where you have permission.**

---

# 📬 Contact

For questions, research collaboration, corrections, or suggestions, please use the contact information provided in the GitHub profile associated with this repository.

---

## ⭐ Acknowledgement

This research was inspired in part by the work of **Owen Slubowski, CISSP**, particularly his research into AI-assisted malware analysis.

The purpose of this repository is to build upon existing research and provide a foundation that **future researchers can reproduce, critique, improve, and extend**.

---

**If this repository is useful to your research, consider ⭐ starring the repository and contributing improvements for future researchers.**
