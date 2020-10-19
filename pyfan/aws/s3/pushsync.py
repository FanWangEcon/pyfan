"""
The :mod:`pyfan.aws.s3.pushsync` savse files to s3 and syncs

Includes method :func:`ar_draw_random_normal`.
"""

import os
import pyfan.aws.general.credentials as aws_credentials


def s3_upload(spn_img_pwdfn, st_s3_bucket='fans3testbucket', srt_s3_bucket_folder='pyfan_scatterline3'):
    """Upload an existing file to s3

    Upload to a particular bucket and subfolder, file in some local directory

    Parameters
    ----------
    spn_img_pwdfn: `string`
        full path to image, including the image name
    st_s3_bucket: `string`, optional
        Assuming that AWS credentials are already stored in the container on EC2
        or locally in a .aws credential file. So `st_s3_bucket` bucket name refers
        to bucket in the credentialed user's s3 account.
    srt_s3_bucket_folder: `string`, optional
        folder in s3 bucket to store image

    Returns
    -------
    none

    Examples
    --------
    >>> spn_img_pwdfn = 'C:/Users/fan/Downloads/data/test/test_image.png'
    >>> st_s3_bucket = 'fans3testbucket'
    >>> srt_s3_bucket_folder = 'pyfan_scatterline3/folder1/'
    >>> s3_upload(spn_img_pwdfn, st_s3_bucket, srt_s3_bucket_folder)
    """

    # s3 client
    s3 = aws_credentials.boto3_start_service(st_aws_service='s3')

    # Get file Path and the file name
    srt_path, snm_file = os.path.split(spn_img_pwdfn)
    spn_s3_bucket_folder_file = os.path.join(srt_s3_bucket_folder, snm_file).replace("\\", "/")

    # Uploading
    s3.upload_file(spn_img_pwdfn, st_s3_bucket, spn_s3_bucket_folder_file)
