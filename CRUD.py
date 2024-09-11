import boto3
import json

# Initialize a connection to DynamoDB
dynamodb = boto3.resource('dynamodb')

# Access the DynamoDB table named 'StudentRecords'
student_table = dynamodb.Table('StudentRecords')  

def lambda_handler(event, context):
    # Determine the type of action requested
    action = event.get('action')
    
    try:
        if action == 'create':
            return handle_createStudent(event)
        elif action == 'read':
            return handle_readStudent(event)
        elif action == 'delete':
            return handle_deleteStudent(event)
        elif action == 'update':
            return handle_updateStudent(event)
        else:
            # Return 404 if the action is not recognized
            return {
                'statusCode': 404,
                'body': json.dumps('Action not found')
            }
    
    except Exception as ex:
        # Return 500 for any errors encountered
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {str(ex)}')
        }

# Creating the student record into the StudentRecords DB
def handle_createStudent(event):
    student_id = event['student_id']
    name = event['name']
    course = event['course']    
    student_table.put_item(
        Item={
            'student_id': student_id,
            'name': name,
            'course': course
        }
    ) 
    return {
        'statusCode': 200,
        'body': json.dumps('Student record has been successfully created.')
    }

# Reading the student record basis the primary Key student_id
def handle_readStudent(event):
    student_id = event['student_id']
    rsp = student_table.get_item(
        Key={
            'student_id': student_id
        }
    )
    
    item = rsp.get('Item', {})
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
  
# Deleting the student record basis the parimary Key Student_id
def handle_deleteStudent(event):
    student_id = event['student_id']
    student_table.delete_item(
        Key={
            'student_id': student_id
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Student record has been successfully deleted.')
    }
    
# Updating the student record like name and course basis the primary key
def handle_updateStudent(event):
    student_id = event['student_id']
    name = event.get('name')
    course = event.get('course')
    # Initialize parts for the update expression and attribute values
    expression_attribute_values,expression_attribute_names = {},{}
    update_expression_parts = []
    
    if name:
        update_expression_parts.append(" #name = :name")
        expression_attribute_values[':name'] = name
        expression_attribute_names['#name'] = 'name'
    
    if course:
        update_expression_parts.append(" #course = :course")
        expression_attribute_values[':course'] = course
        expression_attribute_names['#course'] = 'course'
    # Combine the update expression parts into a single string
    update_expression = "SET " + ", ".join(update_expression_parts)
    # Perform the update operation on DynamoDB
    student_table.update_item(
        Key={
            'student_id': student_id
        },
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="UPDATED_NEW"
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Student record has been successfully updated.')
    }
