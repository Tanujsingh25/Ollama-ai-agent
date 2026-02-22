#This file actually talks to Kubernetes
from kubernetes import client, config

config.load_kube_config()
apps = client.AppsV1Api()
core = client.CoreV1Api()

def execute(intent):
    action = intent["action"]

    if action == "get_pods":
        ns = intent.get("namespace", "default")
        pods = core.list_namespaced_pod(ns)
        return [p.metadata.name for p in pods.items]

    if action == "scale_deployment":
        apps.patch_namespaced_deployment_scale(
            name=intent["name"],
            namespace=intent["namespace"],
            body={"spec": {"replicas": intent["replicas"]}}
        )
        return "Deployment scaled successfully"

    if action == "get_logs":
        return core.read_namespaced_pod_log(
            name=intent["pod"],
            namespace=intent["namespace"]
        )

    if action == "describe_resource":
        return f"Describe {intent['resource']} not yet implemented"

    return "Unknown action"