# EC2 Image Builder : AMI-Update-Automation
1. Gets Parent Image AMI ID
2. Modifies existing parameter store value with new AMI ID (Parameter Store name should be same as AMI name)
3. Updates CFN Stack so that new parent ami will be used

### Build Steps:
#### 1) Target Account:
1. Create Automation document "SSMAutomation_code.txt" in Target account
2. Create SSM Parameter Store in Target account
3. Go to event bus and add permissions to receive events from source account
4. Create rule with "EventPattern_TargetAccount.txt" pattern and select Target as SSM Automation (IAM role selected should have sufficient permissions like passrole and assumerole)

#### 2) Source Account:
1. Create a event rule with "EventPattern_SourceAccount.txt" event pattern and send events to target account event bus (You will target bus arn)

#### Workflow:
1. As soon as an AMI with specified name with shared with target account, an event from source will get triggered and sent to target account.
2. Event bridge will then run SSM Automation document based on the event.
3. Automation document captures new ami id and stores it in parameter store and updates CFN stack which will create new image recipe and run pipeline
