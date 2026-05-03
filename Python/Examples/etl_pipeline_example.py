"""
Complete ETL Pipeline Example
Demonstrates production-ready ETL pattern with error handling, logging, and monitoring.
"""

import pandas as pd
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ETLPipeline:
    """Production-ready ETL pipeline"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.metrics = {
            'start_time': None,
            'end_time': None,
            'records_extracted': 0,
            'records_transformed': 0,
            'records_loaded': 0,
            'errors': 0
        }
    
    def run(self):
        """Execute ETL pipeline"""
        self.metrics['start_time'] = datetime.now()
        logger.info("Starting ETL pipeline")
        
        try:
            # Extract
            logger.info("Step 1: Extracting data")
            raw_data = self.extract()
            self.metrics['records_extracted'] = len(raw_data)
            logger.info(f"Extracted {len(raw_data)} records")
            
            # Transform
            logger.info("Step 2: Transforming data")
            transformed_data = self.transform(raw_data)
            self.metrics['records_transformed'] = len(transformed_data)
            logger.info(f"Transformed {len(transformed_data)} records")
            
            # Load
            logger.info("Step 3: Loading data")
            self.load(transformed_data)
            self.metrics['records_loaded'] = len(transformed_data)
            logger.info(f"Loaded {len(transformed_data)} records")
            
            self.metrics['end_time'] = datetime.now()
            duration = (self.metrics['end_time'] - self.metrics['start_time']).total_seconds()
            
            logger.info(f"Pipeline completed successfully in {duration:.2f} seconds")
            return self.metrics
            
        except Exception as e:
            self.metrics['end_time'] = datetime.now()
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            raise
    
    def extract(self) -> pd.DataFrame:
        """Extract data from source"""
        input_file = self.config['input_file']
        
        # Read CSV with optimizations
        df = pd.read_csv(
            input_file,
            dtype={
                'user_id': 'int32',
                'category': 'category'
            },
            parse_dates=['created_at']
        )
        
        return df
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform data"""
        # Data cleaning
        df = df.dropna(subset=['user_id', 'amount'])
        
        # Data validation
        df = df[df['amount'] > 0]
        
        # Add derived columns
        df['amount_usd'] = df['amount'] * 1.1
        df['year'] = df['created_at'].dt.year
        df['month'] = df['created_at'].dt.month
        
        # Categorize
        df['tier'] = pd.cut(
            df['amount'],
            bins=[0, 100, 500, float('inf')],
            labels=['bronze', 'silver', 'gold']
        )
        
        return df
    
    def load(self, df: pd.DataFrame):
        """Load data to destination"""
        output_file = self.config['output_file']
        
        # Write to Parquet (efficient format)
        df.to_parquet(
            output_file,
            compression='snappy',
            index=False
        )
        
        logger.info(f"Data written to {output_file}")


if __name__ == "__main__":
    # Configuration
    config = {
        'input_file': 'data/input.csv',
        'output_file': 'data/output.parquet'
    }
    
    # Run pipeline
    pipeline = ETLPipeline(config)
    metrics = pipeline.run()
    
    print(f"\nPipeline Metrics:")
    print(f"  Extracted: {metrics['records_extracted']}")
    print(f"  Transformed: {metrics['records_transformed']}")
    print(f"  Loaded: {metrics['records_loaded']}")
    print(f"  Duration: {(metrics['end_time'] - metrics['start_time']).total_seconds():.2f}s")
