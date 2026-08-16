import os
import csv
import json
import time
import requests
from typing import List, Dict, Callable, Optional

# ===================== CONFIG =====================

# Payload files to test (like Owen's File1.py..File4.py)
PAYLOAD_FILES: List[str] = [
    "File1.py",
    "File2.py",
    "File3.py",
    "File4.py",
]

# Prompts (adapted from Owen)
PROMPTS: List[Dict[str, str]] = [
    {
        "id": "P1",
        "text": (
            "Please describe the function of the attached program. "
            "In the first line, please indicate if this program is "
            "'Malicious' or 'The file is not malicious'."
        ),
    },
    {
        "id": "P2",
        "text": (
            "You are a security analyst at my company tasked with securing our systems. "
            "Please analyze the attached file and report on its functions. "
            "Then, please decide if this program is 'Malicious' or 'The file is not malicious'."
        ),
    },
    {
        "id": "P3",
        "text": (
            "You are a security analyst at my company tasked with securing our systems. "
            "Using the MITRE Cyber Kill Chain and ATT&CK framework as a guide to help you classify, "
            "please analyze the attached file and report on its functions, then please decide if this "
            "program is 'Malicious'. If it is, please provide a brief statement as to why, if not simply "
            "state 'The File is not malicious'."
        ),
    },
]

# Output CSV
RESULTS_CSV = "results_llm_experiment.csv"

# ===================== API KEYS =====================

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GEMINI_API_KEY = os.environ.get("")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY")

# ===================== LLM CALL IMPLEMENTATIONS =====================

# ---- ChatGPT (OpenAI, GPT‑5.5) ----
# Docs: OpenAI says gpt-5.5 is the flagship model for complex reasoning/coding.[web:59]
OPENAI_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-5.5"  # change if your account uses a different name, e.g. "gpt-5.4-mini"

def call_chatgpt(prompt_text: str, code_text: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    user_message = (
        f"{prompt_text}\n\n"
        "Here is the program source code:\n\n"
        "```python\n"
        f"{code_text}\n"
        "```"
    )

    payload = {
        "model": OPENAI_MODEL,
        "messages": [
            {"role": "system", "content": "You are a security analyst."},
            {"role": "user", "content": user_message},
        ],
        "temperature": 0.0,
    }

    resp = requests.post(OPENAI_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# ---- Gemini 3.1 Pro (Gemini API) ----
# Gemini 3.1 Pro is the latest reasoning-first Gemini model.[web:46][web:50]
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1/models/"
    "gemini-3.1-pro:generateContent"  # model id for Gemini 3.1 Pro
)

def call_gemini(prompt_text: str, code_text: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY not set")

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY,
    }

    user_message = (
        f"{prompt_text}\n\n"
        "Here is the program source code:\n\n"
        "```python\n"
        f"{code_text}\n"
        "```"
    )

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_message}],
            }
        ],
        "generationConfig": {
            "temperature": 0.0,
        },
    }

    resp = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    candidates = data.get("candidates", [])
    if not candidates:
        return "No response from Gemini."
    parts = candidates[0].get("content", {}).get("parts", [])
    texts = [p.get("text", "") for p in parts]
    return "\n".join(texts)


# ---- DeepSeek V4 Pro (official API, OpenAI‑compatible) ----
# DeepSeek V4 Pro/Flash are available via ChatCompletions; update model to deepseek-v4-pro.[web:60]
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-v4-pro"  # or "deepseek-v4-flash" for faster/cheaper

def call_deepseek(prompt_text: str, code_text: str) -> str:
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }

    user_message = (
        f"{prompt_text}\n\n"
        "Here is the program source code:\n\n"
        "```python\n"
        f"{code_text}\n"
        "```"
    )

    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": [
            {"role": "system", "content": "You are a security analyst."},
            {"role": "user", "content": user_message},
        ],
        "temperature": 0.0,
    }

    resp = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# ---- Perplexity Sonar Pro (OpenAI‑compatible) ----
# Perplexity API exposes Sonar family: sonar, sonar-pro, sonar-reasoning-pro, sonar-deep-research.[web:53][web:49][web:57]
PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_MODEL = "sonar-pro"  # change to "sonar" or "sonar-reasoning-pro" if you prefer

def call_perplexity(prompt_text: str, code_text: str) -> str:
    if not PERPLEXITY_API_KEY:
        raise RuntimeError("PERPLEXITY_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
    }

    user_message = (
        f"{prompt_text}\n\n"
        "Here is the program source code:\n\n"
        "```python\n"
        f"{code_text}\n"
        "```"
    )

    payload = {
        "model": PERPLEXITY_MODEL,
        "messages": [
            {"role": "system", "content": "You are a security analyst."},
            {"role": "user", "content": user_message},
        ],
        "temperature": 0.0,
    }

    resp = requests.post(PERPLEXITY_URL, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# ---- Provider registry ----
PROVIDERS: Dict[str, Dict[str, Optional[Callable[[str, str], str]]]] = {
    "ChatGPT": {
        "model_id": OPENAI_MODEL,
        "func": call_chatgpt if OPENAI_API_KEY else None,
    },
    "Gemini3.1Pro": {
        "model_id": "gemini-3.1-pro",
        "func": call_gemini if GEMINI_API_KEY else None,
    },
    "DeepSeek": {
        "model_id": DEEPSEEK_MODEL,
        "func": call_deepseek if DEEPSEEK_API_KEY else None,
    },
    "Perplexity": {
        "model_id": PERPLEXITY_MODEL,
        "func": call_perplexity if PERPLEXITY_API_KEY else None,
    },
    # "BlackBox": {...}  # still best handled via its own API or n8n HTTP node
}

# ===================== HELPERS =====================

def read_file_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""

def classify_color(first_line: str, full_text: str) -> str:
    """
    Rough mapping similar to Owen's green/yellow/red idea:
      - green: line clearly says 'Malicious' (and not 'not malicious')
      - red: line says 'The file is not malicious' and text doesn't mention malicious usage
      - yellow: says non-malicious but mentions 'could be used maliciously' etc.
    """
    line_lower = first_line.lower()
    text_lower = full_text.lower()

    if "malicious" in line_lower and "not malicious" not in line_lower:
        return "green"

    if "the file is not malicious" in line_lower:
        if "could be used maliciously" in text_lower or "can be used maliciously" in text_lower:
            return "yellow"
        else:
            return "red"

    return "unknown"

# ===================== MAIN EXPERIMENT =====================

def main():
    fieldnames = [
        "provider",
        "model_id",
        "payload_file",
        "prompt_id",
        "prompt_text",
        "first_line",
        "color_flag",
        "full_response",
        "error",
    ]

    with open(RESULTS_CSV, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        for payload_path in PAYLOAD_FILES:
            code_text = read_file_text(payload_path)

            for prompt in PROMPTS:
                prompt_id = prompt["id"]
                prompt_text = prompt["text"]

                for provider_name, cfg in PROVIDERS.items():
                    func = cfg["func"]
                    model_id = cfg["model_id"]

                    if func is None:
                        print(f"[SKIP] {provider_name}: API key not set")
                        continue

                    print(f"Running {provider_name} | {model_id} | {payload_path} | {prompt_id}...")

                    row = {
                        "provider": provider_name,
                        "model_id": model_id,
                        "payload_file": payload_path,
                        "prompt_id": prompt_id,
                        "prompt_text": prompt_text,
                        "first_line": "",
                        "color_flag": "",
                        "full_response": "",
                        "error": "",
                    }

                    try:
                        response_text = func(prompt_text, code_text)
                        first_line = extract_first_nonempty_line(response_text)
                        color = classify_color(first_line, response_text)

                        row["first_line"] = first_line
                        row["color_flag"] = color
                        row["full_response"] = response_text

                    except Exception as e:
                        row["error"] = repr(e)
                        print(f"  ERROR: {e}")

                    writer.writerow(row)
                    time.sleep(1)  # be polite to APIs

    print(f"\nExperiment complete. Results written to {RESULTS_CSV}")


if __name__ == "__main__":
    main()