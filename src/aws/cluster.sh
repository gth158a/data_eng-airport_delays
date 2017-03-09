aws emr create-cluster \
      --region 'us-east-1' --release-label 'emr-5.3.1' \
      --applications Name=Spark --name "$1" \
      --steps file://step.json \
      --log-uri 's3n://aws-logs-054866707802-us-east-1/elasticmapreduce/' \
      --ec2-attributes '{"KeyName":"the_cloud",
      "InstanceProfile":"EMR_EC2_DefaultRole", "SubnetId":"subnet-e86819b3",
      "EmrManagedSlaveSecurityGroup":"sg-58a9d424",
      "EmrManagedMasterSecurityGroup":"sg-5ea9d422"}' \
      --instance-groups '[{"InstanceCount":2,
      "InstanceGroupType":"CORE","InstanceType":"m3.2xlarge",
      "Name":"Core Instance Group"},
      {"InstanceCount":1,"InstanceGroupType":"MASTER",
      "InstanceType":"m3.2xlarge","Name":"Master Instance Group"}]' \
      --service-role EMR_DefaultRole --configurations
      '[{"Classification":"spark","Properties":
      {"maximizeResourceAllocation":"true"},"Configurations":[]}]'

  // File is run as "bash cluster.sh <nameOfCluster>"
