import mysql.connector as mc
mdb=mc.connect(host='localhost',user='root',passwd='jayk',database='jaykamavisdar')
cr=mdb.cursor()
def stocks():
    bname=input('Enter the book name::')
    author=input('Enter author name::')
    def imported():
        qty=int(input('Enter quantity::'))
        doa=input('Enter the date of arrival::')
        val=(bname,author,qty,doa)
        qry1="insert into libimport values(%s,%s,%s,%s)"
        cr.execute(qry1,val)
        print(cr.rowcount,'book added to library')
        rec=input('Do you wanna review the records(y or n)::')
        if rec.lower()=='y':
            cr.execute('select * from libimport')
            out=cr.fetchall()
            for x in out:
                print(x)
        mdb.commit()
    def already():
        bid=input('Enter Book ID::')
        shelf=input('Enter Shelf No.::')
        val=(bid,bname,author,shelf)
        qry2="insert into libstocks values(%s,%s,%s,%s)"
        cr.execute(qry2,val)
        print(cr.rowcount,'book entered in the record')
        rec=input('Do you wanna review the records(y or n)::')
        if rec.lower()=='y':
            cr.execute('select * from libstocks')
            out=cr.fetchall()
            for x in out:
                print(x)
        mdb.commit()

    ch1='yY'
    while ch1 in 'yY':
        print('Where do you wanna add these books?')
        print('1.In Imports')
        print('2.In Stock')
        print('3.EXIT')
        ch=int(input('Enter you choice(1 to 3)::'))
        if ch==1:
            imported()
        elif ch==2:
            already()
        elif ch==3:
            print('See you soon')
        else:
            print('Enter valid choice')
        ch1=input('Do you wanna repeat(y or n)::')

def student():
    reg_no=int(input('Enter the registration number::'))
    sname=input('Enter the student name::')
    def rbs():
        dor=input('Enter the date of return::')
        bid=input('Enter Book ID of returned book::')
        val=(reg_no,sname,dor,bid)
        qry3="insert into return_by_student values(%s,%s,%s,%s,%s)"
        cr.execute(qry3,val)
        if cr.rowcount>1:
            print(cr.rowcount,'books are returned')
        else:
            print(cr.rowcount,'book is returned')
        rec=input('Do you wanna review the records(y or n)::')
        if rec.lower()=='y':
            cr.execute('select * from return_by_student')
            out=cr.fetchall()
            for x in out:
                print(x)
        mdb.commit()
    def taken():
        dot=input('Enter the date of taking::')
        bid=input('Enter Book ID of taken book::')
        val=(reg_no,sname,dot,bid)
        qry4="insert into taken_by_student values(%s,%s,%s,%s)"
        cr.execute(qry4,val)
        print(cr.rowcount,'book taken by',sname, reg_no)
        rec=input('Do you wanna review the records(y or n)::')
        if rec.lower()=='y':
            cr.execute('select * from taken_by_student')
            out=cr.fetchall()
            for x in out:
                print(x)
        mdb.commit()

    ch2='y'
    while ch2 in 'yY':
        print('1.Taking')
        print('2.Returning')
        ch=int(input('Enter you choice(1 or 2)::'))
        if ch==1:
            taken()
        elif ch==2:
            rbs()
        else:
            print('Enter valid choice')
        ch2=input('Do you wanna add another record(y or n)::')

def demands():
    bname=input('Enter the demanded book name::')
    author=input('Enter author name::')
    qty=int(input('Enter quantity::'))
    val=(bname,author,qty)
    qry="insert into libdemands values(%s,%s,%s)"
    cr.execute(qry,val)
    print(cr.rowcount,'book added to demand list')
    rec=input('Do you wanna review the records(y or n)::')
    if rec.lower()=='y':
        cr.execute('select * from libdemands')
        out=cr.fetchall()
        for x in out:
            print(x)
    mdb.commit()
def records():
    ch='y'
    while ch in 'yY':
        print('What do you wanna see')
        print('1.Library Imports')
        print('2.Library Demands')
        print('3.Library Stocks')
        print('4.Books taken by students')
        print('5.Books returned by students')
        menu=int(input('Enter your choice(1 to 6)::'))
        if menu==1:
            cr.execute('select * from libimport')
            for x in cr:
                print (x)
        elif menu==2:
            cr.execute('select * from libdemands')
            for x in cr:
                print (x)
        elif menu==3:
            cr.execute('select * from libstocks')
            for x in cr:
                print (x)
        elif menu==4:
            cr.execute('select * from taken_by_student')
            for x in cr:
                print (x)
        elif menu==5:
            cr.execute('select * from return_by_student')
            for x in cr:
                print (x)
        elif menu==6:
            print('Thank YOU')
        else:
            print('Enter valid Choice')
        ch=input('Do you wanna see something else(y or n)::')

CH='y'
while CH in 'yY':
    print('******MENU******')
    print('1.Edit Stock Records')
    print('2.Edit Student Records')
    print('3.Add a book to demand list')
    print('4.View Records')
    choice=int(input('Enter your choice(1 to 4)::'))
    if choice==1:
        stocks()
    elif choice==2:
        student()
    elif choice==3:
        demands()
    elif choice==4:
        records()
    else:
        print('Enter valid choice number')
    CH=input('Do you wanna review something else(y or n)::')