[//]: # "Copyright Amazon.com Inc. or its affiliates. All Rights Reserved."
[//]: # "SPDX-License-Identifier: CC-BY-SA-4.0"

# Getting started with AWS Crypto Tools projects

This file covers general concepts that apply to
all AWS Crypto Tools projects.

## Language Specifics

Getting started guides for each language:

- [Python](./python/README.md)

## Operations

## Forks

Every user must create their own fork of the project repository.
Any development must be done on that user's fork
and pull requests come from a branch on the user's fork
to a branch on the project fork.

## Branches and Pull Requests

We recommend that you never make changes to the branch
that you intend to make a pull request into.
In other words,
if you want to make a pull request into the `development` branch on the project fork,
do not make changes in the `development` branch on your fork.
Instead, make a new branch on your fork
that branches from `development`
and contains your changes.

```shell script
git checkout development
git checkout -b my-awesome-changes
```

Keeping branches separate like this
helps you and us keep track of and organize changes,
especially when multiple pull requests might be merging into the same branch
over the same time period.
For example,
if you and someone else both open a pull request to `development`
at the same time with different changes,
one of those pull requests will be merged first.
Once the other pull request merges,
you now need to reconcile your pull request with the merged changes.
This is simplest if your changes and the merged changes
are in separate branches
and your `development` branch
always has the same state as
the project fork's `development` branch.

## CI

Our projects use a variety of CI platforms:

- [GitHub Actions](https://docs.github.com/en/actions) :
  Linux, MacOS, and Windows CI platform tightly integrated with GitHub.
- [TravisCI](https://travis-ci.org/)
  Linux and MacOS CI platform.
  **NOTE: We do not frequently use TravisCI for MacOS testing.**
- [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
  Linux and Windows CI platform.
- [AppVeyor](https://www.appveyor.com/) :
  Windows CI platform.
  **NOTE: Usually only used on older projects
  that we have not migrated to something else yet.**
