SELECT 
    e.id, 
    w.name as workflow, 
    e.status,
    substring(d.data from '\"node\":\"([^\"]+)\"') as failed_node,
    substring(d.data from '\"message\":\"([^\"]+)\"') as error_message
FROM execution_entity e
JOIN execution_data d ON e.id = d."executionId"
JOIN workflow_entity w ON e."workflowId" = w.id
WHERE e.id IN ('4111', '4108', '4104', '4009')
ORDER BY e."startedAt" DESC;
