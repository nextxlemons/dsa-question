-- Last updated: 7/23/2026, 3:49:39 PM
SELECT teacher_id, count(DISTINCT subject_id) as cnt
FROM Teacher
GROUP BY teacher_id