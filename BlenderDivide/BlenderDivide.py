import boto3
import json

def criatask(dStartFrame,dEndFrame):
    
    
    environment = []
    
    environment.append(
        {
            'name':'STARTFRAME',
            'value':str(dStartFrame)
            })

    environment.append(
        {
            'name':'ENDFRAME',
            'value':str(dEndFrame)
            })

    environment.append(
        {
            'name':'SCENE',
            'value':'TheFinalCut'
            })

    environment.append(
       {
            'name':'ARQBLENDER',
            'value':'ArquivoBlenderCortes.blend'
            })

    environment.append(
        {
            'name':'OUTPREFIX',
            'value':'EnzoLuigi_'
            })


    client = boto3.client('ecs')
    
   
    response = client.run_task(
        cluster = "faresys",
        count = 1,
        launchType = "FARGATE",
        networkConfiguration = {
            'awsvpcConfiguration': {
                "subnets": ("subnet-1b1b0625","subnet-4409c722","subnet-4da6726c", "subnet-4da6726c","subnet-65d04928","subnet-d11b9bdf"),
                "securityGroups":["sg-9af964bf"],
                "assignPublicIp":"ENABLED"
                
            }
        },
        overrides = {
            'containerOverrides': [
                {
                    'name': 'faresys',
                    'environment': environment
                }]
        },
        platformVersion = "1.4.0",
        taskDefinition = "faresys:10"
        )
    print(response)
    # TODO implement

dStart = 4117
dEnd = 162075
dPasso = int ((dEnd-dStart)/32)

for i in range(32):
    if  i == 31:
        dFim = dEnd
    else:
        dFim = dStart+dPasso
    criatask(dStart,dFim)
    dStart = dFim+1
