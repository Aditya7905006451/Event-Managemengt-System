import json
import string
import random
from json import JSONDecodeError
from datetime import datetime,date

def AutoGenerate_EventID():
    #generate a random Event ID
    Event_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
    return Event_ID

def Register(type,member_json_file,organizer_json_file,Full_Name,Email,Password):
    '''Register the member/ogranizer based on the type with the given details'''
    if type.lower()=='organizer':
        f=open(organizer_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()
    else:
        f=open(member_json_file,'r+')
        d={
            "Full Name":Full_Name,
            "Email":Email,
            "Password":Password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
        f.close()

def Login(type,members_json_file,organizers_json_file,Email,Password):
    '''Login Functionality || Return True if successful else False'''
    d=0
    if type.lower()=='organizer':
        f=open(organizers_json_file,'r+')
    else:
        f=open(members_json_file,'r+')
    try:
        content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["Email"]==Email and content[i]["Password"]==Password:
            d=1
            break
    if d==0:
        f.close()
        return False
    f.close()
    return True

def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    '''Create an Event with the details entered by organizer'''
    f = open(events_json_file, 'r+')
    d = {
        "ID":Event_ID,
        "Name":Event_Name,
        "Organizer": org,
        "Start Date":Start_Date,
        "Start Time":Start_Time,
        "End Date":End_Date,
        "End Time":End_Time,
        "Users Registered":Users_Registered,
        "Capacity":Capacity,
        "Seats Available":Availability 
    }
    try:
        content = json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close()

def View_Events(org,events_json_file):
    '''Return a list of all events created by the logged in organizer'''
    f=open(events_json_file,'r+')
    content = json.load(f)
    ans_list = []
    for i in content:
        if i["Organizer"] == org:
            ans_list.append(i)
    return ans_list

def View_Event_ByID(events_json_file,Event_ID):
    '''Return details of the event for the event ID entered by user'''
    Event_ID = int(input("Enter a Event ID is: "))
    l = []
    f = open(event_json.file,"r+")
    content = json.load(f)
    for i in content:
        if content["ID"] == Event_ID:
            return i

def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_detail):
    '''Update Event by ID || Take the key name to be updated from member, then update the value entered by user for that key for the selected event
    || Return True if successful else False'''
    org = input("Enter the Organizer is:")
    Event_ID = int(input("Enter a Event ID is: "))
    l = []
    f = open(event_json.file,"r+")
    content = json.load(f)
    for i in content:
        if content["ID"] == Event_iD:
            content[i][detailed_to_be_updated] = updated_detail
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
        else:
            return False

def Delete_Event(org,events_json_file,event_ID):
    '''Delete the Event with the entered Event ID || Return True if successful else False'''
    org = input("Enter the Organizer is:")
    event_ID = int(input("Enter a Event ID is: "))
    f = open(event_json.file,"r+")
    content = json.load(f)
    for i in content:
        if content["ID"] == Event_ID:
            del content[i]
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
        else:
            return False


def Register_for_Event(events_json_file,event_id,Full_Name):
    '''Register the logged in member in the event with the event ID entered by member. 
    (append Full Name inside the "Users Registered" list of the selected event)) 
    Return True if successful else return False'''
    date_today=str(date.today())
    # print(date_today) current date
    now = datetime.now()
    # print(now) no use
    current_time = now.strftime("%H:%M:%S")
    # print(current_time) current time
    '''Write your code below this line'''   
    event_id = int(input("Event a Event ID: "))
    Full_Name = input("Enter a Full Name: ")
    if append.Full_Name == Users_Registered:
        return True
    else:
        return False 

def fetch_all_events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    '''View Registered Events | Fetch a list of all events of the logged in memeber'''
    '''Append the details of all upcoming and ongoing events list based on the today's date/time and event's date/time'''
    date_today=str(date.today())
    # print(date_today)
    # print(type(date_today)) - str
    now = datetime.now()
    # print(now)
    # print(type(now))
    # no use with now
    current_time = now.strftime("%H:%M:%S")
    # print(current_time)
    # print(type(current_time)) - str
    '''Write your code below this line'''
    Full_Name = input("Enter a Full Name: ")
    if append.date_today == Register_for_Event:
        if append.current_time == Register_for_Event:
            return True
        else:
            return False
    else:
        return

def Update_Password(members_json_file,Full_Name,new_password):
    '''Update the password of the member by taking a new passowrd || Return True if successful else return False'''
    f=open(members_json_file,'r+')
    content = json.load(f)
    for i in content:
        if i["Full Name"] == Full_Name:
            i["Password"] = new_password
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            return True
        else:
            continue
    return False

def View_all_events(events_json_file):
    '''Read all the events created | DO NOT change this function'''
    '''Already Implemented Helper Function'''
    details=[]
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details
