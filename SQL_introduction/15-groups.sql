-- list the number of records with the same score in the table second_table
-- The result should display:
--   the score
--   the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
-- run: cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

-- Selects the score column from the second_table.
-- Counts the occurrences of each unique score value in the second_table.
-- This count is aliased as number.
SELECT score, COUNT(score) AS number 

FROM second_table 
GROUP BY score 
ORDER BY number DESC;