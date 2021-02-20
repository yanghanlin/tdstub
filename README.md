# tdstub

[![Build status](https://github.com/YangHanlin/tdstub/actions/workflows/build-image.yml/badge.svg)](https://github.com/YangHanlin/tdstub/actions/workflows/build-image.yml) [![Deploy status](https://github.com/YangHanlin/tdstub/actions/workflows/deploy-image.yml/badge.svg)](https://github.com/YangHanlin/tdstub/actions/workflows/deploy-image.yml)

An API server to reveal system information and runtime environment, as well as to echo incoming request. It is designed to be used for test purposes, especially when deployed in containers/to k8s clusters.

## API Reference

### Request

**Method:** Any

**Endpoint:** Any

**Query parameters:** Any

### Response

**Status code:** `200 OK`, while it is possible to control the status code by providing a special query parameter `status` with value of expected status code

**Response body:** See example

### Example

**Request header**

```
POST /some/random/path?somekey=somevalue&status=400
```

**Request body**

```json
{
  "somekeyinbody": "somevalue"
}
```

**Response header**

```
HTTP 400 Bad Request
```

**Response body**

```jsonc
{
  // system information and runtime environment
  "environment": {
    // information about current server instance
    "instance": {
      "uid": "9720421b-6cac-46a7-87e2-a64262be3349", // unique id for every server instance
      "description": "Instance initialized at 2021-02-20T07:43:24.660941"
    },
    // information about host machine
    "host": {
      // basic information about hardware and OS
      "platform": {
        "architecture": "x86_64",
        "os": "Linux-5.4.0-65-generic-x86_64-with-glibc2.28",
        "processor": ""
      },
      // basic information about Python runtime
      "runtime": {
        "python": {
          "implementation": "CPython",
          "version": "3.9.1"
        },
        "django": "3.1.6",
        "drf": "3.12.2"
      },
      // basic information about hostname and network interfaces
      "network": {
        "hostname": "stub-stable-7f595d5456-gj4pl",
        "interfaces": {
          "lo": {
            "ips": [
              "127.0.0.1",
              "('::1', 0, 0)"
            ]
          },
          "eth0": {
            "ips": [
              "10.42.1.59",
              "('fe80::2461:9eff:fe27:edb0', 0, 3)"
            ]
          }
        }
      },
      // list of environment variables
      "environment_variables": {
        "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "HOSTNAME": "stub-stable-7f595d5456-gj4pl",
        "LANG": "C.UTF-8",
        "GPG_KEY": "E3FF2839C048B25C084DEBE9B26995E310250568",
        "PYTHON_VERSION": "3.9.1",
        "PYTHON_PIP_VERSION": "21.0.1",
        "PYTHON_GET_PIP_URL": "https://github.com/pypa/get-pip/raw/4be3fe44ad9dedc028629ed1497052d65d281b8e/get-pip.py",
        "PYTHON_GET_PIP_SHA256": "8006625804f55e1bd99ad4214fd07082fee27a1c35945648a58f9087a714e9d4",
        "APP_NAME": "stub",
        "CURRENT_CHANNEL": "stable",
        "CURRENT_GIT_COMMIT": "8af6a9e3238605446944d4524d1987dd27143197",
        "CURRENT_GIT_REF": "main",
        "KUBERNETES_SERVICE_HOST": "10.43.0.1",
        "KUBERNETES_SERVICE_PORT": "443",
        "KUBERNETES_PORT_443_TCP_PORT": "443",
        "STUB_STABLE_PORT_18000_TCP_PROTO": "tcp",
        "STUB_UNSTABLE_PORT_18001_TCP_ADDR": "10.43.73.26",
        "KUBERNETES_PORT": "tcp://10.43.0.1:443",
        "KUBERNETES_PORT_443_TCP_PROTO": "tcp",
        "KUBERNETES_PORT_443_TCP_ADDR": "10.43.0.1",
        "STUB_STABLE_PORT": "tcp://10.43.47.58:18000",
        "STUB_UNSTABLE_SERVICE_PORT": "18001",
        "STUB_UNSTABLE_PORT_18001_TCP": "tcp://10.43.73.26:18001",
        "KUBERNETES_PORT_443_TCP": "tcp://10.43.0.1:443",
        "STUB_STABLE_SERVICE_HOST": "10.43.47.58",
        "STUB_STABLE_SERVICE_PORT": "18000",
        "STUB_STABLE_PORT_18000_TCP_PORT": "18000",
        "STUB_UNSTABLE_SERVICE_HOST": "10.43.73.26",
        "KUBERNETES_SERVICE_PORT_HTTPS": "443",
        "STUB_STABLE_PORT_18000_TCP": "tcp://10.43.47.58:18000",
        "STUB_STABLE_PORT_18000_TCP_ADDR": "10.43.47.58",
        "STUB_UNSTABLE_PORT": "tcp://10.43.73.26:18001",
        "STUB_UNSTABLE_PORT_18001_TCP_PROTO": "tcp",
        "STUB_UNSTABLE_PORT_18001_TCP_PORT": "18001",
        "HOME": "/root",
        "DJANGO_SETTINGS_MODULE": "tdstub.settings",
        "TZ": "UTC",
        "RUN_MAIN": "true"
      }
    }
  },
  // information about current incoming request
  "request": {
    "path": "/some/random/path",
    "method": "POST",
    "headers": {
      "Content-Length": "36",
      "Content-Type": "application/json",
      "Host": "localhost:18000",
      "Connection": "close",
      "User-Agent": "PostmanRuntime/7.26.8",
      "Accept": "*/*",
      "Postman-Token": "f479b9ff-4a1c-43ec-b6ac-972bd5530e2b",
      "Accept-Encoding": "gzip, deflate, br"
    },
    "query_params": {
      "somekey": "somevalue",
      "status": "400"
    },
    "data": {
      "somekeyinbody": "somevalue"
    }
  }
}
```
