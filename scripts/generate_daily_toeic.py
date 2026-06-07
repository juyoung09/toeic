from __future__ import annotations

import argparse
import json
import random
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")

QUESTION_BANK = [
    {
        "part": "Part 5",
        "skill": "prepositions",
        "prompt": "The accounting team asked employees ___ all travel receipts by Friday.",
        "choices": {"A": "for", "B": "to", "C": "about", "D": "with"},
        "answer": "B",
        "explanation": "ask + someone + to do something is the correct structure.",
        "focus": ["receipt", "travel expense", "deadline"],
    },
    {
        "part": "Part 5",
        "skill": "word form",
        "prompt": "The new software update will be installed ___ after the office closes.",
        "choices": {"A": "automatic", "B": "automate", "C": "automatically", "D": "automation"},
        "answer": "C",
        "explanation": "An adverb is needed to modify the verb phrase 'will be installed'.",
        "focus": ["software update", "install", "office closes"],
    },
    {
        "part": "Part 5",
        "skill": "tense",
        "prompt": "By the time the client arrives, the proposal ___ by the design team.",
        "choices": {"A": "completed", "B": "will have been completed", "C": "has completed", "D": "completing"},
        "answer": "B",
        "explanation": "Future perfect passive fits an action completed before a future time.",
        "focus": ["proposal", "client", "design team"],
    },
    {
        "part": "Part 5",
        "skill": "conjunctions",
        "prompt": "The seminar was postponed ___ the speaker had a scheduling conflict.",
        "choices": {"A": "because", "B": "although", "C": "unless", "D": "so that"},
        "answer": "A",
        "explanation": "The second clause gives the reason for the postponement.",
        "focus": ["postpone", "speaker", "scheduling conflict"],
    },
    {
        "part": "Part 5",
        "skill": "relative clauses",
        "prompt": "The technician ___ repaired the printer will return tomorrow to inspect the scanner.",
        "choices": {"A": "whose", "B": "whom", "C": "who", "D": "which"},
        "answer": "C",
        "explanation": "'Who' is the subject of the relative clause referring to a person.",
        "focus": ["technician", "repair", "inspect"],
    },
    {
        "part": "Part 5",
        "skill": "vocabulary",
        "prompt": "The company will ___ a new training program for all supervisors next month.",
        "choices": {"A": "launch", "B": "depart", "C": "observe", "D": "retain"},
        "answer": "A",
        "explanation": "'Launch' means to start or introduce a new program or product.",
        "focus": ["training program", "supervisor", "launch"],
    },
    {
        "part": "Part 5",
        "skill": "comparatives",
        "prompt": "This year's customer survey was ___ detailed than last year's version.",
        "choices": {"A": "many", "B": "more", "C": "most", "D": "much"},
        "answer": "B",
        "explanation": "Use 'more + adjective + than' for comparative forms of many longer adjectives.",
        "focus": ["survey", "detailed", "version"],
    },
    {
        "part": "Part 5",
        "skill": "articles",
        "prompt": "The warehouse manager ordered ___ additional scanner for the shipping desk.",
        "choices": {"A": "a", "B": "an", "C": "the", "D": "no article"},
        "answer": "B",
        "explanation": "'Additional' starts with a vowel sound, so 'an' is used before it.",
        "focus": ["warehouse", "scanner", "shipping desk"],
    },
    {
        "part": "Part 5",
        "skill": "subject-verb agreement",
        "prompt": "The list of approved vendors ___ updated every quarter.",
        "choices": {"A": "are", "B": "were", "C": "is", "D": "have been"},
        "answer": "C",
        "explanation": "The subject is singular: 'the list', not 'vendors'.",
        "focus": ["vendor", "approved", "quarter"],
    },
    {
        "part": "Part 5",
        "skill": "phrasal verbs",
        "prompt": "Please ___ the attached invoice before forwarding it to the finance department.",
        "choices": {"A": "look up", "B": "look over", "C": "look after", "D": "look into"},
        "answer": "B",
        "explanation": "'Look over' means to review or inspect something briefly.",
        "focus": ["invoice", "forward", "finance department"],
    },
    {
        "part": "Part 6",
        "skill": "sentence insertion",
        "prompt": "Memo: We have updated the visitor policy. Employees must register guests at least 24 hours before arrival. ___ Security badges will be prepared in advance.",
        "choices": {"A": "This will allow reception staff to confirm each appointment.", "B": "The cafeteria will be closed during renovations.", "C": "Several employees requested new parking spaces.", "D": "The invoice was sent last week."},
        "answer": "A",
        "explanation": "Choice A connects visitor registration with reception and security preparation.",
        "focus": ["visitor policy", "register", "security badge"],
    },
    {
        "part": "Part 7",
        "skill": "inference",
        "prompt": "Notice: The 3 P.M. product demonstration has been moved from Room 204 to the main auditorium because attendance is higher than expected. What can be inferred?",
        "choices": {"A": "The demonstration was canceled.", "B": "More people plan to attend than originally anticipated.", "C": "Room 204 is being renovated.", "D": "The event will begin earlier."},
        "answer": "B",
        "explanation": "The room changed because expected attendance increased.",
        "focus": ["demonstration", "auditorium", "attendance"],
    },
]

VOCAB_BANK = [
    {"word": "allocate", "meaning": "to assign or set aside resources", "example": "The manager allocated more staff to the urgent project."},
    {"word": "amend", "meaning": "to change or correct a document", "example": "The contract was amended after legal review."},
    {"word": "audit", "meaning": "a formal inspection of records", "example": "The annual audit will begin on Monday."},
    {"word": "compliance", "meaning": "following rules or standards", "example": "The policy ensures compliance with safety regulations."},
    {"word": "courier", "meaning": "a delivery service or person", "example": "The documents were sent by courier."},
    {"word": "delegate", "meaning": "to assign a task to another person", "example": "Supervisors should delegate routine tasks."},
    {"word": "dispatch", "meaning": "to send something to a destination", "example": "The replacement parts were dispatched yesterday."},
    {"word": "inventory", "meaning": "goods held in stock", "example": "The warehouse inventory is checked weekly."},
    {"word": "mandatory", "meaning": "required", "example": "Attendance at the safety briefing is mandatory."},
    {"word": "negotiate", "meaning": "to discuss terms and reach an agreement", "example": "The vendor negotiated a lower delivery fee."},
    {"word": "overdue", "meaning": "late or past the deadline", "example": "Several payments are now overdue."},
    {"word": "procurement", "meaning": "the process of obtaining supplies", "example": "Procurement approved the equipment purchase."},
    {"word": "reimburse", "meaning": "to pay someone back", "example": "The company will reimburse travel expenses."},
    {"word": "relocate", "meaning": "to move to another place", "example": "The branch office will relocate in July."},
    {"word": "renewal", "meaning": "an extension of a contract or license", "example": "The license renewal is due next week."},
    {"word": "shipment", "meaning": "goods sent for delivery", "example": "The shipment arrived ahead of schedule."},
    {"word": "shortage", "meaning": "a lack of something needed", "example": "A supply shortage delayed production."},
    {"word": "specification", "meaning": "a detailed requirement", "example": "The device meets all technical specifications."},
    {"word": "tentative", "meaning": "not final or confirmed", "example": "The meeting date is still tentative."},
    {"word": "warranty", "meaning": "a written guarantee", "example": "The printer includes a two-year warranty."},
]


def parse_run_date(value: str | None) -> date:
    if value:
        return date.fromisoformat(value)
    return datetime.now(KST).date()


def build_pack(run_date: date) -> dict:
    rng = random.Random(run_date.toordinal())
    questions = rng.sample(QUESTION_BANK, 8)
    vocabulary = rng.sample(VOCAB_BANK, 12)

    numbered_questions = []
    for index, question in enumerate(questions, start=1):
        item = dict(question)
        item["number"] = index
        numbered_questions.append(item)

    return {
        "date": run_date.isoformat(),
        "timezone": "Asia/Seoul",
        "generated_at": f"{run_date.isoformat()}T06:00:00+09:00",
        "summary": {
            "question_count": len(numbered_questions),
            "vocabulary_count": len(vocabulary),
            "target_minutes": 35,
        },
        "questions": numbered_questions,
        "vocabulary": vocabulary,
    }


def render_markdown(pack: dict) -> str:
    lines = [
        f"# TOEIC Daily Study Result - {pack['date']}",
        "",
        "## Today",
        "",
        f"- Questions: {pack['summary']['question_count']}",
        f"- Vocabulary: {pack['summary']['vocabulary_count']}",
        f"- Target time: {pack['summary']['target_minutes']} minutes",
        "",
        "## Questions",
        "",
    ]

    for question in pack["questions"]:
        lines.extend(
            [
                f"### {question['number']}. {question['part']} - {question['skill']}",
                "",
                question["prompt"],
                "",
            ]
        )
        for key, value in question["choices"].items():
            lines.append(f"- {key}. {value}")
        lines.extend(["", f"Focus: {', '.join(question['focus'])}", ""])

    lines.extend(["## Answer Key", ""])
    for question in pack["questions"]:
        lines.extend(
            [
                f"{question['number']}. {question['answer']} - {question['explanation']}",
                "",
            ]
        )

    lines.extend(["## Vocabulary", "", "| Word | Meaning | Example |", "|---|---|---|"])
    for vocab in pack["vocabulary"]:
        lines.append(f"| {vocab['word']} | {vocab['meaning']} | {vocab['example']} |")

    lines.extend(
        [
            "",
            "## Study Log",
            "",
            "- Score: ",
            "- Missed questions: ",
            "- Words to review: ",
            "- One-sentence reflection: ",
            "",
        ]
    )
    return "\n".join(lines)


def render_index(reports_dir: Path) -> str:
    report_files = sorted(path for path in reports_dir.glob("*.md") if path.name != "README.md")
    lines = ["# TOEIC Daily Reports", ""]
    if not report_files:
        lines.append("No reports generated yet.")
    else:
        for path in reversed(report_files[-90:]):
            lines.append(f"- [{path.stem}]({path.name})")
    lines.append("")
    return "\n".join(lines)


def write_outputs(root: Path, pack: dict) -> None:
    reports_dir = root / "reports"
    data_dir = root / "data" / "results"
    reports_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    run_date = pack["date"]
    report_path = reports_dir / f"{run_date}.md"
    json_path = data_dir / f"{run_date}.json"
    latest_path = data_dir / "latest.json"
    index_path = reports_dir / "README.md"

    report_path.write_text(render_markdown(pack), encoding="utf-8")
    json_text = json.dumps(pack, ensure_ascii=False, indent=2) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    latest_path.write_text(json_text, encoding="utf-8")
    index_path.write_text(render_index(reports_dir), encoding="utf-8")

    print(f"Wrote {report_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {latest_path}")
    print(f"Wrote {index_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a daily TOEIC study result.")
    parser.add_argument("--date", default="", help="KST date to generate, in YYYY-MM-DD format.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    run_date = parse_run_date(args.date.strip() or None)
    pack = build_pack(run_date)
    write_outputs(root, pack)


if __name__ == "__main__":
    main()
