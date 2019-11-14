from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    matric = Column(String, primary_key = True)
    name = Column(String(250))
    leftprint = Column(String(250))
    rightprint = Column(String(250))
    leftiris = Column(String(250))
    rightiris = Column(String(250))

class Attendances(Base):
    __tablename__ = 'attendances'
    code = Column(String(12), primary_key = True)
    week = Column(Integer)
    count = Column(Integer)
    students = Column(String)

class Courses(Base):
    __tablename__ = 'courses'
    code = Column(String(12), primary_key = True)
    title = Column(String(250))
    day = Column(String(12))
    period = Column(String(12))

# res0 = attendances.insert().values(code = 'CPE412', week = 3, count = 1, students = str(['2015/1/54321KI']))
# res2 = courses.insert().values(title = 'Introduction to C++ Programming', code = 'CPE311', day = 'Tuesday', period = '14:30')
# res = students.select()
# res1 = attendances.select()
# res3 = courses.select()
# conn = engine.connect()
# result = conn.execute(res)
# result1 = conn.execute(res1)
# result0 = conn.execute(res0)
# result2 = conn.execute(res2)
# result3 = conn.execute(res3)

if __name__ == "__main__":
    engine = create_engine('sqlite:///atted.db')
    Base.metadata.create_all(engine)

    session = Session(engine)

    session.add(Students(matric = '2014/1/45655CP', name = 'Joel Audu', leftprint = '2', rightprint = '3'))
    session.commit()

    # def savefile(self, name, mode, data):
    #     with open(name + '.json', mode) as f:
    #         j.dump(data, f, indent=4)
    #     f.close()

    # def readfile(self, name):
    #     with open(name + '.json') as f:
    #         data = j.load(f)
    #     f.close()
    #     return data