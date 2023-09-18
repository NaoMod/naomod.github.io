import icalendar

def cleanstring(something):
    return str(something).replace('"', '').replace("'","").replace(":","").replace("\n"," ").strip()

def YamlHead(data):
    out = ""
    out += "---\nlayout : null\n"
    for key,value in data.items():
        string = cleanstring(value)
        out +=  "{} : {}\n".format(key,string)
    out+="---\n"
    return out

def write_md(data):
    filename = data['filename'] + ".md"
    with open(filename, 'w') as file:
        file.write(YamlHead(data['yamlhead']))
        if data["body"]:
            file.write(data["body"])


def load_ics(path):
    out = []
    file = open(path, 'rb')
    ical = icalendar.Calendar.from_ical(file.read())
    for component in ical.walk():
        if component.name == "VEVENT":
            out.append(component)
            print(component.get("summary"))
            print(component.get("description"))
            # print(component.get("organizer"))
            print(component.get("location"))
            print(component.decoded("dtstart"))
            print("-----------------")
    file.close()
    return out

def datetime2stringdict(data):
    out = {}
    out["year"] = "{}".format(data.year)
    out["month"]= "{:02d}".format(data.month)
    out["day"] = "{:02d}".format(data.day)
    return out


def extractfilename(decoded_datetime,title):
    out = ""
    xdate = datetime2stringdict(decoded_datetime)
    out += "{}-{}-{}".format(xdate["year"],xdate["month"],xdate["day"])
    for word in cleanstring(title).replace("-","").replace(",","").split():
        out += "-{}".format(word)
    
    print(out)
    return out
    


def extractdata(event):
    out = {}
    out["filename"] = extractfilename(event.decoded("dtstart"), event.get("summary"))
    
    out["yamlhead"] = {"title":event.get("summary")}
    # out["yamlhead"].update(datetime2stringdict(event.decoded("dtstart"))) #removed because we should be able to use jekyll to query
    
    out["yamlhead"] = {"speaker":event.get("location")}
    out["yamlhead"] = {"location":"na-b218"} #default location

    #Get fields from ICS and similarly assign "field name : field value" in yaml header
    # for var in ["location","summary","description"]: #location moved to speaker field
    for var in ["summary","description"]:
        out["yamlhead"].update({var : event.get(var)})

    out["body"] = event.get("description")
    return out


events = load_ics("NaomodWeeklySeminars")
for event in events:
    write_md(extractdata(event))