SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ) #from https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
podman build -t vg "${SCRIPT_DIR}"
podman run --rm -it -v "${PWD}":/vg --workdir /vg vg