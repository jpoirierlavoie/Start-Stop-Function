import googleapiclient.discovery
import os

def start_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().start(project=os.environ['PROJECT'], zone=os.environ['ZONE'], instance=os.environ['NAME']).execute()
    return result

def stop_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().stop(project=os.environ['PROJECT'], zone=os.environ['ZONE'], instance=os.environ['NAME']).execute()    
    return result