SELECT e.id, w.name, e.status, e."startedAt" 
FROM execution_entity e 
JOIN workflow_entity w ON e."workflowId" = w.id 
WHERE e.status IN ('error', 'failed') 
ORDER BY e."startedAt" DESC 
LIMIT 10;
