-- displays maximum temp for each state
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
