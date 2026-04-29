# Health

Types:

```python
from anyformat.types import HealthCheckResponse
```

Methods:

- <code title="get /health/">client.health.<a href="./src/anyformat/resources/health.py">check</a>() -> <a href="./src/anyformat/types/health_check_response.py">HealthCheckResponse</a></code>

# Webhooks

Types:

```python
from anyformat.types import WebhookCreateResponse, WebhookListResponse
```

Methods:

- <code title="post /v2/webhooks/">client.webhooks.<a href="./src/anyformat/resources/webhooks.py">create</a>(\*\*<a href="src/anyformat/types/webhook_create_params.py">params</a>) -> <a href="./src/anyformat/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /v2/webhooks/">client.webhooks.<a href="./src/anyformat/resources/webhooks.py">list</a>() -> <a href="./src/anyformat/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v2/webhooks/{webhook_id}/">client.webhooks.<a href="./src/anyformat/resources/webhooks.py">delete</a>(webhook_id) -> None</code>

# Files

Methods:

- <code title="delete /v2/files/{collection_id}/">client.files.<a href="./src/anyformat/resources/files.py">delete</a>(collection_id) -> None</code>

# Workflows

Types:

```python
from anyformat.types import (
    Workflow,
    WorkflowListResponse,
    WorkflowCreateFileResponse,
    WorkflowGetFileResultsResponse,
    WorkflowListFilesResponse,
    WorkflowListRunsResponse,
    WorkflowRunResponse,
    WorkflowUploadResponse,
)
```

Methods:

- <code title="post /v2/workflows/">client.workflows.<a href="./src/anyformat/resources/workflows.py">create</a>(\*\*<a href="src/anyformat/types/workflow_create_params.py">params</a>) -> <a href="./src/anyformat/types/workflow.py">Workflow</a></code>
- <code title="get /v2/workflows/{workflow_id}/">client.workflows.<a href="./src/anyformat/resources/workflows.py">retrieve</a>(workflow_id) -> <a href="./src/anyformat/types/workflow.py">Workflow</a></code>
- <code title="get /v2/workflows/">client.workflows.<a href="./src/anyformat/resources/workflows.py">list</a>(\*\*<a href="src/anyformat/types/workflow_list_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_list_response.py">WorkflowListResponse</a></code>
- <code title="delete /v2/workflows/{workflow_id}/">client.workflows.<a href="./src/anyformat/resources/workflows.py">delete</a>(workflow_id) -> None</code>
- <code title="post /v2/workflows/{workflow_id}/files/">client.workflows.<a href="./src/anyformat/resources/workflows.py">create_file</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_create_file_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_create_file_response.py">WorkflowCreateFileResponse</a></code>
- <code title="get /v2/workflows/{workflow_id}/files/{collection_id}/results/">client.workflows.<a href="./src/anyformat/resources/workflows.py">get_file_results</a>(collection_id, \*, workflow_id) -> <a href="./src/anyformat/types/workflow_get_file_results_response.py">WorkflowGetFileResultsResponse</a></code>
- <code title="get /v2/workflows/{workflow_id}/files/">client.workflows.<a href="./src/anyformat/resources/workflows.py">list_files</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_list_files_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_list_files_response.py">WorkflowListFilesResponse</a></code>
- <code title="get /v2/workflows/{workflow_id}/runs/">client.workflows.<a href="./src/anyformat/resources/workflows.py">list_runs</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_list_runs_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_list_runs_response.py">WorkflowListRunsResponse</a></code>
- <code title="post /v2/workflows/{workflow_id}/run/">client.workflows.<a href="./src/anyformat/resources/workflows.py">run</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_run_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_run_response.py">WorkflowRunResponse</a></code>
- <code title="post /v2/workflows/{workflow_id}/upload/">client.workflows.<a href="./src/anyformat/resources/workflows.py">upload</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_upload_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_upload_response.py">WorkflowUploadResponse</a></code>
