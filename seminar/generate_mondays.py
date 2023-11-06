import datetime
from pathlib import Path


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
    return onDay(date, 0)


############
# Input data
############
start_date: datetime.date = datetime.date(2023, 11, 6)
end_date: datetime.date = datetime.date(2024, 4, 1)
output_dir: Path = Path("./seminar/2324/_posts")

############
# Preparations
############
output_dir.mkdir(parents=True, exist_ok=True)
example_file: Path = Path("./seminar/example.md")
if not example_file.exists():
    raise "Missing example file at location " + str(example_file)

############
# Loop
############
finished: bool = False
current_date = start_date + datetime.timedelta(days=1)
counter: int = 1
while not finished:
    next_monday: datetime.date = find_next_monday(current_date)
    if next_monday > end_date:
        finished = True
    else:
        file_name = str(next_monday) + "-talk" + str(counter) + ".md"
        counter = counter + 1
        output_file: Path = output_dir / file_name
        output_file.write_text(example_file.read_text())
        print("Created " + str(output_file))
        current_date = next_monday + datetime.timedelta(days=1)
