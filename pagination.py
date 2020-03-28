from google.cloud import storage

storage_client = storage.Client()
blob_list = storage_client.list_blobs(
    'BUCKET_NAME_HERE',
    fields='items(name,contentLanguage),nextPageToken',
    prefix='PREFIX_HERE/')

file_list = []

for page in blob_list.pages:
    print('=' * 20)
    print('    Page number: {:d}'.format(blob_list.page_number))
    print('  Items in page: {:d}'.format(page.num_items))
    print('     First item: {!r}'.format(next(page)))
    print('Items remaining: {:d}'.format(page.remaining))
    print('Next page token: {}'.format(blob_list.next_page_token))
    for blob in list(page):
        file_list.append(blob.name)

print("length of file list is {}".format(len(file_list)))