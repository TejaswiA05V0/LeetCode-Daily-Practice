select max(salary) as secondHighestSalary
from Employee
where salary<(select max(salary) from Employee);
