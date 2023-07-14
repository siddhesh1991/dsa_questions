import pandas as pd
import os
from config import s3_bucket_name
import boto3

def write_output(results, output_type, analysis_name):
    # Convert results to a DataFrame for easy writing to CSV or S3
    df = pd.DataFrame(results)

    if output_type == 'csv':
        filename = f"{analysis_name}_{os.environ['RUN_DATE']}.csv"
        df.to_csv(filename)
        print(f"Output written to CSV: {filename}")

    elif output_type == 's3':
        # Connect to the S3 bucket
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(s3_bucket_name)

        # Write to S3
        filename = f"{analysis_name}_{os.environ['RUN_DATE']}.csv"
        csv_buffer = StringIO()
        df.to_csv(csv_buffer)
        bucket.put_object(Key=filename, Body=csv_buffer.getvalue())
        print(f"Output written to S3 bucket '{s3_bucket_name}' with key: {filename}")
