"""Python script that checks the operational status of AWS services."""

def main():
  service = 'Lambda'

  service_status = get_service_status(service)

  if service_status:
    print(f"\n{service} service status: '{service_status}'")  

    if service_status == "Operational":
      print(f"Performing operations on '{service}'.")
    else:
      print(f"'{service}' is NOT operational.")
  else:
    print(f"Status of {service} could not be retrieved.")

def get_service_status(service_name):
  aws_service_status = {
      'EC2': 'Maintenance',
      'S3': 'Operational',
      'Lambda': 'Issues Detected',
      'DynamoDB': 'Operational',
      'RDS': 'Operational',
  }
  try:
    return aws_service_status[service_name]
  except KeyError as ke:
    print(f"Error: {ke}. Status for AWS service {service_name} is not available in our records.")
    return None
  

if __name__ == '__main__':
  main() 
