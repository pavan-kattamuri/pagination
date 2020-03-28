from google.cloud import storage

storage_client = storage.Client()
bucket_name = 'BUCKET_NAME_HERE'
bucket = storage_client.get_bucket(bucket_name)
blob_list = storage_client.list_blobs(
    bucket_name,
    fields='items(name,contentType)',
    prefix='PREFIX_HERE/')