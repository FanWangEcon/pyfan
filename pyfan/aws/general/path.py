"""
The :mod:`pyfan.aws.general.path` file paths etc

Includes method :func:`detect_store_path`, :func:`save_img`.
"""

import platform as platform
from pathlib import Path
import os
import pyfan.aws.s3.pushsync as s3_pushsync


def detect_store_path(bl_check_path_exist=True, srt_sub_path=None, st_local_path=None):
    """Detects checks if program is running on an AWS Linux Instance

    In our case, all code that run on AWS linux are running inside conda containers.
    If running on container, save to data folder. If running on some local machine
    save results to the user's home path's download folder, data subfolder.

    Parameters
    ----------
    bl_check_path_exist : `bool`
        checking saving path if it does not exist
    srt_sub_path: `string`, optional
        this is the subpath to be used, in the data folder in EC2 container,
        or inside the downloads data folder under user directory.
    st_local_path: `string`, optional
        local overriding string save path, if not, use download/data folder. This
        will replace the local path

    Returns
    -------
    tuple[bool, string]
        returns boolean if on amzn splatform, then the directory where to store save files
    """

    # detect platform
    st_plotform = platform.release()

    # platform specific path
    if 'amzn' in st_plotform:
        amzn_linux_status = True
        spt_local_directory = '/data/'
        if srt_sub_path is not None:
            spt_local_directory = os.path.join(spt_local_directory, srt_sub_path)
    else:
        amzn_linux_status = False
        if st_local_path is None:
            spt_local_directory = os.path.join(str(Path.home()), 'Downloads', 'data')
            if srt_sub_path is not None:
                spt_local_directory = os.path.join(spt_local_directory, srt_sub_path)
        else:
            spt_local_directory = st_local_path

    # generate path if it does not exist
    if bl_check_path_exist:
        Path(spt_local_directory).mkdir(parents=True, exist_ok=True)

    return amzn_linux_status, spt_local_directory


def save_img(plt, sna_image_name, spt_image_path=None,
             dpi=300, papertype='a4',
             orientation='horizontal',
             bl_upload_s3=False, st_s3_bucket=None, srt_s3_bucket_folder=None):
    """Saves Graph Locally, and also upload to S3 if requested

    Given figure object,

    Parameters
    ----------
    plt: `matplotlib.pyplot`
        a matplotlib pyplot object from a graph that was just generated
    sna_image_name: `string`
        image name, without the suffix of png
    spt_image_path: `string`, optional
        path to image, if None, then use default local path in :func:`detect_store_path`
    dpi: `integer`, optional
        image dpi
    papertype: `string`, optional
        One of 'letter', 'legal', 'executive', 'ledger', 'a0' through 'a10', 'b0' through 'b10'.
    orientation: `string`, optional
        'horizontal' or 'portrait'
    bl_upload_s3: `bool`, optional
        if file will be uploaded to s3
    st_s3_bucket: `string`, optional
        Assuming that AWS credentials are already stored in the container on EC2
        or locally in a .aws credential file. So `st_s3_bucket` bucket name refers
        to bucket in the credentialed user's s3 account.
    srt_s3_bucket_folder: `string`, optional
        folder in s3 bucket to store image

    Returns
    -------
    tuple[bool, string]
        returns boolean if on amzn splatform, then the directory where to store save files
    """

    # Get Image Path, locally or locally in Ec2 Container
    amzn_linux_status, spt_local_directory = detect_store_path(bl_check_path_exist=True,
                                                               srt_sub_path=srt_s3_bucket_folder,
                                                               st_local_path=spt_image_path)

    # Save image locally
    snm_image_name = sna_image_name + '.png'
    spn_img_pwdfn = os.path.join(spt_local_directory, snm_image_name)
    plt.savefig(spn_img_pwdfn, dpi=dpi, papertype=papertype, orientation=orientation)

    # Given locally saved image copy over to aws
    if bl_upload_s3:
        s3_pushsync.s3_upload(spn_img_pwdfn, st_s3_bucket, srt_s3_bucket_folder)
