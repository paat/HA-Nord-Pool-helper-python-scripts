
# HA-Nord-Pool-Helper Python Scripts

## Overview
This project contains Python scripts designed to integrate with Home Assistant for managing devices based on Nord Pool electricity prices. It optimizes device operation by considering dynamic pricing, helping to save on energy costs.

## Requirements
- Home Assistant installation.
- Nordpool integration (HACS)
- Git (for cloning the repository).
- Python 3.x (as used by Home Assistant).

## Installation and Deployment

### Step 1: Clone the Repository
To get started, go to homeassistant python_scripts folder (create if does not exist). Use the following command:
```bash
git clone https://github.com/paat/HA-Nord-Pool-helper-python-scripts.git
```

### Step 2: Copy Scripts to Home Assistant
After cloning, copy the Python scripts to your Home Assistant's `python_scripts` directory. If you're running Home Assistant OS or Supervised, you can use the `update_and_copy.sh` script included in the repository:
```bash
sh update_and_copy.sh
```
Make sure that the script has execute permissions (`chmod +x update_and_copy.sh`).

### Step 3: Configure Home Assistant
- Enable the Python Scripts integration by adding `python_script:` to your Home Assistant's `configuration.yaml` file.
- Configure nordpool
  - Rename nordpool sensor id to sensor.nordpool (script assumes sensor.nordpool exists)
  - Configure price to be in cents
- Restart Home Assistant to apply the changes.

### Step 4: Create input_boolean Helper
Create input_boolean helper for the device. The helper can be used in automations to control your electricity consuming device.

### Step 5: Create Automations
Create automations in Home Assistant to utilize these scripts. This can be done via the Home Assistant UI under the "Automations" section.

## Usage example

### Example: Create input_boolean Helper
Settings -> Devices & Services -> Helper -> (Create Helper) -> Toggle
- Give a descriptive name, example: low_price_switch_boiler
- id of the device will be input_boolean.low_price_switch_boiler

### Example: Create Automations
You first need automations that would execute python script and update input_boolean states.
If this is done, you need to automations for switching the device on and off
#### Automation for updating input_boolean states
You can copy-paste this yaml into automation creation window:
```yaml
alias: nordpool_set_low_price_status_boolean_inputs
description: Set low price status for boolean inputs that control device on/off
trigger:
  - platform: state
    entity_id:
      - sensor.nordpool
condition: []
action:
  - service: python_script.set_low_price_status
    data:
      input_boolean_id: input_boolean.low_price_switch_boiler
      number_of_hours: 4
      low_price: 1
mode: single
```
- The  python script is triggered by any changes in sensor.nordpool.
- For each input_boolean you can add new action/service row
  - input_boolean_id: device-id of the helper (created in previous step)
  - number_of_hours: how many hours device must be on during 24-hour period
  - low_price: price threshold in cents. At such a low price device can be switched on without optimisation.

#### Automation for switching device on/off
- Note, you can have similar automation for climate (turn down/up heating)
- It is much easier to configure this automation via HA user interface.
##### Switch on Automation
```yaml
alias: Boiler - input boolean - turn on
description: ""
trigger:
  - platform: state
    entity_id:
      - input_boolean.low_price_switch_boiler
condition:
  - condition: state
    entity_id: input_boolean.low_price_switch_boiler
    state: "on"
action:
  - type: turn_on
    device_id: 70082b9547d0e8726a52e621a33ffc82
    entity_id: e79e39b842e3563656538d59054d962f
    domain: switch
mode: single
```
##### Switch off Automation
```yaml
alias: Boiler - input boolean - switch off
description: ""
trigger:
  - platform: state
    entity_id:
      - input_boolean.low_price_switch_boiler
condition:
  - condition: state
    entity_id: input_boolean.low_price_switch_boiler
    state: "off"
action:
  - type: turn_off
    device_id: 70082b9547d0e8726a52e621a33ffc82
    entity_id: e79e39b842e3563656538d59054d962f
    domain: switch
mode: single
```

## Contributing
Contributions to the project are welcome. Please ensure to follow best practices and guidelines when submitting pull requests or issues.
