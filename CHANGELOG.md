# Changelog

## 0.1.0a4

- Add number reuse, phone readiness, and SMS reception start for Activation V2.
- Preserve method-specific HTTP 202 responses, retryAfter and nullable order expiry.
- Cover all 61 operations while preserving the existing 58 contracts.

## 0.1.0a3

- Add all-country and country-specific compact Activation counts with optional provider ratings.
- Preserve raw counts, rating fields, country casing, documented authentication and all existing method names.
- Cover all 58 operations with local mock and wire-contract tests.

## 0.1.0a2

- Improve installation and quickstart instructions, API coverage and contextual links to the SMSPVA service, documentation and support.
- Update package descriptions and homepage metadata.


## 0.1.0a1

- Add synchronous and asynchronous Python clients for all 56 documented Activation V2, Rental and Private Email operations.
- Preserve documented HTTP methods, parameters, response fields, pending SMS and no-stock results.
- Include typed parameters and response dictionaries, timeout handling, and an SMS polling helper with a saved expiry.
- Add MIT licensing and local contract tests. Alternative API is excluded.

This alpha has not been validated against paid production operations.
