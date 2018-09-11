# User Analytics (Python)

## Installation

```sh
cd user-analytics-py
pip install .
```

## Usage

```python
import useranalytics
client = useranalytics.UserAnalytics(
    token='...',
    endpoint='https://4i0ifsvq23.execute-api.us-west-2.amazonaws.com/staging')
client.list()
client.describe('UserAnalytics')
client.post('UserAnalytics', {'foo':'bar'})
```
