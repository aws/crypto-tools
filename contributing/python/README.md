[//]: # "Copyright Amazon.com Inc. or its affiliates. All Rights Reserved."
[//]: # "SPDX-License-Identifier: CC-BY-SA-4.0"

# Developing on AWS Crypto Tools Python projects

This file covers various in-depth topics that you might encounter
while contributing to our Python projects.

# Upstream Dependencies

## pyca/cryptography

`pyca/cryptography` is our preferred Python cryptographic backend.
As part of their CI,
they [test several of their downstream consumers](https://github.com/pyca/cryptography/tree/master/.travis/downstream.d)
to catch changes that break those consumers early.
The [AWS Encryption SDK for Python](https://github.com/aws/aws-encryption-sdk-python)
and the [DynamoDB Encryption Client for Python](https://github.com/aws/aws-dynamodb-encryption-python)
are among those downstream dependencies.

Early on,
[changes to our dependencies](https://github.com/pyca/cryptography/issues/4297)
would sometimes
[transitively break](https://github.com/pyca/cryptography/issues/4415)
`pyca`'s downstream tests of our libraries.
In order to avoid this,
we introduced frozen test dependencies
that `pyca`'s downstream tests use.

The frozen test dependencies are stored in
`test/upstream-requirements-py27.txt`
and `test/upstream-requirements-py37.txt`.
You can update the frozen test dependencies with the
`freeze-upstream-requirements-py27`
and `freeze-upstream-requirements-py37`
`tox` environments.
You can test the frozen test dependencies with the
`test-upstream-requirements-py27`
and `test-upstream-requirements-py27`
`tox` environments.
The CI for each project requires these test environments to succeed.

The integration tests for both of these libraries
require certain environment variables to be set.
However, the non-integration tests MUST complete successfully
if those environment variables are not set.
We test this using the
[`nocmk`](https://github.com/aws/aws-encryption-sdk-python/blob/97d9468375603a708d6fa9cb6703c3fc174501a6/tox.ini#L59-L69)
`tox` test environment.
**It is critical that these test environments unset all environment variables.
This ensures that the local tests work successfully
in environments where the integration test environment variables have not been set.**
