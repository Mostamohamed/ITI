USE ITI


--1
create function getmonth(@date DATE)
returns NVARCHAR(10)
as
begin
    declare @month NVARCHAR(10)
    set @month = FORMAT(@date, 'MMMM')
    return @month
end

SELECT dbo.getmonth('2024-07-21')



--2
create function getvalues(@fvalue int , @svalue int)
returns @t table 
(
	betweenvalue int
)
		as
		begin
			while @fvalue+1<@svalue
			begin
			set @fvalue+=1
			insert into @t
			select @fvalue
			end
			return
		end
		    
select * from  dbo.getvalues(10,20)



--3
create function getdeptname(@st_no int)
returns table 
		as return(
			 select d.Dept_Name ,s.St_Fname + ' ' + s.St_Lname AS FullName
			 from Student s
			 inner join Department d
			 on s.Dept_Id=d.Dept_Id and s.St_Id =@st_no	
		)

select * from  dbo.getdeptname(10)



--4
create function getmsg(@st_id int)
returns nvarchar(100)  
	 as
     begin
			 declare @msg nvarchar(50)
			 declare @fname nvarchar(20)
			 declare @lname nvarchar(20)
		 select @fname=st_fname , @lname=St_Lname 
			from student 
			where St_Id = @st_id
		 if @fname is null and @lname is null
			set @msg ='First name & last name are null'
		 else if @fname is null and @lname is not null
			set @msg ='first name is null'
		 else if @fname is not null and @lname is null
			set @msg ='last name is null'
		 else 
			set @msg ='First name & last name are not null'
		 return @msg 
	 end


select dbo.getmsg(14) as msg
select dbo.getmsg(13)  as msg



--5
create function getdetails(@mgr_id int)
returns table 
		as return(
			 select 
				Dept_Name , Ins_Name , Manager_hiredate
			 from Department 
			 inner join Instructor
			 on Instructor.Ins_Id=Department.Dept_Manager and Department.Dept_Manager=@mgr_id
		)
select * from  dbo.getdetails(13)



--6
create function getstname(@string nvarchar(50))
returns @t table 
(
	studentName nvarchar(100)
)
	as
	begin
		 if @string ='first name'
					 insert into @t
	 				 select isnull(St_Fname,'Fname') from Student
		 else if @string ='last name'
					 insert into @t
	 				 select isnull(St_Lname,'Lname') from Student
		 else if @string ='full name'
					 insert into @t
	 				 select LTRIM(RTRIM(isnull(St_Fname+' '+St_Lname,'Fullname'))) 
					 --I used LTRIM(RTRIM(...)) to remove leading/trailing spaces if one of the names is missing.
					 from Student
				return
	end
		    
select * from  dbo.getstname('first name')
select * from  dbo.getstname('last name')
select * from  dbo.getstname('full name')



--7
select St_Id 'Student No', LEFT(St_Fname,len(St_Fname)-1) 'Student first name' 
from student 


--8
delete Stud_Course from Stud_Course	 
		inner join student 
		on Stud_Course.St_Id = Student.St_Id 
		inner join Department 
		on Department.Dept_Id = Student.Dept_Id
	where Dept_Name='SD'


--9
--Creating schema
USE Company_SD
IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'Company')
    EXEC('CREATE SCHEMA Company');

IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = 'HumanResource')
    EXEC('CREATE SCHEMA HumanResource');

--transfer tables
IF OBJECT_ID('dbo.Departments', 'U') IS NOT NULL
BEGIN
    ALTER SCHEMA Company TRANSFER dbo.Departments;
END

IF OBJECT_ID('dbo.Employee', 'U') IS NOT NULL
BEGIN
    ALTER SCHEMA HumanResource TRANSFER dbo.Employee;
END



--10
SELECT 
    CONSTRAINT_NAME, 
    CONSTRAINT_TYPE
FROM 
    INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE 
    TABLE_NAME = 'Employee';


--11
CREATE SYNONYM Emp FOR HumanResource.Employee

Select * from Employee 
-- Fail Will work only if Employee exists in the default schema, usually dbo

Select * from [Human Resource].Employee  
--FAIL is not a valid schema name

Select * from Emp 
--Run 

Select * from [Human Resource].Emp 
--Fail Synonyms cannot be accessed via a different schema than they were created in.


--12
USE ITI

CREATE LOGIN ITIStud 
WITH PASSWORD = 'PASSWORD';


CREATE USER ITIStud FOR LOGIN ITIStud;

--GRANT
GRANT SELECT, INSERT ON dbo.Student TO ITIStud;
GRANT SELECT, INSERT ON dbo.Course TO ITIStud;

--DENY
DENY UPDATE, DELETE ON dbo.Student TO ITIStud;
DENY UPDATE, DELETE ON dbo.Course TO ITIStud;
