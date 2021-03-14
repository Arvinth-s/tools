#OM NAMO NARAYANA
import csv

input_file = 'F:/users/barath/ContactDetails_2022Batch.txt'
save_csv_file = 'F:/users/barath/nitt_1.csv'

f = open(input_file, 'r', encoding="utf8")
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
print(temp_list[0])

for i, temp in enumerate(temp_list):
    try:
        Name, ParentsName = list(temp.split('Name'))[1:3]
        Name, Roll_no = list(Name.split('No'))
        Roll_no, Branch = list(Roll_no.split("Branch"))
        Branch, Batch = list(Branch.split('Batch'))
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
        branch.append(Branch)
    except:
        count = count+1
_contact = []
for contact in contactNo:
    temp = list(contact.split('\n'))
    _contact.append([i[3:] for i in temp if(len(i)>1)])
_name = []
for Name in name:
    temp = list(Name.split('Roll'))
    temp = list(temp[0].split(':'))
    _name.append([i for i in temp if(len(i)>1)])
_address = []
for Address in address:
    temp = list(Address.split(':'))
    _address.append([i for i in temp if(len(i)>1)])
_roll_no = []
for Roll_no in roll_no:
    temp = list(Roll_no.split(':'))
    _roll_no.append([i for i in temp if(len(i)>1)])

for Roll_no in roll_no:
    temp = list(Roll_no.split(':'))
    _roll_no.append([i for i in temp if(len(i)>1)])

_branch = []
for Branch in branch:
    temp = list(Branch.split(':'))
    _branch.append([i for i in temp if(len(i)>1)])

address = _address
_address = []
for addr in address:
    addr = list(addr[0].split(','))
    temp = ""
    for i in addr:
        temp = temp + " " + i
    _address.append([temp])

contact = _contact
_contact = []
for cont in contact:
    temp = ""
    for i in cont:
        temp = temp + " " + i
    _contact.append([temp])

print(count)
print(len(name))

select = 122

print('Name:', _name[select], 'Contact:', _contact[select], 'Address:', _address[select], 'Roll number:', _roll_no[select], 'Branch:', _branch[select])



with open(save_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(_name)):
        writer.writerow([_name[i][0], _contact[i][0], _branch[i][0], _roll_no[i][0], _address[i][0]])