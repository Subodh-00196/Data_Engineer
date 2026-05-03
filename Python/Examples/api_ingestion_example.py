"""
API Data Ingestion Example
Demonstrates production patterns for API data ingestion with retry logic, 
rate limiting, and error handling.
"""

import requests
import time
import logging
from typing import List, Dict
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def retry_with_backoff(max_retries=3, backoff_factor=2):
    """Decorator for retry logic with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.Timeout, 
                        requests.exceptions.ConnectionError) as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= backoff_factor
        return wrapper
    return decorator


def rate_limited(max_per_second):
    """Decorator to enforce rate limiting"""
    min_interval = 1.0 / max_per_second
    
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed
            
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        
        return wrapper
    return decorator


class APIIngestion:
    """API data ingestion with best practices"""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    @retry_with_backoff(max_retries=3)
    @rate_limited(max_per_second=10)
    def fetch_page(self, endpoint: str, page: int, page_size: int = 100) -> Dict:
        """Fetch single page from API"""
        url = f"{self.base_url}/{endpoint}"
        params = {'page': page, 'limit': page_size}
        
        response = self.session.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    def fetch_all_pages(self, endpoint: str, page_size: int = 100) -> List[Dict]:
        """Fetch all pages from paginated API"""
        all_records = []
        page = 1
        
        while True:
            logger.info(f"Fetching page {page} from {endpoint}")
            
            try:
                data = self.fetch_page(endpoint, page, page_size)
                
                # Handle different pagination formats
                if isinstance(data, list):
                    records = data
                elif 'results' in data:
                    records = data['results']
                elif 'data' in data:
                    records = data['data']
                else:
                    records = []
                
                if not records:
                    logger.info(f"No more data. Total records: {len(all_records)}")
                    break
                
                all_records.extend(records)
                logger.info(f"Fetched {len(records)} records. Total: {len(all_records)}")
                
                # Check if there are more pages
                if len(records) < page_size:
                    break
                
                page += 1
                
            except Exception as e:
                logger.error(f"Error fetching page {page}: {e}")
                break
        
        return all_records
    
    def close(self):
        """Close session"""
        self.session.close()


def main():
    """Example usage"""
    # Initialize API client
    api = APIIngestion(
        base_url='https://api.example.com',
        api_key='your_api_key_here'
    )
    
    try:
        # Fetch data from multiple endpoints
        endpoints = ['users', 'products', 'orders']
        
        for endpoint in endpoints:
            logger.info(f"Processing endpoint: {endpoint}")
            records = api.fetch_all_pages(endpoint)
            
            # Process records (save to database, file, etc.)
            logger.info(f"Fetched {len(records)} records from {endpoint}")
            
    finally:
        api.close()


if __name__ == "__main__":
    main()
