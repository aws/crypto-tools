# Repository Management Tenets and Goals

## Definitions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
[RFC 2119](https://tools.ietf.org/html/rfc2119).

## What this document is

The purpose of this document is to define our tenets and goals
for how we will manage our repositories.
This will serve as the point of reference for all other documents
that discuss how to achieve those goals.

## What this document is not

This document does *not* discuss how we will achieve any of these goals.


## Tenets

1. [Mechanisms, not good intentions.](#Mechanisms)
1. [If it's not written down, it doesn't exist.](#Written Rules)
1. [Rules must be machine-enforceable.](#Enforceable Rules)
1. [Minimal human involvement.](#Human Involvement)
1. [Simple human intervention.](#Human Intervention)


### Mechanisms

If we care about something happening,
it MUST NOT be dependent on the good intentions of humans.
It MUST be enforceable without direct human action.

### Written Rules

If we care about managing something about a repository,
we MUST write that thing down.
Unwritten rules cannot be enforced by mechanisms.

This is important for two reasons:

1. We must be able to efficiently communicate our requirements to all maintainers.
    The only way that we can do this reliably is by writing them down.
1. Maintainers understanding our requirements is necessary but not sufficient.
    We must also communicate those requirements to our users and contributors.
    The only way that we can do this reliably is by writing them down.

### Enforceable Rules

Any rules that we define MUST be machine enforceable.
If a machine cannot enforce a rule then that rule is not sufficiently well defined.

For a rule to be enforceable, it MUST NOT be ambiguous.

For example, if we want to require that unit tests complete
then we MUST define branch protection rules that enforce that requirement.

This is important for two reasons:

1. If we have not defined our requirements well enough for a machine to enforce them,
    then we have not defined them well enough for all humans to understand them.
1. If a rule requires human judgement to be applied,
    then that rule is incomplete.

Ambiguity in life is unavoidable, but ambiguity MUST be the exception.

For example, it is reasonable to have a rule that states clearly when a human must be engaged,
but it is not reasonable to have a rule that states that a human must always be engaged
in order to determine 

### Human Involvement

Humans should not need to engage with automation unless something has gone wrong
or a situation is sufficiently ambiguous to go beyond the known rules.

When a situation does pass a defined ambiguity threshold,
our automation MUST automatically halt and request human intervention.

### Human Intervention

Anyone with write access to a repository MUST be able to stop any automation
if they think something has gone wrong or will go wrong
or if they think that a situation is sufficiently ambiguous.
