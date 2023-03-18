from aws_cdk import (
    Stack,
    pipelines,
    aws_codepipeline_actions as pipeline_actions_,
)
from constructs import Construct

class NautashAhmadPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Creating a source step for pipeline
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/CodePipelineSource.html#aws_cdk.pipelines.CodePipelineSource.git_hub
        source = pipelines.CodePipelineSource.git_hub(
            'nautash2022skipq/Sprint-03', 'master',
            authentication='NautashAhmadGithubPATToken',
            trigger=pipeline_actions_.GitHubTrigger('POLL')
        )
        
        # Creating a build step for pipeline
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/ShellStep.html
        synth = pipelines.ShellStep(
            'NautashAhmadPipelineShellStep',
            commands=[
                'npm install -g aws-cdk',
                'pip install -r requirements.txt',
                'cd nautash_ahmad/',
                'cdk synth',
                'cdk deploy --profile nautash2022skip',
            ]
        )