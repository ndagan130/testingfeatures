import boto3

client = boto3.client(
    's3',
    aws_access_key_id=AKIAYKS7MSSWWE5NRHFG,
    aws_secret_access_key=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
)
print(client.list_buckets())
