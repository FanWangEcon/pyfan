import boto3
import platform as platform
import yaml
from os import path


def boto3_start_service(st_aws_service='s3'):
    st_plotform = platform.release()

    # platform specific path
    if 'amzn' not in st_plotform:

        snm_aws_yml = "C:/Users/fan/fanwangecon.github.io/_data/aws.yml"
        if path.isfile(snm_aws_yml):
            fl_yaml = open(snm_aws_yml)
            ls_dict_yml = yaml.load(fl_yaml, Loader=yaml.BaseLoader)
            # Get the first element of the yml list of dicts
            aws_yml_dict_yml = ls_dict_yml[0]

            # Use AWS Personal Access Keys etc to start boto3 client
            aws_service = boto3.client(st_aws_service,
                                       aws_access_key_id=aws_yml_dict_yml['aws_access_key_id'],
                                       aws_secret_access_key=aws_yml_dict_yml['aws_secret_access_key'],
                                       region_name=aws_yml_dict_yml['region'])

    else:
        aws_service = boto3.client(st_aws_service)

    return aws_service
