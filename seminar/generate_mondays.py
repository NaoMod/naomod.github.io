import datetime
from pathlib import Path
import random
from string import Template


def on_day(date: datetime.date, day: int):
    """
    Returns the date of the next given weekday after
    the given date. For example, the date of next Monday.

    NB: if it IS the day we're looking for, this returns 0.
    consider then doing onDay(foo, day + 1).
    """
    days = (day - date.weekday() + 7) % 7
    return date + datetime.timedelta(days=days)


def find_next_monday(date: datetime.date):
    return on_day(date, 0)


def generate_event_file(date: datetime.date, speaker: str):
    next_monday: datetime.date = find_next_monday(date)
    file_name = str(next_monday) + "-" + speaker + ".md"
    output_file: Path = output_dir / file_name
    output_file.write_text(template.substitute(speaker=speaker))
    print("Created " + str(output_file))


############
# Input data
############
start_date: datetime.date = datetime.date(2024, 9, 23)
output_dir: Path = Path("./seminar/2425/_posts")
speakers: list[str] = [
    "Gerson Sunyé",
    "Massimo Tisi",
    "Erwan Bousse",
    "Hugo Bruneliere",
    "Théo Le Calvar",
    "Jean-Marie Mottu",
    "Dalila Tamzalit",
    "Hiba Ajabri",
    "Ali Benjilany",
    "Matthew Coyle",
    "Yasmina Dali Youcef",
    "James Miranda",
]
random.shuffle(speakers)
extra_dates: int = 5

############
# Preparations
############
output_dir.mkdir(parents=True, exist_ok=True)
example_file: Path = Path("./seminar/talk_template.md")
if not example_file.exists():
    raise Exception("Missing example file at location " + str(example_file))

template: Template = Template(example_file.read_text())

############
# Loop
############
current_date = find_next_monday(start_date + datetime.timedelta(days=1))

for speaker in speakers:
    generate_event_file(current_date, speaker)
    current_date = find_next_monday(current_date + datetime.timedelta(days=1))

for extra in range(0, extra_dates):
    generate_event_file(current_date, "TBA")
    current_date = find_next_monday(current_date + datetime.timedelta(days=1))