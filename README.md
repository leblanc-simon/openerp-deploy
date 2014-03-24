# OpenERP Deploy

A very simple tools to deploy an OpenERP application

**CAUTION : ** not ready for production

## Usage

Create an app.json to define your application

```javascript
{
    "name": "My OpenERP installation",
    "version": "1.0.0",

    "openerp": {
        "server": "lp:ocb-server",
        "addons": "lp:ocb-addons",
        "web": "lp:ocb-web"
    },

    "addons": {
        "enova": {
            "my-personal-module": "lp:openerp-personal-module/7.0"
        },
        "extras": {
            "openerp-connector": "lp:openerp-connector/7.0",
            "sale-wkfl": "lp:sale-wkfl/7.0"
        }
    },

    "libraries": [
        "requests==0.14.2"
    ],

    "download": {
        "scripts": {
            "my-script.py": "https://example.org/custom.py",
            "my-script-2.py": "https://example.org/custom-2.py"
        },
        "backup": {
            "psqlbackup.sh": "https://example.org/psqlbackup.sh"
        }
    },

    "pre-execute": [
        ["ls", "-l"],
        ["ls", "-la"]
    ],

    "post-execute": [
        ["echo", "'toto'"]
    ]
}
```

This app.json :

* Execute ```ls -l``` and ```ls -la```
* Install OpenERP server, addons and web from ocb's branches
* Install your personal module
* Install openerp-connector and sale-wkfl modules
* Install the python's library "requests" v0.14.2
* Download :
  * ```custom.py``` into ```scripts/my-script.py```
  * ```custom-2.py``` into ```scripts/my-script-2.py```
  * ```psqlbackup.sh``` into ```backup/psqlbackup.sh```
* Execute ```echo 'toto'```

Then, run ```main.py```

**Examples** :

* Install OpenERP and your defined modules, then show the configuration

```bash
python main.py -s -f app.json /home/openerp
```

* Install your defined modules without OpenERP, then show the configuration

```bash
python main.py -o -s -f app.json /home/openerp
```

See ```python main.py -h``` for all options

## TODOs

* remove "enova" from addons and accept multi-keys
* process SQL patch (require to define a database)
* write OpenERP configuration file
* secure process


## License

* [WTFPL](http://www.wtfpl.net/)

## Author

* Simon Leblanc : <contact@leblanc-simon.eu>
