# DevTools Integration for Home Assistant

--------

[![GitHub Release][releases-shield]][releases]
![Downloads][download-latest-shield]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
[![Build Status][build-shield]][build]
![Made with Love in Norway][madewithlove-shield]

The `devtools` integration is a custom Home Assistant component designed to fill gaps and simplify tasks for the creator.
This integration currently provides a single feature that allows users to call any command registered with the WebSocket API as an action (previously known as a service) and get its response.

## Installation

### HACS

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bendikrb&repository=ha-devtools&category=Integration)

Or
Search for `Developer tools` in HACS and install it under the "Integrations" category.

### Manual Installation
<details>
<summary>More Details</summary>

* You should take the latest [published release](https://github.com/bendikrb/ha-devtools/releases).
* To install, place the contents of `custom_components` into the `<config directory>/custom_components` folder of your Home Assistant installation.
* Restart Home Assistant
* In the HA UI go to Settings -> Integrations click "+" and search for "Developer tools"
</details>

## Configuration is done in the UI

The configuration UI will guide you through adding the integration to Home Assistant, you just need a [long-lived access token](https://developers.home-assistant.io/docs/auth_api/#long-lived-access-token) which can be created in the "Security" section of your Home Assistant profile page.


## Features

### Action: `call_ws_endpoint`

The `devtools.call_ws_endpoint` action enables you to call any command registered with the Home Assistant WebSocket API and retrieve its response. This can be particularly useful for debugging, testing, or automating tasks that require direct interaction with the WebSocket API.

#### Service Data

- `type` (string) - The WebSocket API command to call.
- `data` (dictionary, optional) - The parameters to pass to the command.

#### Example Usage

```yaml
action: devtools.call_ws_endpoint
data:
  type: "validate_config"
  data:
    trigger: ...
    condition: ...
    action: ...
```


***
[commits-shield]: https://img.shields.io/github/commit-activity/y/bendikrb/ha-devtools.svg?style=flat
[commits]: https://github.com/bendikrb/ha-devtools/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat
[logo]: https://brands.home-assistant.io/devtools/logo.png
[icon]: https://brands.home-assistant.io/devtools/icon.png
[build-shield]: https://github.com/bendikrb/ha_devtools/actions/workflows/validate.yaml/badge.svg
[build]: https://github.com/bendikrb/ha_devtools/actions/workflows/validate.yaml
[license-shield]: https://img.shields.io/github/license/bendikrb/ha-devtools.svg?style=flat
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40bendikrb-blue.svg?style=flat
[releases-shield]: https://img.shields.io/github/release/bendikrb/ha-devtools.svg?style=flat
[releases]: https://github.com/bendikrb/ha-devtools/releases
[download-latest-shield]: https://img.shields.io/github/downloads/bendikrb/ha-devtools/latest/total?style=flat
[madewithlove-shield]: https://madewithlove.now.sh/no?heart=true&colorB=%233584e4
