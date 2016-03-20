#!/bin/sh

# generate from the content modified 1 day ago or earlier

wok_dir=`dirname $(readlink -f $0)`

if [[ -d "${wok_dir}/content" ]] && [[ `find "${wok_dir}/content" "${wok_dir}/templates" -type f -mtime -1 2> /dev/null | wc -l` -ne 0 ]]; then
  cd "${wok_dir}" && wok
fi
