-- Last updated: 7/23/2026, 3:49:44 PM
-- Write your PostgreSQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state 
from Person p
LEFT JOIN Address a
ON p.personID = a.personID;