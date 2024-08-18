-- Creating Schema and table for data import 

create schema if not exists Churn;

use churn;
create table if not exists customer_churn (
creditScore int not null,
geography varchar(20) null,
gender varchar(15) null,
Age int not null,
tenure int null,
balance float null,
numberOfProducts int null,
hasCreditCard int not null,
isActiveMember int null,
estimated float null,
exited int not null);


-- Exploratory Data Analysis

use churn;

-- Customer segmentation based on age
SELECT 
    CASE 
        WHEN age < 20 THEN '<20'
        WHEN age BETWEEN 20 AND 29 THEN '20-29'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        WHEN age BETWEEN 50 AND 59 THEN '50-59'
        WHEN age >= 60 THEN '60+'
    END AS AgeGroup,
    COUNT(*) AS CustomerCount,
    avg(exited) as ChurnRate,
    round(avg(estimatedSalary)) as avgSalary
FROM customer_churn
group by AgeGroup
order by AgeGroup;

-- Churn rate based on Product Utilization
select numberOfProducts, avg(exited) as ChurnRate, count(*) as totalCustomers
from customer_churn
group by numberOfProducts
order by numberOfProducts;

-- Activity Impact on Churn
select isActiveMember, avg(exited) as ChurnRate, count(*) as totatMemebers
from customer_churn
group by isActiveMember;

-- Geography impact on ChurnRate
select geography, avg(exited) as ChurnRate, count(*) as totalMembers
from customer_churn
group by geography;

-- Churn rate based on tenures
select
      case when tenure < 3 then '0-3'
      when tenure between 3 and 6 then '3-6'
      when tenure between 7 and 10 then '7-10'
      end as tenures,
      avg(exited) as ChurnRate
from customer_churn
group by tenures
order by tenures;

-- Detecting age outliers
with iqr as (
select Age, ntile(4) over(order by Age) as quartiles
from customer_churn
)

select max(Age), quartiles
from iqr
where quartiles in (1,3)
group by quartiles;

-- using the quartiles method we get ages
-- IQR = 44 - 32 = 12
-- lower limit = IQR1 - 1.5(iqr) = 32 - (1.5 * 12) = 14
-- upper limit = IQR3 + 1.5(iqr) = 44 + (1.5 * 12) = 62

select count(*) as totalCustomers
from customer_churn
where age between 14 and 62; 