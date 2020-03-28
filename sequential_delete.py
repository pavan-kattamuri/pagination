import time
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('BUCKET_NAME_HERE')
blobs_to_delete = [blob for blob in bucket.list_blobs(prefix="PREFIX_HERE/")]

start = time.time()
bucket.delete_blobs(blobs_to_delete)
end = time.time()
print("operation time is {} sec".format(end-start))