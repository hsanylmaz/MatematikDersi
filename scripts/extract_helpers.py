#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pathlib import Path

def extract_existing_raw_sections(html_path: Path):
    """Mevcut HTML dosyasından EXTRA_QUESTIONS JS dizisini ve Mini Check görevlerini çeker."""
    if not html_path.exists():
        return None, None
    text = html_path.read_text(encoding="utf-8")

    # EXTRA_QUESTIONS JS kodunu çek
    extra_questions_raw = None
    sm = "const EXTRA_QUESTIONS = ["
    em = "];"
    start = text.find(sm)
    if start != -1:
        end = text.find(em, start)
        if end != -1:
            extra_questions_raw = text[start + len("const EXTRA_QUESTIONS = "):end + 1].strip()

    # Mini tasks çek
    mini_cards = re.findall(r'<article class="mini-check-card"[^>]*>(.*?)</article>', text, re.DOTALL)
    mini_tasks = []
    for idx, card_body in enumerate(mini_cards):
        tag_m = re.search(r'<div class="mono"[^>]*>MİNİ GÖREV \d+ • (.*?)</div>', card_body)
        q_m = re.search(r'<h3[^>]*>(.*?)</h3>', card_body, re.DOTALL)
        opts = re.findall(r'<button[^>]*data-mini="\d+"[^>]*data-correct="(true|false)"[^>]*>(.*?)</button>', card_body)

        tag = tag_m.group(1).strip() if tag_m else f"MİNİ TEST {idx+1}"
        q_text = " ".join(q_m.group(1).split()) if q_m else "Soru"
        options = [{"label": opt_text.strip(), "correct": corr == "true"} for corr, opt_text in opts]

        mini_tasks.append({
            "id": idx + 1,
            "tag": tag,
            "question": q_text,
            "options": options
        })

    return extra_questions_raw, (mini_tasks if len(mini_tasks) == 3 else None)
