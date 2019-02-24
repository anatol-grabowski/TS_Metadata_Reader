shift PTSs and DTSs of audio and video streams inside .ts
don't shift PCRs though

## Installation
install python3 and pipenv
`pipenv install`

## Example
pipenv run python tsr.py path/to/file.ts 100000

saves shifted.ts in the cwd
