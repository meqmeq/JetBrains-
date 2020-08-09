# Write your code here

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
import calendar

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

today = datetime.today()  # Initiate Today Global Variable

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while 1:
    #User Inputs
    userInput = int(input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit 
    """))

    if userInput == 0:  # exit
        break
    elif userInput == 1:  # input 1 add rows
        rows = session.query(Table).filter(Table.deadline == today.date()).all()  # Only select today's task
        print(f"Today {today.day} {today.strftime('%b')}:")
        if not rows:
            print("Nothing to do!\n")
        else:
            for numTask in range(len(rows)):
                print(str(rows[numTask].id) + ". " + rows[numTask].task)

    elif userInput == 2:
        for i in range(0, 7):
            rowDay = today + timedelta(days=i)  # Gets day of the week
            rows = session.query(Table).filter(Table.deadline == rowDay.date()).all()  # Only select rowDay's task
            print(rowDay.strftime("%A %d %b:"))  # Print the date
            if not rows:
                print("Nothing to do!\n")
            else:
                for numTask in range(len(rows)):
                    print(f"{rows[numTask].id}. {rows[numTask].task}\n")

    elif userInput == 3:
        print("All tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!\n")
        else:
            for numTask in range(len(rows)):
                print(f'{rows[numTask].id}. {rows[numTask].task}. {rows[numTask].deadline.strftime("%#d %b")}')
                # print(f'{row[numTask].id}. {row[numTask].task}. {row[numTask].strftime("%d %b")}')
        print('\n')

    elif userInput == 4:
        rows = session.query(Table).filter(Table.deadline < today.date()).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!\n")
        else:
            for numTask in range(len(rows)):
                print(f'{rows[numTask].id}. {rows[numTask].task}. {rows[numTask].deadline.strftime("%#d %b")}')
        print('\n')



    elif userInput == 5:  # Add task
        inputTask = input("Enter task\n")
        inputDeadline = input("Enter deadline\n")
        formedDeadline = datetime.strptime(inputDeadline,'%Y-%m-%d')
        new_row = Table(task=inputTask,
                        deadline=formedDeadline)
        session.add(new_row)
        session.commit()
        print("The task has been added!"
              "")

    elif userInput == 6:
        print("Choose the number of the task you want to delete:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print("Nothing to do!\n")
        else:
            for numTask in range(len(rows)):
                print(f'{rows[numTask].id}. {rows[numTask].task}. {rows[numTask].deadline.strftime("%#d %b")}')

            deleteItem = int(input())
            specific_row = rows[deleteItem - 1]
            session.delete(specific_row)
            session.commit()
        print("The task has been deleted!")
        print('\n')


print("Bye!")
