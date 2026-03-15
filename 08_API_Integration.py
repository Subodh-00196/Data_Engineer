"""
================================================================================
                    REST API - DATA ENGINEER INTERVIEW GUIDE
================================================================================
REST API examples and integration patterns for Data Engineering
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. HTTP METHODS (GET, POST, PUT, DELETE, PATCH)
2. API AUTHENTICATION
3. ERROR HANDLING & RETRY LOGIC
4. PAGINATION
5. RATE LIMITING
6. API INTEGRATION WITH PYSPARK
7. REAL-WORLD EXAMPLES
8. BEST PRACTICES
================================================================================
"""

import requests
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# ============================================================================
# 1. HTTP METHODS (GET, POST, PUT, DELETE, PATCH)
# ============================================================================

""" GET Request - Retrieve data """
base_url = 'https://api.example.com/data'

# Simple GET request
response = requests.get(base_url)
if response.status_code == 200:
    data = response.json()
    print("GET Response:", data)
else:
    print(f"GET request failed with status code {response.status_code}")

# GET with query parameters
params = {'page': 1, 'limit': 100, 'status': 'active'}
response = requests.get(base_url, params=params)

# GET with headers
headers = {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json'
}
response = requests.get(base_url, headers=headers)

""" POST Request - Create new resource """
payload = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'age': 30
}

response = requests.post(base_url, json=payload)
if response.status_code == 201:
    data = response.json()
    print("POST Response:", data)
else:
    print(f"POST request failed with status code {response.status_code}")

""" PUT Request - Update entire resource """
resource_id = 1
url_put = f"{base_url}/{resource_id}"
payload_put = {
    'name': 'John Updated',
    'email': 'john.updated@example.com',
    'age': 31
}

response = requests.put(url_put, json=payload_put)
if response.status_code == 200:
    data = response.json()
    print("PUT Response:", data)
else:
    print(f"PUT request failed with status code {response.status_code}")

""" PATCH Request - Partial update """
url_patch = f"{base_url}/{resource_id}"
payload_patch = {'email': 'john.newemail@example.com'}

response = requests.patch(url_patch, json=payload_patch)
if response.status_code == 200:
    data = response.json()
    print("PATCH Response:", data)
else:
    print(f"PATCH request failed with status code {response.status_code}")

""" DELETE Request - Delete resource """
url_delete = f"{base_url}/{resource_id}"
response = requests.delete(url_delete)
if response.status_code == 204:
    print("Resource deleted successfully")
else:
    print(f"DELETE request failed with status code {response.status_code}")

# ============================================================================
# 2. API AUTHENTICATION
# ============================================================================

""" Bearer Token Authentication """
token = "YOUR_ACCESS_TOKEN"
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
response = requests.get(base_url, headers=headers)

""" API Key Authentication """
# In header
headers = {'X-API-Key': 'YOUR_API_KEY'}
response = requests.get(base_url, headers=headers)

# In query parameter
params = {'api_key': 'YOUR_API_KEY'}
response = requests.get(base_url, params=params)

""" Basic Authentication """
from requests.auth import HTTPBasicAuth

response = requests.get(
    base_url,
    auth=HTTPBasicAuth('username', 'password')
)

# Or using tuple
response = requests.get(base_url, auth=('username', 'password'))

""" OAuth 2.0 Authentication """
# Get access token
token_url = 'https://api.example.com/oauth/token'
token_data = {
    'grant_type': 'client_credentials',
    'client_id': 'YOUR_CLIENT_ID',
    'client_secret': 'YOUR_CLIENT_SECRET'
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()['access_token']

# Use access token
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get(base_url, headers=headers)

# ============================================================================
# 3. ERROR HANDLING & RETRY LOGIC
# ============================================================================

""" Basic Error Handling """
try:
    response = requests.get(base_url, timeout=10)
    response.raise_for_status()  # Raises HTTPError for bad status codes
    data = response.json()
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except json.JSONDecodeError as json_err:
    print(f"JSON decode error: {json_err}")

""" Retry Logic with Exponential Backoff """
def make_request_with_retry(url, max_retries=3, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = backoff_factor ** attempt
                print(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"All {max_retries} attempts failed")
                raise

""" Using requests.Session with Retry """
def create_session_with_retry():
    session = requests.Session()
    
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS", "POST"]
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session

# Usage
session = create_session_with_retry()
response = session.get(base_url)

# ============================================================================
# 4. PAGINATION
# ============================================================================

""" Offset-based Pagination """
def fetch_all_pages_offset(base_url, page_size=100):
    all_data = []
    offset = 0
    
    while True:
        params = {'limit': page_size, 'offset': offset}
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
        
        data = response.json()
        
        if not data or len(data) == 0:
            break
        
        all_data.extend(data)
        offset += page_size
        
        print(f"Fetched {len(all_data)} records so far...")
    
    return all_data

""" Page-based Pagination """
def fetch_all_pages_numbered(base_url, page_size=100):
    all_data = []
    page = 1
    
    while True:
        params = {'page': page, 'per_page': page_size}
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
        
        data = response.json()
        
        if not data or len(data) == 0:
            break
        
        all_data.extend(data)
        page += 1
        
        print(f"Fetched page {page - 1}, total records: {len(all_data)}")
    
    return all_data

""" Cursor-based Pagination """
def fetch_all_pages_cursor(base_url):
    all_data = []
    next_cursor = None
    
    while True:
        params = {'cursor': next_cursor} if next_cursor else {}
        response = requests.get(base_url, params=params)
        
        if response.status_code != 200:
            break
        
        result = response.json()
        data = result.get('data', [])
        
        if not data:
            break
        
        all_data.extend(data)
        next_cursor = result.get('next_cursor')
        
        if not next_cursor:
            break
        
        print(f"Fetched {len(all_data)} records so far...")
    
    return all_data

# ============================================================================
# 5. RATE LIMITING
# ============================================================================

""" Simple Rate Limiting """
import time

def rate_limited_request(url, requests_per_second=10):
    delay = 1.0 / requests_per_second
    
    response = requests.get(url)
    time.sleep(delay)
    
    return response

""" Rate Limiting with Token Bucket """
class RateLimiter:
    def __init__(self, rate_limit, time_period=1):
        self.rate_limit = rate_limit
        self.time_period = time_period
        self.tokens = rate_limit
        self.last_update = time.time()
    
    def acquire(self):
        now = time.time()
        elapsed = now - self.last_update
        
        # Refill tokens
        self.tokens = min(
            self.rate_limit,
            self.tokens + elapsed * (self.rate_limit / self.time_period)
        )
        self.last_update = now
        
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            sleep_time = (1 - self.tokens) * (self.time_period / self.rate_limit)
            time.sleep(sleep_time)
            self.tokens = 0
            self.last_update = time.time()
            return True

# Usage
limiter = RateLimiter(rate_limit=100, time_period=60)  # 100 requests per minute

for i in range(150):
    limiter.acquire()
    response = requests.get(f"{base_url}/{i}")
    print(f"Request {i + 1} completed")

""" Handle 429 (Too Many Requests) """
def make_request_with_rate_limit_handling(url):
    max_retries = 5
    
    for attempt in range(max_retries):
        response = requests.get(url)
        
        if response.status_code == 429:
            # Check Retry-After header
            retry_after = response.headers.get('Retry-After')
            
            if retry_after:
                wait_time = int(retry_after)
            else:
                wait_time = 2 ** attempt  # Exponential backoff
            
            print(f"Rate limited. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
        elif response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    raise Exception("Max retries exceeded for rate limiting")

# ============================================================================
# 6. API INTEGRATION WITH PYSPARK
# ============================================================================

""" Fetch API Data and Create PySpark DataFrame """
from pyspark.sql import SparkSession
import requests

spark = SparkSession.builder.appName("APIIntegration").getOrCreate()

# Fetch data from API
def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed: {response.status_code}")

# Get data
api_url = "https://api.example.com/users"
data = fetch_api_data(api_url)

# Create DataFrame
df = spark.createDataFrame(data)
df.show()

""" Parallel API Calls with PySpark """
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import requests

def call_api(user_id):
    try:
        url = f"https://api.example.com/users/{user_id}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('email')
        return None
    except:
        return None

# Register UDF
call_api_udf = udf(call_api, StringType())

# Apply to DataFrame
user_ids = spark.createDataFrame([(1,), (2,), (3,)], ["user_id"])
enriched_df = user_ids.withColumn("email", call_api_udf("user_id"))
enriched_df.show()

""" Batch API Calls """
def fetch_users_batch(user_ids, batch_size=100):
    all_users = []
    
    for i in range(0, len(user_ids), batch_size):
        batch = user_ids[i:i + batch_size]
        
        # API that accepts batch requests
        response = requests.post(
            "https://api.example.com/users/batch",
            json={'user_ids': batch}
        )
        
        if response.status_code == 200:
            all_users.extend(response.json())
        
        time.sleep(0.1)  # Rate limiting
    
    return all_users

# ============================================================================
# 7. REAL-WORLD EXAMPLES
# ============================================================================

""" Example 1: Fetch Weather Data """
def fetch_weather_data(city, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

""" Example 2: REST API to S3 Pipeline """
import boto3
import json
from datetime import datetime

def api_to_s3_pipeline(api_url, s3_bucket, s3_prefix):
    # Fetch data from API
    response = requests.get(api_url)
    data = response.json()
    
    # Transform data
    transformed_data = []
    for record in data:
        transformed_data.append({
            'id': record['id'],
            'name': record['name'],
            'processed_at': datetime.now().isoformat()
        })
    
    # Upload to S3
    s3_client = boto3.client('s3')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    s3_key = f"{s3_prefix}/data_{timestamp}.json"
    
    s3_client.put_object(
        Bucket=s3_bucket,
        Key=s3_key,
        Body=json.dumps(transformed_data),
        ContentType='application/json'
    )
    
    print(f"Data uploaded to s3://{s3_bucket}/{s3_key}")
    return len(transformed_data)

""" Example 3: Incremental API Data Sync """
def incremental_api_sync(api_url, last_sync_timestamp):
    params = {
        'updated_after': last_sync_timestamp,
        'limit': 1000
    }
    
    all_records = []
    page = 1
    
    while True:
        params['page'] = page
        response = requests.get(api_url, params=params)
        
        if response.status_code != 200:
            break
        
        records = response.json()
        
        if not records:
            break
        
        all_records.extend(records)
        page += 1
        
        # Rate limiting
        time.sleep(0.5)
    
    # Update last sync timestamp
    if all_records:
        new_timestamp = max(record['updated_at'] for record in all_records)
        return all_records, new_timestamp
    
    return all_records, last_sync_timestamp

# ============================================================================
# 8. BEST PRACTICES
# ============================================================================

"""
API INTEGRATION BEST PRACTICES:

1. ERROR HANDLING:
   - Always handle exceptions
   - Implement retry logic with exponential backoff
   - Log errors for debugging

2. RATE LIMITING:
   - Respect API rate limits
   - Implement client-side rate limiting
   - Handle 429 responses gracefully

3. AUTHENTICATION:
   - Store credentials securely (environment variables, secrets manager)
   - Refresh tokens before expiration
   - Use appropriate auth method for API

4. PAGINATION:
   - Handle all pagination types
   - Fetch all pages for complete data
   - Monitor memory usage for large datasets

5. TIMEOUTS:
   - Always set connection and read timeouts
   - Use appropriate timeout values
   - Handle timeout exceptions

6. LOGGING:
   - Log API requests and responses
   - Log errors and retries
   - Monitor API performance

7. DATA VALIDATION:
   - Validate API responses
   - Handle missing or malformed data
   - Check response status codes

8. PERFORMANCE:
   - Use connection pooling (requests.Session)
   - Implement parallel requests when appropriate
   - Cache responses when possible

9. SECURITY:
   - Use HTTPS
   - Validate SSL certificates
   - Don't log sensitive data

10. MONITORING:
    - Track API call success/failure rates
    - Monitor response times
    - Set up alerts for failures
"""

""" Complete Example: Production-Ready API Client """
import logging
from typing import Optional, Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url: str, api_key: str, max_retries: int = 3):
        self.base_url = base_url
        self.api_key = api_key
        self.session = self._create_session(max_retries)
    
    def _create_session(self, max_retries: int) -> requests.Session:
        session = requests.Session()
        
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        return session
    
    def _get_headers(self) -> Dict[str, str]:
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = self.session.get(
                url,
                headers=self._get_headers(),
                params=params,
                timeout=30
            )
            response.raise_for_status()
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"GET {url} failed: {e}")
            return None
    
    def post(self, endpoint: str, data: Dict) -> Optional[Dict]:
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = self.session.post(
                url,
                headers=self._get_headers(),
                json=data,
                timeout=30
            )
            response.raise_for_status()
            logger.info(f"POST {url} - Status: {response.status_code}")
            return response.json()
        
        except requests.exceptions.RequestException as e:
            logger.error(f"POST {url} failed: {e}")
            return None
    
    def fetch_all_pages(self, endpoint: str, page_size: int = 100) -> List[Dict]:
        all_data = []
        page = 1
        
        while True:
            params = {'page': page, 'per_page': page_size}
            data = self.get(endpoint, params=params)
            
            if not data or len(data) == 0:
                break
            
            all_data.extend(data)
            page += 1
            logger.info(f"Fetched page {page - 1}, total records: {len(all_data)}")
        
        return all_data

# Usage
client = APIClient(
    base_url="https://api.example.com",
    api_key="YOUR_API_KEY"
)

users = client.fetch_all_pages("users")
print(f"Fetched {len(users)} users")

"""
================================================================================
END OF API INTEGRATION GUIDE
================================================================================
"""
