Use ITI

--1
Create view Student_Details	
as
select concat(s.St_Fname,' ',s.St_Lname) as FullName ,c.Crs_Name As CourseName , Grade 
		from Student as S 
		inner join Stud_Course as SC 
		on s.St_Id=sc.St_Id
		inner join Course as C 
		on c.Crs_Id=sc.Crs_Id
		where sc.Grade > 50

select * from Student_Details



--2 
create view View_MangerDetails 
with encryption
as
select Ins.Ins_Name as ManagerName , Top_Name as Topic 
		from Department as Dept 
		inner join  Instructor as Ins 
		on Dept.Dept_Manager = ins.Ins_Id 
		inner join Ins_Course 
		on ins.Ins_Id=Ins_Course.Ins_Id
		inner join Course 
		on Ins_Course.Crs_Id = Course.Crs_Id
		inner join Topic 
		on Topic.Top_Id = Course.Top_Id


select * from View_MangerDetails



--3
Create view View_InsDeptDetails
as
select i.Ins_Name as InstuctorName , Dept_Name as DepartmentName 
		from Instructor i
		inner join Department d
		on d.Dept_Id=i.Dept_Id
		where d.Dept_Name in ('SD','Java')

select * from View_InsDeptDetails



--4
create view V1 
as
select * 
from Student 
where St_Address in ('Alex','Cairo')
With  check	option;

update V1
set st_address='tanta'
Where st_address='alex';
--The attempted update or insert failed because the target row would not be visible in the view.

select * from V1



--5
Use Company_SD

Create View View_ProjectDetails
as
select p.Pname as ProjectName , count(w.ESSn) as NumOFEmps 
		from Project p
		inner join Works_for w
		on p.Pnumber = w.Pno 
		inner join Employee e
		on e.SSN = w.ESSn
		group by p.Pname 

select * from View_ProjectDetails



--6
Use ITI

-- can't use clustered cause the table have primary key and already one clustered index
--SQL Server allows only one clustered index per table
--iam not allowed to create another clustered index
Create nonclustered index  manager_Hiredate 
on Department(Manager_hiredate)



--7
-- there are duplicated value in age
Create unique index Unique_Age 
on Student(st_age) 
--will fail, there are duplicate age values in the St_Age column



--8.
Use Company_SD

declare EditSalary Cursor
for select salary 
	from Employee
	for update 
declare @salary  money
open EditSalary
fetch next from EditSalary into @salary
while @@fetch_status = 0
	begin
		if @salary < 3000
		begin
			update Employee
			set salary += @salary*.1
			where current of EditSalary
		end
		else
		begin
			update Employee
			set Salary += @salary*.2 
			where current of EditSalary
		end
		fetch next from EditSalary into @salary
	end
close EditSalary
deallocate EditSalary



--9
use iti

declare DeptDetails Cursor
for select Dept_Name , Ins_Name  
	from Department d
	inner join Instructor i
	on d.Dept_Manager = i.Ins_Id
for read only 
declare @deptName nvarchar(50) , @mangName nvarchar(50)
open  DeptDetails
fetch next from DeptDetails into @deptName, @mangName
while @@fetch_status = 0
	begin
		select @deptName, @mangName
		fetch next from DeptDetails into @deptName, @mangName
	end
close DeptDetails
deallocate DeptDetails



--10
declare instNames cursor
for select distinct Ins_Name
	from Instructor 
	where Ins_Name is not null
for read only
declare @name varchar(50),@all_names varchar(max)=''
open instNames
fetch next from instNames into @name
while @@FETCH_STATUS=0
	begin
		-- If @all_names is empty, don't add comma
		if @all_names = ''
			set @all_names = @name;
		else
			set @all_names = @all_names + ', ' + @name;

		fetch next from instNames into @name;
	end

close instNames
deallocate instNames
select @all_names


--11	Try to generate script from DB ITI that describes all tables and views in this DB

-- Error because of encryption of views --



--12 Using Merge statement between the following two tables [User ID, Transaction Amount]
-- first create tables

create table LastTransactions (
    UserID INT PRIMARY KEY,
    TransactionAmount INT
);
insert into LastTransactions values
(1, 4000),
(4, 2000),
(2, 10000);

create table DailyTransactions (
    UserID INT,
    TransactionAmount INT
);
insert into DailyTransactions values
(1, 1000),
(2, 2000),
(3, 1000);


merge into LastTransactions as target
using DailyTransactions as source
on target.UserID = source.UserID

when MATCHED then
    update set target.TransactionAmount = source.TransactionAmount

when NOT MATCHED by target then
    insert (UserID, TransactionAmount)
    values (source.UserID, source.TransactionAmount);

select * from LastTransactions