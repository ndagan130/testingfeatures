import boto3

client = boto3.client(
    's3',
    aws_access_key_id=AKIAYKS7MSSWWEFNRHFG,
    aws_secret_access_key=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
)

print(client.list_buckets())
