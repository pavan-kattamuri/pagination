import time
from google.cloud import storage

storage_client = storage.Client()
bucket = storage_client.get_bucket('BUCKET_NAME_HERE')
start = time.time()
blobs_to_patch = [blob for blob in bucket.list_blobs(prefix="PREFIX_HERE/")]
print("Total objects to be patched {}".format(len(blobs_to_patch)))

count = 0
MAX_ONCE = 1000
while count < len(blobs_to_patch):
    with storage_client.batch():
        for blob in blobs_to_patch[count:count+MAX_ONCE]:
            blob.content_type = 'image/png'
            blob.patch()
        count = count + MAX_ONCE
end = time.time()
print("operation time is {} sec".format(end-start))