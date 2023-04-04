import boto3

client = boto3.client(
    's3',
    aws_access_key_id=AKIAYKS7MSSWZEFNRHFG,
    aws_secret_access_key=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
)

print(client.list_buckets())
