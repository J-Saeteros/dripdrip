import csv
import boto3 
import pickle
import os


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

def get_labels(imgs):
    labels = []

    return labels

def main():

    print('Running from ' + os.getcwd() + '...')

    ac_key,sa_key = get_keys(keys_path + 'keys.csv')

    client = boto3.client('rekognition','us-east-1',aws_access_key_id = ac_key, aws_secret_access_key = sa_key)

    img_files = os.listdir(rsrc_path)
    imgs = []

    for img_file in img_files:
        with open(rsrc_path, 'rb') as image:
            imgs.append(image)


    labels = get_labels(imgs)




if __name__ == '__main__':
    main()
