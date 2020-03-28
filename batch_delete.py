import time
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('BUCKET_NAME_HERE')
blobs_to_delete = [blob for blob in bucket.list_blobs(prefix="PREFIX_HERE/")]

MAX_ONCE = 1000
count = 0
start = time.time()
while count < len(blobs_to_delete):
    with storage_client.batch():
        for blob in blobs_to_delete[count:count+MAX_ONCE]:
            blob.delete()
        count = count + MAX_ONCE
end = time.time()
print("operation time is {} sec".format(end-start))