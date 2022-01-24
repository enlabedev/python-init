## Setup git

Set a name on your `local` git config

```bash
# e.g.:
$ git config --local user.name "{{ first name }} {{ last name }}"
```

Set an email on your `local` git config

```bash
# suggestion, use your private github email
# e.g.:
$ git config --local user.email "xxxxxxxxxx@users.noreply.github.com"
```

Set a pull strategy on your `local` git config, avoid a warning on every `git pull` since version `2.27`

```bash
$ git config --local pull.rebase false
```

## Setup init
Run python config
```bash
# e.g.:
$ python project-setup.py
```

After Run Task after
- View command palette: ctrl + shift + p (for Mac cmd + shift + p)
- Tasks: Run Task
- Choose task based on operating system
