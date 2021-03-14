#OM NAMO NARAYANA
f = open('F:/users/barath/ContactDetails_2022Batch_part2.txt', 'r', encoding="utf8")
txt = f.read()
temp_list = list(txt.split('.edu'))
roll_no = []
name = []
branch = []
batch = []
parentsName = []
address = []
dOB = []
bloodGrp = []
contactNo = []
count = 0

for i, temp in enumerate(temp_list):
    print(i)
    try:
        Name, ParentsName = list(temp.split('Name'))[1:3]
        Name, Roll_no = list(Name.split('No'))
        Roll_no, Branch = list(Roll_no.split("Branch"))
        ParentsName, Address = list(ParentsName.split('Address'))
        Address, DOB = list(Address.split('D.O.B'))
        DOB, BloodGrp = list(DOB.split('Group'))
        BloodGrp, ContactNo = list(BloodGrp.split('No'))
        contactNo.append(list(ContactNo.split('EMAIL'))[0])
        roll_no.append(Roll_no)
        parentsName.append(ParentsName)
        address.append(Address)
        bloodGrp.append(BloodGrp)
        dOB.append(DOB)
        name.append(Name)
        print(roll_no[-1])
    except:
        count = count+1
contact_number = []
for contact in contactNo:
    temp = list(contact.split('\n'))
    contact_number.append([i for i in temp if(len(i)>1)])
print(count)
print(len(name))
print(contact_number[:100])
print(name[100], contact_number[100])