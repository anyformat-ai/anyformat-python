# Anyformat

Methods:

- <code title="get /">client.<a href="./src/anyformat/_client.py">health_check</a>() -> object</code>

# Health

Methods:

- <code title="get /health/">client.health.<a href="./src/anyformat/resources/health.py">check</a>() -> object</code>

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

Types:

```python
from anyformat.types import FileCreateResponse, FileListResponse
```

Methods:

- <code title="post /v2/files/">client.files.<a href="./src/anyformat/resources/files.py">create</a>(\*\*<a href="src/anyformat/types/file_create_params.py">params</a>) -> <a href="./src/anyformat/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /v2/files/">client.files.<a href="./src/anyformat/resources/files.py">list</a>(\*\*<a href="src/anyformat/types/file_list_params.py">params</a>) -> <a href="./src/anyformat/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v2/files/{collection_id}/">client.files.<a href="./src/anyformat/resources/files.py">delete</a>(collection_id) -> None</code>
- <code title="get /v2/files/{collection_id}/extraction/">client.files.<a href="./src/anyformat/resources/files.py">get_extraction_results</a>(collection_id) -> object</code>

# Workflows

Types:

```python
from anyformat.types import (
    Workflow,
    WorkflowListResponse,
    WorkflowListRunsResponse,
    WorkflowRunResponse,
    WorkflowUploadResponse,
)
```

Methods:

- <code title="post /v2/workflows/">client.workflows.<a href="./src/anyformat/resources/workflows.py">create</a>() -> <a href="./src/anyformat/types/workflow.py">Workflow</a></code>
- <code title="get /v2/workflows/{workflow_id}/">client.workflows.<a href="./src/anyformat/resources/workflows.py">retrieve</a>(workflow_id) -> <a href="./src/anyformat/types/workflow.py">Workflow</a></code>
- <code title="get /v2/workflows/">client.workflows.<a href="./src/anyformat/resources/workflows.py">list</a>(\*\*<a href="src/anyformat/types/workflow_list_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_list_response.py">WorkflowListResponse</a></code>
- <code title="delete /v2/workflows/{workflow_id}/">client.workflows.<a href="./src/anyformat/resources/workflows.py">delete</a>(workflow_id) -> None</code>
- <code title="get /v2/workflows/{workflow_id}/runs/">client.workflows.<a href="./src/anyformat/resources/workflows.py">list_runs</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_list_runs_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_list_runs_response.py">WorkflowListRunsResponse</a></code>
- <code title="get /v2/workflows/{workflow_id}/results/">client.workflows.<a href="./src/anyformat/resources/workflows.py">results</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_results_params.py">params</a>) -> object</code>
- <code title="post /v2/workflows/{workflow_id}/run/">client.workflows.<a href="./src/anyformat/resources/workflows.py">run</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_run_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_run_response.py">WorkflowRunResponse</a></code>
- <code title="post /v2/workflows/{workflow_id}/upload/">client.workflows.<a href="./src/anyformat/resources/workflows.py">upload</a>(workflow_id, \*\*<a href="src/anyformat/types/workflow_upload_params.py">params</a>) -> <a href="./src/anyformat/types/workflow_upload_response.py">WorkflowUploadResponse</a></code>
