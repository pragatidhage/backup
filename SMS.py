import pymysql
import os 
exit='n'
while exit=='n':
        os.system("cls")
        print('-'*90) 
        print('|'+' ' *31+ 'STUDENT MANAGEMENT SYSTEM'+' '* 32+'|')
        print('-'*90) 
        print('|[I]nsert Record |', end='')
        print(' [V]iew Record   |', end='')
        print(' [U]pdate Record |', end='')
        print(' [D]elete Record |', end='')
        print('    [E]XIT |')
        print(90)
        ch=input("YOUR Choice (I/V/U/D/E):")
        ch=ch.upper()
        if ch == 'I':

            connection-pymysql.connect(host="localhost", user="root",passwd="root", db="school")
            mycursor=connection.cursor() 
            choice='y'
            while choice=='y':
                    sno=input('enter the roll number of student')
                    sname=input('enter the name of student')
                    Qry ("INSERT INTO class12 "\ 
                        "VALUES (%5, %s)")
                    data= (sno, sname)
                    mycursor.execute(Qry, data) 
                    print("RECORD INSERTED SUCCESSFULLY")
                    choice=input( 'do you with to insert more records (y/n)')
                    if choice=='y':
                      continue
                    connection.commit() 
                    connection.close()

       elif ch == "V":
          connection=pymysql.connect(host="localhost", user="root", pass

wd="root", db="school") mycursor connection.cursor() #mycursor.execute(""create table class12 (rno int, name varch

ar(20))""")

choice='y' while choice=='y":

rno-int(input('enter the roll number of student whose reco

rd you want to search ))

Qry ("""select from class12 WHERE rno = %s""")

data= (rno,)

mycursor.execute(Qry, data)

count=0

for (rno, name)in mycursor:

count+=1

print("Student Roll Norno) print('Student Name ,name)

print(======') if count :

print('press any key to continue") clrscreen()

print('total records, count, 'found') choice=input('do you with to search more record (y/n)')) if choice=='y':

continue

connection.commit() connection.close() == "U":

elif ch
connection=pymysql.connect(host="localhost", user="root", pass

wd="root", db="school")

mycursor connection.cursor() #inycursor.execute("" "create table class12 (rno int, name varch

an(20))""")

choice='y' while(choice=='y'):

rno=int(input('enter the roll number of student whose reco

to change '))

rd you want

name=input('enter new name')

Qry = ("""UPDATE class12 set name=%s WHERE rno = %s"**)

data (name, rno)

mycursor.execute(Qry, data)

print( RECORD UPDATED SUCCESSFULLY')

choice=input('do you wish to update more records (y/n)')

if choice=='y": continue

connection.commit()

connection.close()

elif ch 'D':

connection=pymysql.connect(host="localhost", user="root", pass

wd="root", db="school")

mycursor connection.cursor() #nycursor.execute("""create table class12 (rno int, name varch

ar(28))")

choice='y'

while choice=='y':

rno-int(input('enter the roll number of student whose reco

rd you want to delete :))

Qry (""DELETE FROM class12 WHERE rno = %s""") data = (rno,)
mycursor.execute(Qry, data)

print( RECORD DELETED SUCCESSFULLY')

choice=input('Do you wish to delete more records (y/n) ?")

if choices'y':

continue

connection.commit() connection.close()

elif ch == 'E':

print("\n\t\t Thanks for using Student Management System...")

print("\t\t------ print("\t\t

Created By anjeevsinghacademy.com |") print("\t\t- break

-

-")

else:

print('\t\t\t Error: Not a valid Option ) print("\t\t Valid option are "I", "V", "U", "D", or "E" only")

exit=input("\t\t Do you wish to exit the program(y/n)")

if exits'n':

continue