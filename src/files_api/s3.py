import boto3

try:
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.type_defs import PutObjectOutputTypeDef
except ImportError:
    print("boto3-stubs[s3] is not installed")

BUCKET_NAME = "cloud-course-bucket-jordan"

# session = boto3.Session(profile_name="cloud-course")
session = boto3.Session()

s3_client: "S3Client" = session.client("s3")

response: "PutObjectOutputTypeDef" = s3_client.put_object(
    Bucket=BUCKET_NAME,
    Key="hello.txt",
    Body="Hello, world!",
    ContentType="text/plain",  # ContentType allows us to view text in browser w/o downloading the file
)
