--1
Use ITI
go
Create procedure Student_Numbers
	as	
	begin
		select Dept_Name DepartmentName , count(St_Id) StudentNumber 
		from Department D 
		inner join Student S 
		on s.Dept_Id = d.Dept_Id 
		group by Dept_Name
	end
go

exec Student_Numbers



--2
Use Company_SD
go
Create procedure Emp_Numbers   @pname varchar(20),@num int=null 
	as
	begin
		select  @num = count(ESSn)  
		from Project p
		inner join Works_for w
		on p.Pnumber = w.Pno  and pname =@pname
		inner join Employee e
		on e.SSN = w.ESSn
			if @num > 3
			begin
				select 'The number of employees in the project '+@pname+' is 3 or more'
			end
			else  
			begin
				 select 'The following employees work for the project '+@pname
				 union all 
				 select concat(fname ,' ', lname)  
				 from Project p
					inner join Works_for w
					on p.Pnumber = w.Pno  and pname =@pname
					inner join Employee e
					on e.SSN = w.ESSn
			end
	end
go
exec Emp_Numbers 'Al Rowad'



--3
go
Create procedure update_WorksFor  @old int , @new int , @pnum int
	as
	begin
		begin try
			update Works_for 
			set ESSn = @new
			where ESSn = @old and Pno = @pnum

			select 'Employee updated successfully.'
		end try
		begin catch
			select  'Error occurred: ' + @@error
		end catch
	end
go
exec update_WorksFor @old = 102672, @new = 512463, @pnum = 200



--4
IF COL_LENGTH('Project', 'Budget') IS NULL
    ALTER TABLE Project ADD Budget MONEY;
GO

-- Fill sample values
UPDATE Project SET Budget = 95000;
GO

-- Create Audit table
CREATE TABLE Audit (
    ProjectNo INT NOT NULL,
    UserName NVARCHAR(50) NOT NULL,
    ModifiedDate DATE,
    Budget_Old MONEY NOT NULL,
    Budget_New MONEY NOT NULL
);
GO

-- Create Trigger to audit budget updates
CREATE TRIGGER Update_Audit
ON Project
AFTER UPDATE
AS
BEGIN
    IF UPDATE(Budget)
    BEGIN
        INSERT INTO Audit (ProjectNo, UserName, ModifiedDate, Budget_Old, Budget_New)
        SELECT 
            i.Pnumber, 
            SUSER_NAME(), 
            GETDATE(), 
            d.Budget, 
            i.Budget
        FROM inserted i
        JOIN deleted d ON i.Pnumber = d.Pnumber
        WHERE i.Budget <> d.Budget;
    END
END;
GO

-- Test the trigger
UPDATE Project SET Budget = 200000 WHERE Pname = 'AL Solimaniah';
GO

-- See audit results
SELECT * FROM Audit;


--5
Use ITI

go

Create Trigger Prevent_insert
on Department
instead of insert
	as
	begin
		select 'You can’t insert a new record in that table'
	end
go



--6
Use Company_SD
go

Create Trigger Prevent_InsertEmp
on Employee
after insert
	as
	begin
		if Month(getdate()) = 3
		begin
			rollback transaction
			select 'Insertion not allowed in March.'
		end
	end
go



--7
Use ITI
go

Create Table Student_Audit
(
	UserName nvarchar(50) not null  ,
	ModifiedDate date  ,
	Note nvarchar(200) ,
)
go

Create Trigger Update_Audit
on Student
after insert
	as 
	begin
		insert into Student_Audit (UserName, ModifiedDate, Note)
			SELECT 
				SUSER_NAME(),
				GETDATE(),
				SUSER_NAME() + ' Insert New Row with Key = [' + CONVERT(NVARCHAR(20), St_Id) + '] in table Student'
			FROM inserted;
	end
go



--8
go

Create Trigger Student_Delete
on Student 
instead of Delete
	as
	begin
		insert into Student_Audit (UserName, ModifiedDate, Note)
			SELECT 
				SUSER_NAME(),
				GETDATE(),
				SUSER_NAME() + ' Try to delete Row with Key = [' + CONVERT(NVARCHAR(20), St_Id) + ']'
			FROM deleted
	end
