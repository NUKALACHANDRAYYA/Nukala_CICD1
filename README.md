Mounting a GCS Bucket in Cloud Run via UI

1. Configuring the Volume in Cloud Run

Navigate to the Cloud Run Console.

Scroll down to the "Volumes" section under the "Container(s), Volumes, Networking, Security" tab.

Click "Add Volume".

Select "Cloud Storage" as the volume type.

Provide the GCS Bucket Name (YOUR_BUCKET_NAME).

Enter a Volume Name (this will be used in the next step).

Set the Volume Access to Read-Write, so your application can create and delete files.

Click "Done".

2. Mounting the Volume to the Container

Scroll down to the "Containers" section under the "Container(s), Volumes, Networking, Security" tab.

Click on the "Volume Mounts" tab.

Click "Add Mount Volume".

Select the Volume Name from the dropdown (this will be auto-populated from the previous step).

Enter the Mount Path (e.g., /mnt/gcs).

Click "Done".


This ensures your application can read, write, and delete files from the bucket as expected.
# python-jenkins-app
