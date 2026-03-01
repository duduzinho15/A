SELECT "executionId", data->'resultData'->'error' as error_msg FROM execution_data WHERE "executionId" IN (4111, 4108, 4104, 4009);
