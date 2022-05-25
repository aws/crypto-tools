# Repository Management Tenets and Goals

## What this document is

The purpose of this document is to define our tenets and goals
for how we will manage our repositories.
This will serve as the point of reference for all other documents
that discuss how to achieve those goals.

## What this document is not

This document does *not* discuss how we will achieve any of these goals.
Implementation requirements and approaches are discussed in other documents.

## Definitions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
[RFC 2119](https://tools.ietf.org/html/rfc2119).

* **Requirement** : A requirement is something that MUST be true.
    An example of this could be that secrets MUST NOT be committed in code.
* **Preference** : A preference is something that SHOULD be true,
    but that we will not force to be true.
    An example of this could be design patterns or code formatting.

## Tenets

1. [Mechanisms, not good intentions.](#Mechanisms)
1. [If it's not written down, it doesn't exist.](#Written Rules)
1. [Rules must be machine-enforceable.](#Enforceable Rules)
1. [Minimal human involvement.](#Human Involvement)
1. [Simple human intervention.](#Human Intervention)
1. [Be Consistent.](#Consistency)

### Mechanisms

Requirements MUST NOT depend on the good intentions of humans.
They MUST be enforceable without direct human action.

### Written Rules

Requirements MUST be defined in written documentation.

This is important because:

1. We MUST efficiently communicate our requirements to all maintainers.
    The only way that we can do this is by writing them down.
1. We MUST communicate our requirements to our users and contributors.
    The only way that we can do this is by writing them down.
1. We cannot enforce undefined requirements.
1. We cannot know when/if/how requirements change if they are not recorded.

### Enforceable Rules

All requirements MUST be machine enforceable.
If a machine cannot enforce a requirement
then that requirement is not sufficiently well defined.

For a requirement to be enforceable, it MUST NOT be ambiguous.

For example, if we want to require that unit tests pass,
we can enforce that by defining branch protection rules
that will block a merge if the unit tests have not passed.

This is important because:

1. If we have not defined our requirements well enough for a machine to enforce them,
    then we have not defined them well enough for all humans to understand them.
1. If a rule requires human judgment to be applied,
    then that rule is incomplete.

Ambiguity in life is unavoidable, but ambiguity MUST be the exception.

For example, it is reasonable to have a rule that states clearly when a human MUST be engaged
but it is not reasonable to have a rule that states that a human MUST always be engaged.

#### Enforced Rules

All requirements SHOULD be machine enforced.

Any preferences that can be machine enforced
SHOULD be machine enforced,
and SHOULD then be made into requirements.

### Human Involvement

Humans SHOULD NOT need to engage with automation unless something has gone wrong
or a situation is too ambiguous for the automation to understand.

When a situation passes a defined ambiguity threshold
our automation MUST halt and request human intervention.

### Human Intervention

Anyone with write access to a repository MUST be able to stop any automation
if they think something has gone wrong, will go wrong,
or that a situation is sufficiently ambiguous.

### Consistency

> Special cases aren't special enough to break the rules.
>
>  -- The Zen of Python

Requirements and preferences SHOULD be consistent with relevant community norms.
Where they diverge, that divergence MUST be to raise the bar
and the reasons for that divergence MUST be clearly documented.

Requirements and preferences MUST be consistent across projects
governed by this document that share common characteristics
(ex: language, build system, etc).
