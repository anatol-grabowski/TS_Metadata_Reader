shifts PTSs and DTSs of audio and video streams inside .ts, doesn't shift PCRs

## Installation
install python3 and pipenv, clone the repo, `pipenv install` from the project dir

## Usage
`pipenv run python tsr.py path/to/file.ts 100000`

saves shifted.ts into the cwd
