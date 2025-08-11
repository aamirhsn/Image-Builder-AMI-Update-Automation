#!/usr/bin/env python
import boto3

ami_name = "TestIamge"
param = "ami"

def get_ami_id():
    ec2 = boto3.client('ec2')
    response = ec2.describe_images(
    Owners=["0123456789"],
    Filters=[{'Name': 'name', 'Values': [ami_name]}, {'Name': 'creation-date', 'Values': ['2022-10-22T*']}])
    return response['Images'][1]['ImageId']
    
def replace_ami(param):
    ssm = boto3.client('ssm')
    parameter = ssm.put_parameter(Name= param, Value='ami-0123456789', Overwrite= True)
    return parameter


#def launch_stack():
#    try:
#        cf_client = boto3.client('cloudformation')
#        stackdata= cf_client.update_stack(
#        StackName='run',
#        TemplateURL='[https://test-pwsh.s3.amazonaws.com/cfn.yaml]')
#    except Exception as e:
#        print(str(e))
#    return stackdata

def handler(event, context):
    #ami_result= get_ami_id()
    replace_result= replace_ami(param)
    #stack_result= launch_stack()
    #print(ami_result)
    print(replace_result)
    
	
	parameter['Parameter']['Value'])
