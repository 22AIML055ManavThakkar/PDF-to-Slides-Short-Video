import re

def is_heading(line):
    return (
        len(line.split()) <= 4
        and line.isupper() or line.istitle()
    )

def get_key_points(text, max_points=6):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    sections = []

    current_title = None
    current_content = []

    for line in lines:
        if is_heading(line):
            if current_title and current_content:
                sections.append((current_title, " ".join(current_content)))
            current_title = line
            current_content = []
        else:
            current_content.append(line)

    if current_title and current_content:
        sections.append((current_title, " ".join(current_content)))

    # ✅ If we found real sections, use them
    if len(sections) >= 2:
        return sections[:max_points]

    # 🔁 FALLBACK: chunk-based (for unstructured PDFs)
    chunks = []
    current = []
    for line in lines:
        current.append(line)
        if sum(len(l.split()) for l in current) >= 120:
            chunks.append(("Overview", " ".join(current)))
            current = []

    if current:
        chunks.append(("Overview", " ".join(current)))

    return chunks[:max_points]


def make_slide_content(title, content):
    words = content.split()

    bullet1 = " ".join(words[:12])
    bullet2 = " ".join(words[12:24])

    narration = " ".join(words[:30])

    return title.title(), [bullet1, bullet2], narration

