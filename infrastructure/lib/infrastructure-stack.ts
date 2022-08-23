import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lamda from 'aws-cdk-lib/aws-lambda'

export class InfrastructureStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines the stack goes here
    const apiLambda = new lamda.Function(this, "ApiFunction", {
      runtime: lamda.Runtime.PYTHON_3_9,
      code: lamda.Code.fromAsset("../app"), // location of where to run lamda
      handler: "copykitt_apy.handler" // the name of the file and handler name
    })

    // example resource
    // const queue = new sqs.Queue(this, 'InfrastructureQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
