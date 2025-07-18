--Instructor Table 
CREATE TABLE Instructor (
    ID INT IDENTITY PRIMARY KEY,
    First VARCHAR(50),
    Last VARCHAR(50),
    BD DATE,
    HireDate DATE DEFAULT GETDATE(),
    Salary DECIMAL(10,2) DEFAULT 3000 CHECK (Salary BETWEEN 1000 AND 5000),
    OverTime DECIMAL(10,2) UNIQUE,
    Address VARCHAR(50) CHECK (Address IN ('Cairo', 'Alex')),

 
    NetSalary AS (Salary + OverTime) PERSISTED,
    Age AS (YEAR(GETDATE()) - YEAR(BD))
);


--Course Table
CREATE TABLE Course (
    CID INT IDENTITY PRIMARY KEY,
    CName VARCHAR(100),
    Duration INT UNIQUE
);


--Teach Table
CREATE TABLE Teach (
    InstructorID INT,
    CID INT,
    PRIMARY KEY (InstructorID, CID),
    FOREIGN KEY (InstructorID) REFERENCES Instructor(ID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (CID) REFERENCES Course(CID)
        ON UPDATE CASCADE ON DELETE CASCADE
);


--Lab Table
CREATE TABLE Lab (
    CID INT,
    LID INT IDENTITY(1,1), 
    Location VARCHAR(100),
    Capacity INT CHECK (Capacity < 20),

    PRIMARY KEY (CID, LID),
    FOREIGN KEY (CID) REFERENCES Course(CID)
        ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE Instructor;
DROP TABLE Course;
DROP TABLE Teach;
DROP TABLE Lab;