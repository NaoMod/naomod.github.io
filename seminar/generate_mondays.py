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


############
# Input data
############
start_date: datetime.date = datetime.date(2023, 11, 14)
output_dir: Path = Path("./seminar/2324/_posts")
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
    "Yasmina Daliyoucef",
    "Josselin Enet",
    "James Miranda",
]
random.shuffle(speakers)

############
# Preparations
############
output_dir.mkdir(parents=True, exist_ok=True)
example_file: Path = Path("./seminar/example.md")
if not example_file.exists():
    raise "Missing example file at location " + str(example_file)

template: Template = Template(example_file.read_text())

############
# Loop
############
current_date = start_date + datetime.timedelta(days=1)
counter: int = 1

for speaker in speakers:
    next_monday: datetime.date = find_next_monday(current_date)
    file_name = str(next_monday) + "-talk" + str(counter) + ".md"
    counter = counter + 1
    output_file: Path = output_dir / file_name
    output_file.write_text(template.substitute(speaker=speaker))
    print("Created " + str(output_file))
    current_date = next_monday + datetime.timedelta(days=1)
