# RedisEnterprise

> see https://aka.ms/autorest

This is the AutoRest configuration file for redisenterprise.

## Getting Started

To build the SDKs for My API, simply install AutoRest via `npm` (`npm install -g autorest`) and then run:

> `autorest readme.md`

To see additional help and options, run:

> `autorest --help`

For other options on installation see [Installing AutoRest](https://aka.ms/autorest/install) on the AutoRest github page.

---

## Configuration

### Basic Information

These are the global settings for the RedisEnterprise API.

``` yaml
openapi-type: arm
tag: package-2021-03
```


### Tag: package-2021-03

These settings apply only when `--tag=package-2021-03` is specified on the command line.

```yaml $(tag) == 'package-2021-03'
input-file:
  - ../input/Users.yml
```

---

# Code Generation

## Swagger to SDK

This section describes what SDK should be generated by the automatic system.
This is not used by Autorest itself.

``` yaml $(swagger-to-sdk)
swagger-to-sdk:
  - repo: azure-cli-extensions
```