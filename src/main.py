import csv
import boto3 
import pickle
import os

import pdb


## Paths
## we assume we run from src folder
bin_path = '../bin/'  #out dir
rsrc_path = '../rsrc/'  #out dir
keys_path = '../keys/'  #out dir




def get_keys(file):
    cred = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            cred.append(row)

    return cred[0]['Access key ID'] , cred[0]['Secret access key']

def get_labels(img_file,client):
    labels = []

    print('Opening img: ' + rsrc_path + img_file)

    with open(rsrc_path + img_file, 'rb') as image:

        response = client.detect_labels(Image = {'Bytes' : image.read()})

        if len(response['Labels']) == 0:
            print(img_file + ' has no labels')  #maybe print the image file  

        else:

            for l in response['Labels']:
                fields = {}
                fields['Name'] = l['Name']
                fields['Confidence'] = l['Confidence']
                fields['Full_Response'] = response
                labels.append(fields)

    return labels

def main():

    print('Running from ' + os.getcwd() + '...')

    ac_key,sa_key = get_keys(keys_path + 'keys.csv')

    client = boto3.client('rekognition','us-east-1',aws_access_key_id = ac_key, aws_secret_access_key = sa_key)



    img_files = os.listdir(rsrc_path)
    img_data = []

    for i in img_files:
        img_data.append((i,get_labels(i,client)))



    for d in img_data:
        print(d[0] + ' has labels:');

        for l in img_data[1]:
            print(l)



if __name__ == '__main__':
    main()
