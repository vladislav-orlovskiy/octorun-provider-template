import rpyc
import os
class Provider(rpyc.Service):

    def exposed_request_runner(self, labels: str, gh_runner_token: str, org: str,):
        print("Requesting github-runner with labels: ", labels)
        print("Github runner token: ", gh_runner_token)
        print("Github org: ", org)
        command = f"""export name=self-hosted-$(date +%s)
                    docker run -d --name "$name" \\
                    -e RUNNER_SCOPE=org \\
                    -e ORG_NAME={org} \\
                    -e "RUNNER_NAME=$name" \\
                    -e RUNNER_LABELS={labels} \\
                    -e RUNNER_TOKEN={gh_runner_token} \\
                    -e RUNNER_WORKDIR=/tmp \\
                    -v "/var/run/docker.sock:/var/run/docker.sock" \\
                    -e RUNNER_POST_RUN_SCRIPT=post.sh \\
                    myoung34/github-runner:latest && \\
                    echo "kill 1" > /tmp/post.sh && docker cp '/tmp/post.sh' "$name:post.sh" && \\
                    rm -f '/tmp/post.sh'
                """
        print("Command to run: ", command)
        try:
            exit_code = os.system(command)
                    #allow container to die after job is complete
            if exit_code != 0:
                error = "Error: Failed to start github-runner"
                raise Exception(error)
            return f"Runner github-runner started with labels {labels} successfully"
        except Exception as e:
            error = f"Error: {e}"
            return error
